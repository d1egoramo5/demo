# this is a script to return the number of days lived

from datetime import datetime
from datetime import date

# today's date
today = datetime.date.today()
print("Today's date is: ", today)

# date of birth
dob = date(1997, 1, 23)

# calculation
delta = today - dob
print("You have lived ", delta.days, "days!")
