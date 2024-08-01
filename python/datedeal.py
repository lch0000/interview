from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse
import arrow

now = datetime.now()

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(delta.days, delta.seconds)

stamp = datetime(2011, 1, 3)
print(str(stamp))
print(stamp.strftime('%Y-%m-%d'))

value = '2011-01-03'
print(datetime.strptime(value, '%Y-%m-%d'))

print(parse('2011-01-03'))
print(parse('Jan 31, 1997 10:45 PM'))

#arrow
now = arrow.now()
print(now.year, now.month, now.hour, now.minute, now.second)
print(now.weekday(), now.isocalendar())
