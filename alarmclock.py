

class AlarmClock:
    def __init__(self, alarm_time, time):
        self.alarm_time = alarm_time
        self.time = time
        self.on = False
        


    def turn_off(self):
        self.on = False
    def turn_on(self):
        self.on = True 

    def set_time(self):
        self.time = input('What time is it')
        print(f'current time is {self.time}')
        



































