

day1 = input('')
time1 = input('')
day2 = input('')
time2 = input('')

'''
print('Day = ' + day[3:])
print('Hour = ' + time[:2])
print('Minutes = ' + time[5:7])
print('Seconds = ' + time[10:])


day1 = 'Dia 5'
time1 = '08 : 12 : 23'
day2 = 'Dia 9'
time2 = '06 : 13 : 23'
'''

day1 = int(day1[3:])
day2 = int(day2[3:])

hour1 = int(time1[:2])
hour2 = int(time2[:2])

minutes1 = int(time1[5:7])
minutes2 = int(time2[5:7])

seconds1 = int(time1[10:])
seconds2 = int(time2[10:])

if(seconds2 < seconds1):
    seconds2 = seconds2 + 60
    minutes2 = minutes2 - 1

if(minutes2 < minutes1):
    minutes2 = minutes2 + 60
    hour2 = hour2 - 1

if(hour2 < hour1):
    hour2 = hour2 + 24
    day2 = day2 - 1

day = str(day2 - day1)
hour = str(hour2 - hour1)
minutes = str(minutes2 - minutes1)
seconds = str(seconds2 - seconds1)

print(day + ' dia(s)')
print(hour + ' hora(s)')
print(minutes + ' minuto(s)')
print(seconds + ' segundo(s)')