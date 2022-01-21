from calendar import c
from genericpath import exists
from operator import truediv
from pickle import FALSE
from socket import *
import string
import time 
import array

class ip_scanner():
    
    
    def __init__(self, ip = string):
        self.ip = ip
        #defualt 
        self.callBuffer = list(([0,('init','init', 'init','localhost',time.time())],[1,('init','init','init','localhost',time.time())]))
        
    def preBuffer(self, ip):
        # id, "start scan time", "stop scan time", "differents scan time", "IP", "Add time"
        temp = len(self.callBuffer), '', '', '', ip, time.time(),
        for i in self.callBuffer:
            if i[0] == temp[0] - 1:
                self.callBuffer.append([temp[0],(temp[1],temp[2],temp[3],temp[4],temp[5])])
                break
        return True
    
    def getRange(self, input1, input2):
        self.Range = str(int(input1.split('.')[0]) - int(input2.split('.')[0]))+"."+str(int(input1.split('.')[1]) - int(input2.split('.')[1]))+"."+str(int(input1.split('.')[2]) - int(input2.split('.')[2]))+"."+str(int(input1.split('.')[3]) - int(input2.split('.')[3]))
        if int(self.Range.split('.')[3]) > 0:
            for i in range(int(self.Range.split('.')[3])):
                if i<=1:
                    self.preBuffer(str(input2.split('.')[0])+'.'+str(input2.split('.')[1])+'.'+str(input2.split('.')[2])+'.'+str((i)+int(input2.split('.')[3])))               
                if i>=1:
                    self.preBuffer(str(input2.split('.')[0])+'.'+str(input2.split('.')[1])+'.'+str(input2.split('.')[2])+'.'+str((i+1)+int(input2.split('.')[3])))               
        if(int(self.Range.split('.')[3]) == 0):
            self.preBuffer(input1)       
            print(input2)             
        return int(self.Range.split('.')[3])
    
    def getAdress(self, input):
        if input.find('-') != -1:   
          IPs = self.getRange(input.split('-')[1], input.split('-')[0])
          print('Range of ip adresses('+str(IPs)+') are save in buffer for scan!')
          return True
        else:
          self.getRange(input, input)
          print('Adress('+input+') saved in buffer for scan!')
          return False
    
  

        
if __name__ == '__main__':
    instance = ip_scanner() 
    adress = instance.getAdress("152.168.0.199 - 152.168.0.255")
    print(instance.callBuffer)
    
   
# if __name__ == '__main__':
#     target = input('IP: ')
#     target_ip = gethostbyname(target)
#     print('Scanning IP adress', target_ip)
    
#     for i in range(50,500):
#         s = socket(AF_INET, SOCK_STREAM)
#         conn = s.connect_ex((target_ip, i))
#         if(conn == 0):
#             print('Port %d: OPEN' % (i,))
#         s.close()
# print('Time taken:', time.time() - init_time)




    