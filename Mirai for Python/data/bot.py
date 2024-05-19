from .config import *
from pkg.user import *

def isAT(msg:str):
    """
    判断是否AT机器人。
    
    参数:
        msg: 消息内容

    返回: bool
    """
    if(msg.find(f"@{str(qNumber)}") == 0):
        return True
    return False

def isSend(uid:int, group:int, msg:str):
    """
    判断是否发送消息。

    参数:
        uid: 用户id
        group: 群组id
        msg: 消息内容
    
    返回: bool
    """
    if(group in groupList):
        if(atOnly):
            if(isAT(msg)):
                if(uid in blackList):
                    return False
                return True
        return False
    return False

def isadmin(uid:int):
    """
    判断是否为管理员。
    
    参数:
        uid: 用户id

    返回: bool
    """
    if(uid in adminList):
        return True
    return False

def anaAtUser(parm:str):
    """
    解析At信息。

    参数:
        parm: 消息内容

    返回: int
    """
    if(parm.find("@" == 0)):
        parm = parm[1:]
    return int(parm)