import serial, sys
import re

strPort = sys.argv[2]   # serial port

ser=serial.Serial(strPort, 115200)

print("connected to: " + ser.portstr)
count=1

file=sys.argv[1]  # file name
regex = re.compile('\d+')
f=open(file,"w+")
while True:
  line = ser.readline()
  match = regex.findall(line)
  f1=match[4]+"."+match[5]+", "+match[6]+"."+match[7]+", "+match[8]+"."+match[9]+", "+match[10]+"."+match[11]+", "+match[12]+"."+match[13]+", "+match[14]+"."+match[15]+", "+match[16]+"."+match[17]+", "+match[18]+"."+match[19]+", "+match[20]+"."+match[21]+", "+match[22]+"."+match[23]
  print(match[1]+" "+match[2]+" "+match[3]+": "+match[4]+"."+match[5])
  f.write(f1+"\n")
ser.flush()
ser.close()
f.close()
