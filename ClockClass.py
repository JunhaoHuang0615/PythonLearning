import time
class Mytimer:
    # Constructer
    def __init__(self):
        self.prompt = "Please start"
        self.startTime = 0
        self.stopTime = 0
        self.isStarting = False
        self.lasted = []
        self.unit = ['年','月','日','时','分','秒']

    # time start method
    def startTimer(self):
        if(self.isStarting == False):
            self.startTime = time.localtime()
            self.isStarting = True
            print('Start timing')
        else:
            print("stop the timer first")

    # time stop method
    def stopTimer(self):
        if (self.isStarting == True) :
            self.stopTime = time.localtime()
            self.isStarting = False
            self._calc()
            print('Stop the timer')
        else:
            print('the timer has been stopped')
    
    # calculate the time consuming
    def _calc(self):
        self.prompt = '总共计时了'
        for index in range(6): #不能用len(self.startTime)，因为这个长度包含了其他的东西
            self.lasted.append(self.stopTime[index] - self.startTime[index])
            if(self.lasted[index]):
                self.prompt += str( self.lasted[index]) + self.unit[index]
        print(self.prompt)
        self.prompt = '' #重置这个语句，时间不用重置
    
    def __str__(self):
        return self.prompt
    
    __repr__ = __str__ 

    #重写一个__add__方法，这样子两个计时器相加就可以得到总合
    def __add__(self,value):
        prompt = 'total time is '
        total_result = []
        for index in range(len(self.lasted)):
            total_result.append(self.lasted[index]+ value.lasted[index])
            if total_result[index] != 0:
                prompt += (str(total_result[index]) + self.unit[index])
        
        return prompt

t1 = Mytimer()

t1.startTimer()
time.sleep(5)
t1.stopTimer()

t2 = Mytimer()
t2.startTimer()
time.sleep(2)
t2.stopTimer()

print(t1+t2)

