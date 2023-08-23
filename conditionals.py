# i = 8
# if(i % 2 == 0):
#     print ("Even Number")
# else:
#     print ("Odd Number")

from datetime import datetime

raw_year = datetime.now()
fmt_year = int(raw_year.strftime("%Y"))

    
# def evens(nums):
#     sum = 0
#     for num in nums:
#         if num % 2 == 0:
#             sum += num
#         
#     return sum
# 
# print(evens([1,2,3,4,5,6,7,8,9,10]))
# 
# 
# def get_age():
#     age = int(input("What is your age? "))
#     
#     old = "old" if age > 30 else "young"
#     
#     return f"You are {old}"
# 
# print(get_age())
# 
# 
# def calc_age(year):
#     age = fmt_year - year
#     return age
# 
# print(calc_age(2001))
# 

def leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    else:
        if year % 4 == 0:
            if year % 100 != 0:
                return "Leap Year"
            return "Not Leap Year"
        return "Not Leap Year"
    
print(leap_year(2012))
    
    
    
