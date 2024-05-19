from mirai import Plain,Image
from .user import *
from dashscope import ImageSynthesis
from data.bot import isadmin,anaAtUser

"""
命令处理函数

固定参数:
    user: 用户对象
    parm: 参数列表
"""

def getImage(user:User,parm:list)->list:
    """
    通过dashcope请求图片

    参数:
        prompt (str)
    
    返回: 消息链 (图片对象:Image)
    """
    pormpt = str(parm)
    img = ImageSynthesis.call(
        model = ImageSynthesis.Models.wanx_v1,
        prompt = pormpt,
        n=1,
        size = "720*1280"
        )
    try:
        reurl = img["output"]["results"][0]["url"]
    except:
        return [Plain("请求图片失败。")]
    return [Image(url=reurl)]

def getUserInfo(user:User,parm:list)->list:
    """
    获取用户信息

    返回: 消息链 (用户信息:Plain)
    """
    return [Plain(user.getinfo())]

def clearMem(user:User,parm:list)->list:
    """
    清空对话记录

    返回: 消息链 (提示信息:Plain)
    """
    user.clearmem()
    return [Plain("对话记录已清空。")]

def getHelp(user:User,parm:list)->list:
    """
    获取帮助信息

    返回: 消息链 (帮助信息:Plain)
    """
    return [Plain("/画图 <prompt> - 生成图片\n/信息 - 获取用户信息\n/重置 - 清空对话记录")]

def banUser(user:User,parm:list)->list:
    """
    封禁用户

    参数:
        uid (str)
    
    返回: 消息链 (提示信息:Plain)
    """
    if(len(parm) == 1):
        uid = anaAtUser(parm[0])
        blackList.append(uid)
        return [Plain("用户已被封禁。")]
    else:
        return [Plain("参数错误。")]

def unBanUser(user:User,parm:list)->list:
    """
    解封用户

    参数:
        uid (str)
    
    返回: 消息链 (提示信息:Plain)
    """
    if(len(parm) == 1):
        uid = anaAtUser(parm[0])
        blackList.remove(uid)
        return [Plain("用户已解封。")]
    else:
        return [Plain("参数错误。")]

def exitBot(user:User,parm:list)->None:
    """
    保存并关闭机器人
    """
    saveData()
    import os
    os._exit(0)