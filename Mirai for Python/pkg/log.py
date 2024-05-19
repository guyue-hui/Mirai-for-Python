import time

logcache = []

def log(name:str,level:str="info",msg:str="") -> None:
    if(level == "info"):
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logcache.append(f"[{time_str}] [{name}] [{level}] {msg}\n")
        print(f"[{time_str}] [{name}] [{level}] {msg}")
    if(level == "error"):
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logcache.append(f"[{time_str}] [{name}] [{level}] {msg}\n")
        print(f"\033[1;31m[{time_str}] [{name}] [{level}] {msg}\033[0m")

def saveLog(path:str) -> None:
    file_name = path + time.strftime("%Y-%m-%d-%H-%M", time.localtime()) + ".log"
    with open(file_name, 'w') as f:
        f.writelines(logcache)