from .log import log
from .onfunc import *
from data.bot import isadmin
class Command:
    """
    命令类。
    
    参数:
        name: 命令名
        admin: 是否需要管理员权限
        func: 命令函数
    """
    def __init__(self, name:str, admin:bool, func):
        self.name = name
        self.admin = admin
        self.func = func
    def run(self, *args):
        return self.func(*args)

CommandList:list[Command] = []

def regCommand(command:str,admin=False,onfunc=None) -> None:
    """
    注册一个命令。

    参数:
        command: 命令名
        admin: 是否需要管理员权限 | 默认为False
        onfunc: 命令函数 | 默认为None
    """
    CommandList.append(Command(command,admin,onfunc))

def getCommand(command:str,*args) -> list:
    """
    获取一个命令并运行。

    参数:
        command: 命令名
        args: 命令参数

    返回: 命令返回值 | 错误信息
    """
    uid = int(args[0].uid)
    log("Command","info",f"<- {command}")
    for i in CommandList:
        if i.name == command:
            if i.admin == False or isadmin(uid) == True:
                try:
                    funcremsg = i.run(*args)
                except:
                    log("Command","error",f"Run Command {command} Error")
                    return [Plain("运行命令时发生错误。")]
                if(funcremsg != None):
                    log("Command","info",f"Run Command {command}")
                    return funcremsg
            else:
                log("Command","error",f"run {command} permission denied")
                return [Plain("此命令需要管理员权限。")]
    log("Command","info",f"Command {command} Not Found")
    return [Plain("未找到命令。请使用 /帮助 查看帮助。")]