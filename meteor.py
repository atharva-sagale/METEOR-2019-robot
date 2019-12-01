#This is an updated code of METEOR-2k19
#to run and upload this code you require Upycraft_v1.1 IDE which can be downloaded from
# * https://randomnerdtutorials.com/install-upycraft-ide-windows-pc-instructions/ *
#follow this tutorial to download IDE
# Paste this code into IDE by creating a file of name "main.py"
#Connect the nodeMCU with your PC and UPLOAD the Code into nodeMCU
import os
try:
import usocket as socket
except:
import socket
from machine import Pin, ADC, Timer
import network
from time import sleep
import esp
esp.osdebug(None)
import gc
gc.collect()
ssid = 'Node7'
password = 'trskncoe'
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)
zz=0
tim = Timer(1)
analog=ADC(0)
led=Pin(16,Pin.OUT)
motorRb=Pin(4,Pin.OUT)
motorLb=Pin(12,Pin.OUT)
motorRf=Pin(13,Pin.OUT)
motorLf=Pin(14,Pin.OUT)
switch1=Pin(16,Pin.OUT)
switch2=Pin(5,Pin.OUT)
switch3=Pin(15,Pin.OUT)
motorRb.value(0)
motorLb.value(0)
switch1.value(1)
switch2.value(0)
switch3.value(0)
while station.isconnected() == False:
pass
print(station.ifconfig())
def moto(rf,lf,rb,lb):
motorRb.value(rf)
motorLb.value(lf)
motorRf.value(rb)
motorLf.value(lb)
def blink(t):
switch3.value(not switch3.value())
return
def line_tracing():
ctr = 0
last = 0
moto(0,0,0,0)
while True:
sensor0=Pin(5,Pin.IN)#mid
sensor2=Pin(15,Pin.IN)#right
sensor1=Pin(16,Pin.IN)#left
if sensor0.value()==0 and sensor1.value()==1 and sensor2.value()==0:
#move motor forward
moto(1,1,0,0)
elif (sensor0.value()==0 and sensor1.value()==0 and sensor2.value()==1) or
(sensor0.value()==0 and sensor1.value()==1 and sensor2.value()==1):
#move left
last = 0
moto(1,0,0,0)
elif (sensor0.value()==1 and sensor1.value()==0 and sensor2.value()==0) or
(sensor0.value()==1 and sensor1.value()==1 and sensor2.value()==0):
#move right
last = 1
moto(0,1,0,0)
else:
#stop all motors
ctr+=1
if last == 0:
moto(1,0,0,0)
elif last == 1:
moto(0,1,0,0)
else:
moto(0, 0, 0, 0)
#print(ctr)
sleep(0.1)
if ctr >= 50:
moto(0, 0, 0, 0)
break
def func1():
key1 = '?time='#6
key2 = 'HTTP'
if key1 in request:
a = request.find(key1)+6
z = request.find(key2)
sec = request[a:z]
try:
abc = int(sec)
except ValueError:
abc=int(sec)
else:
sec=0
try:
abc = int(sec)
except ValueError:
abc=int(sec)
return abc
def home_auto():
a = """<html>
<head>
<title>METEOR WEB MODE-2k19</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css?family=Orbitron&display=swap"
rel="stylesheet">
<style>
*{
margin: 0px;
padding: 0px;
}
body{
background-color:black;
}
#name{
width: max-content;
margin: 20px auto 20px auto;
}
#but1{
width: max-content;
margin: 10px auto 10px auto;
}
#but1 input{
font-family: 'Orbitron', sans-serif;
font-size: 20px;
color: aliceblue;
background-image:linear-gradient(140deg,#22bb99 30%,#2d57a3 70%);
border: 2px solid black;
width: 150px;
height: 150px;
border-radius: 50%;
}
#name h1{
font-family: 'Orbitron', sans-serif;
color: aliceblue;
text-align: center;
font-size:50px;
}
</style>
</head>
<body>
<div id="main">
<div id="name">
<h1>METEOR 2K19</h1>
</div>
<div id="but1">
<a href='/SWITCH1'> <input type="button" value="SWITCH 1"></input></a>
</div>
<div id="but1">
<a href='/SWITCH2'><input type="button" value="SWITCH 2"></input></a>
</div>
<div id="but1">
<a href='/SWITCH3'><input type="button" value="SWITCH 3"></input></a>
</div>
</div>
</body>
</html>
"""
return a
def robot():
ro = """<html>
<head>
<title>METEOR WEB MODE-2k19</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css?family=Orbitron&display=swap"
rel="stylesheet">
<style>
*{
margin: 0px;
padding: 0px;
}
body{
background-color:black;
}
#name{
width: max-content;
margin: 20px auto 20px auto;
}
#but1{
width: max-content;
margin: 20px auto 10px auto;
}
#but1 input{
font-family: 'Orbitron', sans-serif;
font-size: 20px;
color: aliceblue;
background-color:#2d57a3;
/*background-image:linear-gradient(140deg,#22bb99 30%,#2d57a3 70%);*/
border: 2px solid black;
width: 140px;
height: 140px;
border-radius: 50%;
}
#name h1{
font-family: 'Orbitron', sans-serif;
color: aliceblue;
text-align: center;
font-size:50px;
}
</style>
</head>
<body>
<div id="main">
<div id="name">
<h1>METEOR 2K19</h1>
</div>
<div id="but1">
<a href='/st'> <input type="button" value="FORWARD"></input></a>
</div>
<div id="but1">
<a href='/LEFT'><input type="button" value="LEFT"></input></a>
<a href='/STO'><input type="button" value="STOP"></input></a>
<a href='/RIGHT'><input type="button" value="RIGHT"></input></a>
</div>
<div id="but1">
<a href='/BACK'><input type="button" value="back"></input></a>
</div>
</div>
</body>
</html>
"""
return ro
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
moto(0,0,0,0)
while True:
conn, addr = s.accept()
request = conn.recv(1024)
request = str(request)
#web mode
st = request.find('/st')
left = request.find('/LEFT')
right = request.find('/RIGHT')
back = request.find('/BACK')
stop = request.find('/STO')
robo= request.find('/ROBOT')
home= request.find('/HOME')
switch_port_1= request.find('/SWITCH1')
switch_port_2= request.find('/SWITCH2')
switch_port_3= request.find('/SWITCH3')
hello= request.find('/genericArgs?')
zz = func1()
#app
ip_add= request.find('/ip')
battery_app=request.find('/battery')
forward_mannual_app=request.find('/forward')
right_mannual_app=request.find('/turnright')
left_mannual_app=request.find('/turnleft')
back_mannual_app=request.find('/backward')
sto_app=request.find('/stop')
ha_switch_1 = request.find('/switch1')
ha_switch_2 = request.find('/switch2')
ha_switch_3 = request.find('/switch3')
lt= request.find('/line')
#starting of if-else ladder
if ip_add==6:
response='connected'
elif battery_app==6:
#print ("Battery check")
if analog.read()<50:
response='Not Connected to Robot'#change
elif analog.read() > 480:
response='Battery is charged'
else:
response='Battery Low'
#app
elif forward_mannual_app==6:
response ='Forward'
moto(1,1,0,0)
elif right_mannual_app==6:
response ='Turnright'
moto(1,0,0,0)
elif left_mannual_app==6:
response ='Turnleft'
moto(0,1,0,0)
elif back_mannual_app==6:
response ='Backward'
moto(0,0,1,1)
elif sto_app==6:
response ='Stop'
moto(0,0,0,0)
elif ha_switch_1==6:
if switch1.value()==0:
response = 'Switch 1 is ON'
switch1.value(1)
else:
response = 'Switch 1 is OFF'
switch1.value(0)
elif ha_switch_2==6:
if switch2.value()==0:
response = 'Switch 2 is ON'
switch2.value(1)
else:
response = 'Switch 2 is OFF'
switch2.value(0)
elif ha_switch_3==6:
if switch3.value()==0:
response = 'Switch 3 is ON'
switch3.value(1)
else:
response = 'Switch 3 is OFF'
switch3.value(0)
elif lt==6:
response ='Linetracing'
line_tracing()
print("out")
#web
elif robo==6:
response = robot()
motorRb.value(0)
motorLb.value(0)
motorRf.value(0)
motorLf.value(0)
elif stop == 6 or robo==6:
response = robot()
motorRb.value(0)
motorLb.value(0)
motorRf.value(0)
motorLf.value(0)
elif st == 6 or robo==6:
response = robot()
moto(1,1,0,0)
elif right == 6 or robo==6:
response = robot()
moto(1,0,0,0)
elif left == 6 or robo==6:
response = robot()
moto(0,1,0,0)
elif back == 6 or robo==6:
response = robot()
moto(0,0,1,1)
elif switch_port_1==6 or home==6:
response = home_auto()
if switch1.value()==0:
switch1.value(1)
else:
switch1.value(0)
elif switch_port_2==6 or home==6:
response = home_auto()
if switch2.value()==0:
switch2.value(1)
else:
switch2.value(0)
elif switch_port_3==6 or home==6:
response = home_auto()
if switch3.value()==0:
switch3.value(1)
else:
switch3.value(0)
elif hello==6:
response = 'Switch 3 is ON'
print(zz)
if switch3.value()==1:
switch3.value(1)
else:
switch3.value(1)
tim.init(period=zz*1000,mode=Timer.ONE_SHOT, callback=blink)#calling timer for controlling
Timer Switch
conn.send('HTTP/1.1 200 OK\n')
conn.send('Content-Type: text/html\n')
conn.send('Connection: close\n\n')
conn.sendall(response)
conn.close()