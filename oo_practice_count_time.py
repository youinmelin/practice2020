# compute the end time of an opera,while start time and duration time are given
class Time:
    def __init__(self,hours:int,minutes:int,seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def add_time(self,duration):
        end_hours = end_minutes = end_seconds = 0
        end_hours = self.hours + duration.hours
        end_minutes = self.minutes + duration.minutes
        end_seconds = self.seconds + duration.seconds
        end_hours += int(end_minutes/60)
        end_minutes = end_minutes%60
        end_minutes += int(end_seconds/60)
        end_seconds = end_seconds%60
        print (end_hours,':',end_minutes,':',end_seconds)

start_time = Time(10,30,30)
duration_time = Time (2,45,50)
start_time.add_time(duration_time)

