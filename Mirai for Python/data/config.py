#初始化Bot的配置信息
qNumber = 123456789     #Bot的QQ号
Botkey = 'yirimirai'    #Bot的密钥
Host = 'localhost'      #Bot的主机地址
Port = 8080             #Bot的端口号

#Bot的配置信息
commandPrefix = "/"         #Bot处理消息的命令前缀 默认为"/"
atOnly = True               #是否只接受At的消息 默认为True
groupList = []              #Bot生效的群列表
adminList = []              #管理员列表

#数据存储路径
namePath = "C:\\Qbot\\Yirimirai\\" #用户数据存储路径
logPath = "C:\\Qbot\\Yirimirai\\log\\"          #日志存储路径

#dashscope的配置信息
aiChat = True                                       #是否开启Ai聊天 默认为True
key = "API_KEY"                                     #dashscope的API密钥
defaultTokens = 10000                               #默认Token数量 默认为10000