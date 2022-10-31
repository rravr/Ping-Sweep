import os
import platform
print (  '                   Change Key words "ttl" AND "host" for linux                   ')
print ( "                              +++ PING  SWEEPER +++ " )
print  ("Required IP FORMAT - 0.0.0.0   ")

ip = (input("Enter IP- "))
ip_split = ip.split('.')
list = [l for l in ip_split if l.isdigit()]

octet1 = list[0]
octet2 = list[1]
octet3 = list[2]
octet4 = list[3]
insert  = "."
ip_2 = octet1 + insert + octet2 + insert + octet3  + insert 
 

q= int(input('Please Enter Range + From- '))
p= int(1) + int(input ("Please Enter Range + To- "))
print ("          ") 
print ("                      +++ List 0f 0NLINE IP  +++ ")
print("           ")
for x in range (q,p):
    pc = '-n' if platform.system().lower() == 'windows' else '-c'
    result = os.popen("ping " + pc + " 1 " + ip_2 + str(x) )
    
    for line in result.readlines():
        if "TTL" in line: 
            print("IP ONLINE ---", ip_2 + str(x) )
print ("           ")
print ("                      +++ List Of OFFLINE IP +++ ")
print ("           ")
    
for z in range (q,p):
    pc = '-n' if platform.system().lower() == 'windows' else '-c'
    result = os.popen("ping " + pc + " 1 " + ip_2 + str(z) )
    for line in result.readlines():
        if "host" in line:
            print("IP OFFLINE ---", ip_2 + str(z) )
print ("           ")  
print ("                        +++ SCANNING DONE +++ ")
print ("        ")
# code will work on windows os required host and TTL kewords change for linux or mac"
# addining multithreading can also speed up the scanning proccess.
    