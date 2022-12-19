from models.droid import Droid
from datetime import date

reg_date = date(1051, 10, 10)
droid_1 = Droid("R2D2", 2, reg_date, "None", 1, 2)
current_date = date.today()
year = current_date.year - 960
current_sw_date = date(year, current_date.month, current_date.day)
droid_1_age = current_sw_date.year - droid_1.registration_date.year

print(current_date)
print(current_sw_date)
print(droid_1_age)



