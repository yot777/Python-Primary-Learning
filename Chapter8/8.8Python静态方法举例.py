import time

class TimeTest():
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    #普通方法
    def showTime(self):
    	print('%s:%s:%s' %(self.hour,self.minute,self.second))

    #静态方法
    @staticmethod
    def showCurrentTime():
        return time.strftime("%H:%M:%S", time.localtime())

t = TimeTest(22, 15, 10)
t.showTime()
print(TimeTest.showCurrentTime())