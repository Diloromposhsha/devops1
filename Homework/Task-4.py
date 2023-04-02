minutes = 1234567

# by dividing minutes to 60 we are getting hours
# by dividing those hours to 24 we are getting days
# by dividing those days to 365 we are getting years
# by using operator "//" we are getting only whole number
years = minutes // 60 // 24 // 365

days = int((minutes / 60 / 24 / 365 - years) * 365)

print(minutes,"minutes is approximately",years,"years",days,"days")
