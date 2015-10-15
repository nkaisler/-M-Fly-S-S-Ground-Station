import serial #Import Serial Library
import numpy #Import numpy
import csv #CSV Library
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

teamid= []
missiontime= []
altitude= []
outtemp= []
intemp= []
voltage= []
fswstate= []
accelx= []
accely= []
accelz= []

arduinoData = serial.Serial('com6',9600)
plt.ion()
cnt=0

def makeFig():
    plt.figure(1)
    plt.title('Altitude')
    plt.grid(True)
    plt.ylabel('Altitude (m)')
    plt.plot(altitude, 'r-')

    plt.figure(2)
    plt.title('Exterior Temperature')
    plt.grid(True)
    plt.ylabel('Temperature (C)')
    plt.plot(outtemp, 'r-')

    plt.figure(3)
    plt.title('Interior Temperature')
    plt.grid(True)
    plt.ylabel('Temperature (C)')
    plt.plot(intemp, 'r-')

    plt.figure(4)
    plt.title('Battery Voltage')
    plt.grid(True)
    plt.ylabel('Voltage (V)')
    plt.plot(voltage, 'r-')


    plt.figure(5)
    plt.title('Flight Software State')
    plt.grid(True)
    plt.ylabel('State #')
    plt.plot(fswstate, 'r-')


# Main Ground Station Code


#Header for Telemetry file
with open('CANSAT2015_TLM_5761.csv', 'ab') as csvfile:
            FileWriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            FileWriter.writerows([['TEAMID', 'Mission Time', 'Altitude' , 'Outside Temperature' , 'Inside Temperature' , 'Battery Voltage' , 'FSW State' , 'Acceleration x' , 'Acceleration y', 'Acceleration z']])

# First Read
while (arduinoData.inWaiting()==0):
    pass
arduinoString = arduinoData.readline()
dataArray = arduinoString.split(',')

tid= float( dataArray[0])
FirstTime= float( dataArray[1])
alt= float( dataArray[2])
otemp= float( dataArray[3])
itemp= float( dataArray[4])
volt= float( dataArray[5])
state= float( dataArray[6])
x= float( dataArray[7])
y= float( dataArray[8])
z= float( dataArray[9])
teamid.append(tid)
missiontime.append(0)
altitude.append(alt)
outtemp.append(otemp)
intemp.append(itemp)
voltage.append(volt)
fswstate.append(state)
accelx.append(x)
accely.append(y)
accelz.append(z)
drawnow(makeFig)


with open('CANSAT2015_TLM_5761.csv', 'ab') as csvfile:
        FileWriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        FileWriter.writerows([[tid, '0', alt, otemp, itemp, volt, state, x, y, z]])
plt.pause(.000001)
cnt=cnt+1


#Iteration

while True:

    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split(',')

    tid= float( dataArray[0])
    time= float( dataArray[1]) - FirstTime
    alt= float( dataArray[2])
    otemp= float( dataArray[3])
    itemp= float( dataArray[4])
    volt= float( dataArray[5])
    state= float( dataArray[6])
    x= float( dataArray[7])
    y= float( dataArray[8])
    z= float( dataArray[9])
    teamid.append(tid)
    missiontime.append(time)
    altitude.append(alt)
    outtemp.append(otemp)
    intemp.append(itemp)
    voltage.append(volt)
    fswstate.append(state)
    accelx.append(x)
    accely.append(y)
    accelz.append(z)
    drawnow(makeFig)


    with open('CANSAT2015_TLM_5761.csv', 'ab') as csvfile:
            FileWriter = csv.writer(csvfile, delimiter=',',quoting=csv.QUOTE_MINIMAL)
            FileWriter.writerows([[tid, time, alt, otemp, itemp, volt, state, x, y, z]])


    plt.pause(.000001)
    cnt=cnt+1

