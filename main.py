from calendar import c  
from genericpath import exists
from operator import truediv
from pickle import FALSE
from socket import *
import string
import time 
import array

class ip_scanner():
    
    
    def __init__(self):
        #defualt 
        self.callBuffer = list(([0,('init','init', 'init','localhost',time.time())],[1,('init','init','init','localhost',time.time())]))
        
    def preBuffer(self, ip):
        temp = len(self.callBuffer), '', '', '', ip, time.time(),
        for i in self.callBuffer:
            if i[0] == temp[0] - 1:
                self.callBuffer.append([temp[0],(temp[1],temp[2],temp[3],temp[4],temp[5])])
                break
        return True
    
    def getRange(self, input1, input2):
        self.Range = str(int(input1.split('.')[0]) - int(input2.split('.')[0]))+ \
            "."+str(int(input1.split('.')[1]) - int(input2.split('.')[1]))+ \
            "."+str(int(input1.split('.')[2]) - int(input2.split('.')[2]))+ \
            "."+str(int(input1.split('.')[3]) - int(input2.split('.')[3]))
        if int(self.Range.split('.')[3]) > 0:
            for i in range(int(self.Range.split('.')[3])):
                if i<=1:
                    self.preBuffer(str(input2.split('.')[0])+
                                   '.'+str(input2.split('.')[1])+
                                   '.'+str(input2.split('.')[2])+
                                   '.'+str((i)+int(input2.split('.')[3])))               
                if i>=1:
                    self.preBuffer(str(input2.split('.')[0])+
                                   '.'+str(input2.split('.')[1])+
                                   '.'+str(input2.split('.')[2])+
                                   '.'+str((i+1)+int(input2.split('.')[3])))               
        if(int(self.Range.split('.')[3]) == 0):
            self.preBuffer(input1)       
        return int(self.Range.split('.')[3])
    
    def getAdress(self, input):
        if input.find('-') != -1:   
          IPs = self.getRange(input.split('-')[1], input.split('-')[0])
          print('Range of  adresses('+str(IPs)+') are save in buffer for scan!')
          self.callBuffer.pop(0)
          self.callBuffer.pop(0)
          return True
        else:
          self.getRange(input, input)
          print('Adress('+input+') saved in buffer for scan!')
          self.callBuffer.pop(0)
          self.callBuffer.pop(0)
          return False
      
    #Help method  
    def generateSocket(self):
        return socket(AF_INET, SOCK_STREAM)
    
    def core(self,operation, value):
        for i in self.callBuffer:
            self.core_functions(operation,value,i[1][3])
            
            
    def core_functions(self,operation,value,target):
        print("IP: "+target)
        if (operation == "port"):
            localSocket = self.generateSocket()   
            if (localSocket.connect_ex((target,int(value))) == 0):
                print('Port %d : OPEN' % (int(value),))
            else:
                print('Port %d : CLOSED' % (int(value),))
            localSocket.close()
            return localSocket

if __name__ == '__main__':
    instance = ip_scanner() 
    adress = instance.getAdress("10.7.31.251 - 10.7.31.255")
    instance.core("port", 80)
    