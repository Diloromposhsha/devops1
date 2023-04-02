# A DevOps engineer needs to monitor the remaining time for a 
# long-running task on a server. They have the total time the task
# takes in hours, minutes, and seconds, and they know the time that
# has already passed. They want to calculate the remaining time for
# the task to complete.

# Step 1: Define the problem inputs.

# Total time for the task (hours, minutes, seconds)
# Time passed (hours, minutes, seconds)
total_hours = 5
total_minutes = 25
total_seconds = 15

passed_hours = 2
passed_minutes = 45
passed_seconds = 30

#Hint -> it's easier to work with a single unit of time
# 3600 is seconds in an hour
total_time_in_sec = total_hours * 3600 +total_minutes * 60 +total_seconds;

passed_time_in_sec =  passed_hours * 3600 +passed_minutes * 60 +passed_seconds;

#This will give us the remaining time in seconds.
remaining_total_seconds = total_time_in_sec - passed_time_in_sec

# Our goal is to convert remaininig seconds in minutes hours and sec

# How many hours we have in the remaining_total_seconds

remaining_hours = remaining_total_seconds // 3600
remaining_minutes = remaining_total_seconds % 3600//60
remaining_seconds = remaining_total_seconds % 60
print(f"total_time_in_sec - {total_time_in_sec}")
print(f"passed_time_in_sec - {passed_time_in_sec}")
print(f"remaining_total_seconds - {remaining_total_seconds}")
print(f"remaining_hours - {remaining_hours}")
print(f"remaining_minutes - {remaining_minutes}")
print(f"remaining_seconds - {remaining_seconds}")
