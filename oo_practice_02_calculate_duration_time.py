# calculate the duration time ,while start time and end time are given
class Time:
    # def __init__(self,hours,minutes,seconds):
    def __init__(self,*arg):
        self.hours,self.minutes,self.seconds = arg

    def subtract_time(self,end):
        duration_hours = duration_minutes = duration_seconds = 0
        duration_hours = -self.hours + end.hours
        duration_minutes = -self.minutes + end.minutes
        duration_seconds = -self.seconds + end.seconds
        duration_hours += int(duration_minutes/60)
        duration_minutes = duration_minutes%60
        duration_minutes += int(duration_seconds/60)
        if duration_seconds < 0:
            duration_minutes -= 1
        if duration_minutes < 0:
            duration_hours -= 1
        duration_seconds = duration_seconds%60


        dur_hours = dur_minutes = dur_seconds = 0
        dur_seconds = duration_seconds / 60
        dur_minutes = duration_hours * 60 + duration_minutes + dur_seconds
        dur_hours = duration_hours + dur_minutes / 60
        print (duration_hours,':',duration_minutes,':',duration_seconds)
        # round(x,2) --> output 2 digitals after piont, can alse use print('%.2f'%x)
        print (round(dur_hours,2), 'hours', round(dur_minutes,2), 'mins')
        return (duration_hours,duration_minutes,duration_seconds)

if __name__ == '__main__':
    start_time = Time(0,0,0)
    end_time = Time (0,3,40)
    start_time.subtract_time(end_time)

