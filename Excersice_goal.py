import datetime as d

print("Enter your goal and timeline seperated by colon : \n")

goal_and_date =input().split(':')
print(goal_and_date)
print(type(goal_and_date))

current_Date = d.datetime.today()
print(current_Date)
goal_date = d.datetime.strptime(goal_and_date[1], "%d.%m.%Y")
print(goal_date)
print(f"Total time remaining for to accomplish goal : {goal_and_date[0]} is {(goal_date-current_Date).days}")