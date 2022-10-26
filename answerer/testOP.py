#import subprocess
import os
time = "16:00"
objects="PDLC"
do = "up"

#result="/home/pi/.pyenv/versions/3.7.13/lib/python3.7/site-packages/kocrawl/answerer/take_act.py -time "+time+" -object "+objects+" -do "+do
result2="take_act.py"
#print(result)
#p=subprocess.Popen(["/home/pi/.pyenv/versions/3.7.13/lib/python3.7/site-packages/kocrawl/answerer/take_act.py",time,object,do],stdout=subprocess.PIPE)
os.system(result2)