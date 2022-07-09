import datetime
#Get today's date
date = datetime.datetime.now()

#Get day in Short e.g "Sat"
day=date.strftime("%a")

#Determine the day to check the fare
if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thu" or day == "Fri":
    fare = 100
elif day == "Sat":
    fare = 60
elif day == "Sun":
    fare = 80
else:
    print("No such day")

print("Date: " + str(date.strftime("%x")))
print("Day: " + str(day))
print("Fare: " + str(fare))