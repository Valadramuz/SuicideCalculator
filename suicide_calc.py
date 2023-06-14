age= input("State your age ")
target= input("State the age when you want to die ")

age_int=int(age)
target_int=int(target) 

y= target_int - age_int
d= y * 365
w= y * 52
m= y * 12

print(f"You have {d} days, {w} weeks, and {m} months left.")