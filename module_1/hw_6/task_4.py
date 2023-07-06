import calendar

days_of_week = calendar.weekheader(7).split()
print({idx + 1: day for idx, day in enumerate(days_of_week)})
print({day: idx + 1 for idx, day in enumerate(days_of_week)})
