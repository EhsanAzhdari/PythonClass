class Time:
    def __init__(self, hour, minute, second):
        # Class properties
        self.hour = hour
        self.minute = minute
        self.second = second
        self.fix_Time()
        
    # Class methods
    def show(self):
        print(f"{self.hour}:{self.minute}:{self.second}")
    
    def sum_Time(self, other):
        hour = self.hour + other.hour
        minute = self.minute + other.minute
        second = self.second + other.second
        result = Time(hour, minute, second)
        return result
        
    def sub_Time(self, other):
        hour = self.hour - other.hour
        minute = self.minute - other.minute
        second = self.second - other.second
        result = Time(hour, minute, second)
        return result
    
    def convert_SecondtoTime(self):
        hour = self // 3600
        minute = (self % 3600) // 60
        second = (self % 3600) % 60
        result = Time(hour, minute, second)
        return result
    
    def convert_TimetoSecond(self):
        Total_Seconds = self.second + self.minute*60 + self.hour*60*60
        return Total_Seconds
    
    def convert_GMTtoTehran(self):
        hour = self.hour + 3
        minute = self.minute + 30
        result = Time(hour, minute, self.second)
        return result
    
    def fix_Time(self):
        if self.second >= 60:
            self.second -= 60
            self.minute +=1
            
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
            
        if self.second < 0:
            self.second += 60
            self.minute -= 1
            
        if self.minute < 0:
            self.minute += 60
            self.hour -=1