import os
import lineTool
import time
import datetime
 
#Token = os.environ["MYTOKEN"] 
Token = "your token"
TurnOn_message = "\nRaspberry pi3 B+ turn on \n" #your message
Time_message = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) #day and time
MESSAGE = ''


time.sleep(10)
MESSAGE = TurnOn_message+ Time_message
print("Send message to Line \n%s\n" % MESSAGE)

lineTool.lineNotify(Token, MESSAGE)


input()
