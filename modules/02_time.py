from datetime import datetime, date, timedelta
import time

# today = date.today()
# # print(f"วันที่ : {today}")
# # print(f"วัน : {today.day} เดือน : {today.month} ปี : {today.year}")

# now = datetime.now()
# #print(now)
# print(f"ชั่วโมง : {now.hour} นาที : {now.minute} วินาที : {now.second}")
# #print(f"วันที่ : {now.day} เดือน : {now.month} ปี : {now

today = date.today()
now = datetime.now()

# จัด Format ว ด ป
formatted_date = now.strftime("%d/%m/%Y")
formatted_time = now.strftime("%H-%M-%S")

# คำนวณวันที่
'''tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(weeks=1) # สัปดาห์หน้า (days=7 ก็ได้)
print(tomorrow)
print(yesterday)
print(next_week)'''

# #สร้างโปรแกรมคำนวณอายุ
# birth_date = input("Enter your birth date (dd/mm/yyyy): ")
# birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
# age = now.year - birth_date.year - ((now.month, now.day) < (birth_date.month, birth_date.day))
# print(f"Your age is: {age} years")

# #สร้างโปรแกรมคำนวณอายุ และแสดงผลลัพธ์เป็นปี เดือน วัน
# birth_date = input("Enter your birth date (dd/mm/yyyy): ")
# birth_date = datetime.strptime(birth_date, "%d/%m/%Y")
# age_years = now.year - birth_date.year
# age_months = now.month - birth_date.month
# age_days = now.day - birth_date.day
# if age_days < 0:
#     age_months -= 1
#     age_days += (birth_date.replace(month=birth_date.month + 1, day=1) - birth_date).days
# if age_months < 0:
#     age_years -= 1
#     age_months += 12
# print(f"Your age is: {age_years} years, {age_months} months, and {age_days} days")

# คำนวณวันที่
tomorow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
next_week = today + timedelta(days=7)
next_mount = today + timedelta(days=30)

def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    return age

day = int(input("Day : "))
month = int(input("Month : "))
year = int(input("Year : "))
birth_day = date(year, month, day)

age = calculate_age(birth_day)
print(age)