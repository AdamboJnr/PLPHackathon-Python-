#Get Number of books purchased this month
no_of_books = int(input("Enter the number of books purchased this month: "))

#conditions to determine number of points awarded
if no_of_books == 0:
    points_awarded = 0
    print("Number of points awarded: " + str(points_awarded))
elif no_of_books == 1:
    points_awarded = 6
    print("Number of points awarded: " + str(points_awarded))
elif no_of_books == 2:
    points_awarded = 16
    print("Number of points awarded: " + str(points_awarded))
elif no_of_books == 3:
    points_awarded = 32
    print("Number of points awarded: " + str(points_awarded))
elif no_of_books >= 4:
    points_awarded = 60
    print("Number of points awarded: " + str(points_awarded))
#Check for a negative number
else:
    print("Please input positive integers ")
