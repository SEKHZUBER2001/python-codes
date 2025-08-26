def even_or_odd(number):
    if number%2==0:
        return True
    else:
        return False    
print(even_or_odd(20))
print(even_or_odd(101))

def task_reminder(time_string):
    if time_string == "11:00":
        task="Run over-night backup"
    elif time_string=="5:00":
        task="run TPS report"
    elif time_string=="8:00":
        task="log off"
    else:
        task="support to IT staffs"
    return task
print(task_reminder("12:00"))
        