from mirai import Mirai, WebSocketAdapter, GroupMessage, At
from data.bot import *
from pkg.user import *
from pkg.command import *

def Init() -> None:
    """
    机器人初始化时执行的函数。
    :可以将一些需要初始化的函数放在这里。
    """
    userInit()
    regCommand("/画图",False,getImage)
    regCommand("/信息",False,getUserInfo)
    regCommand("/重置",False,clearMem)
    regCommand("/帮助",False,getHelp)
    regCommand("/ban",True,banUser)
    regCommand("/unban",True,unBanUser)
    regCommand("/exit",True,exitBot)

if __name__ == '__main__':
    bot = Mirai(
        qq=qNumber,
        adapter=WebSocketAdapter(verify_key=Botkey, host=Host, port=Port)
    )
    Init()
    
    @bot.on(GroupMessage)
    async def on_group_message(event: GroupMessage):
        """
        机器人接收到群消息时执行的函数。

        参数:
            event: 消息事件
        """
        msg = str(event.message_chain)
        uid = event.sender.id
        gid = event.sender.group.id

        user = getUser(str(uid))

        #检查是否做出回复，并解析At信息
        if(not isSend(uid,gid,msg)):
            return
        if(isAT(msg)):
            msg = msg.replace(f"@{str(qNumber)}","")
            if(msg.find(" "+commandPrefix) == 0):
                msg = msg[1:]

        #检查是否为命令
        if(msg.find(commandPrefix) == 0):
            msg = msg.split(" ")
            #防止参数为空
            if(len(msg) == 1):
                msg.append("None")

            remsg = getCommand(msg[0],user,msg[1:])
            await bot.send_group_message(gid, remsg)
        else:
            if(aiChat):
                await bot.send_group_message(gid, [At(uid),Plain(user.chat(msg))])
            else:
                await bot.send_group_message(gid, [At(uid),Plain("没有开启AI聊天功能。")])
    bot.run()