import dashscope
from .log import log, saveLog
import json
from data.config import namePath,logPath,defaultTokens,key
dashscope.api_key=key

class User:
    """
    用户类。
    
    参数：
        uid: 用户id
        tokens: 用户token数量 | 默认为10000
        chatnum: 用户对话次数 | 默认为0
        steamid: 用户steamid | 默认为"None"
    """
    def __init__(self,uid:str,tokens:int=defaultTokens,chatnum:int=0,steamid:str="None"):
        self.uid=uid
        self.mem=[]
        self.tokens=tokens
        self.chatnum=chatnum
        self.steamid=steamid
    def chat(self,msg:str)->dict[str,str]:
        """
        与AI聊天。

        参数：
            msg: 用户输入的消息

        返回: AI回复的消息 | 错误信息
        """
        log("AIChat","info","<- "+msg)
        if(self.tokens <= 0):
            log("Chat","error","-> Tokens Not Enough")
            return "Token不足。"
        self.chatnum += 1
        self.mem.append({"role":"user","content":msg})
        resp = dashscope.Generation.call(
            model='qwen-max-0428',
            messages=self.mem,
            max_tokens=256
        )
        try:
            retext = resp["output"]["text"]
            self.mem.append({"role":"assistant","content":retext})
            subtoken = int(resp["usage"]["total_tokens"])
        except:
            log("AIChat","error","-> Error")
            retext = "获取回复时发生错误。"
            subtoken = 0
            self.chatnum -= 1
            self.mem.pop()
        self.tokens -= subtoken
        log("AIChat","info","-> "+retext)
        retext = "\n"+retext+"\nToken消耗:"+str(subtoken)
        return retext
    def clearmem(self) -> None:
        """
        清空该用户对话记录。
        """
        self.mem.clear()
    def getinfo(self) -> str:
        """
        获取该用户信息。
        """
        return "UID:"+self.uid+"\nTokens:"+str(self.tokens)+"\n对话次数:"+str(self.chatnum)+"\nSteamID:"+self.steamid

userList = []
blackList = []

def userInit() -> None:
    """
    初始化用户数据。
    """
    global userList,blackList
    log("User","info"," 开始加载用户数据...")

    try:
        userdata = json.load(open(namePath+"\\userdata.json","r",encoding='utf-8'))
    except:
        log("User","error",f" 未找到{namePath}\\userdata.json。")
        userdata = []
    for i in userdata:
        userList.append(User(i["uid"],i["tokens"],i["chatnum"],i["steamid"]))

    try:
        blackdata = json.load(open(namePath+"\\blacklist.json","r",encoding='utf-8'))
    except:
        log("User","error",f" 未找到{namePath}\\blacklist.json。")
        blackList = []
    for i in blackdata:
        blackList.append(i)

    log("User","info"," 加载用户数据完成,共加载 "+str(len(userList))+" 个用户。")

def saveData() -> None:
    """
    保存用户数据。
    """
    log("User","info"," 开始保存数据...")
    userdata = []
    for i in userList:
        userdata.append({"uid":i.uid,"tokens":i.tokens,"chatnum":i.chatnum,"steamid":i.steamid})
    json.dump(userdata,open(namePath,"w",encoding='utf-8'),ensure_ascii=False)
    blackdata = []
    for i in blackList:
        blackdata.append(i)
    json.dump(blackdata,open(namePath,"w",encoding='utf-8'),ensure_ascii=False)
    log("User","info"," 保存数据完成。")

def getUser(parmuid:str)->User:
    """
    获取用户对象。

    参数：
        parmuid: 用户id

    返回: 用户对象
    """
    for i in userList:
        if i.uid == parmuid:
            return i
    userList.append(User(parmuid))
    return userList[-1]