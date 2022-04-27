def add_time(start, duration, day = None):
  #get start hour, min, period
  start_time,period = start.split()
  start_hour,start_min = start_time.split(':')

  #get duration hour,mins
  dur_hour,dur_min = duration.split(':')

  #lets change time to 24hr clock
  if period == "PM":
    start_hour = int(start_hour) + 12

  #add Time
  end_hour = int(start_hour) + int(dur_hour)
  end_min = int(start_min) + int(dur_min)

  if end_min>=60:
    hours_added = end_min//60
    end_min -= hours_added * 60
    end_hour += hours_added

  #days passed
  days_passed = 0
  if end_hour > 24:
    days_passed = end_hour//24
    end_hour -= days_passed * 24

  #return to 12 hr clock

  if end_hour > 0 and end_hour < 12:
   end_period = 'AM'
  elif end_hour == 12:
    end_period = 'PM'
  elif end_hour > 12:
    end_period = 'PM'
    end_hour -= 12
  else: #end_hour == 0
    end_period = 'AM'
    end_hour +=12

  #days added
  if days_passed > 0:
    if days_passed == 1:
      days_later = ' (next day)'
    else:
      days_later = f' ({days_passed} days later)'
  else:
    days_later = ""

  #day of the week

  weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

  if day:
    weeks_added = days_passed//7
    i = weekdays.index(day.lower().capitalize()) + (days_passed - 7*weeks_added)
    if i > 6:
      i -= 7
      
    end_day = ", " + weekdays[i]
  else:
    end_day = ''

  new_time = str(end_hour)+':'+ str(end_min).zfill(2)+ ' '+ end_period+ end_day +days_later

  return new_time