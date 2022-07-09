import math

#Ask Square feet from the user
squarefeet = int(input("Input The Square Feet of wall to be painted: "))

#Ask the price of paint per gallon
price_of_paint = int(input("Input the price of paint per gallon: "))

#Calculating the number of gallons of paint required
paint_gallons = math.ceil(squarefeet/115)

#Calculating hours of labour required
required_hours = math.ceil(squarefeet/(115/8))

#Calculating the cost of the paint
cost_of_paint = paint_gallons * price_of_paint

#Calculating labour charges
labour_charges = float(required_hours * 20.00)

#Calculating total cost of the paint job
total_cost = labour_charges + cost_of_paint

#printing the requirements
print("The number of gallons of paint required: " + str(paint_gallons))
print("The hours of labour required: " + str(required_hours))
print("The cost of the paint: " + str(cost_of_paint))
print("The labour charges: " + str(labour_charges))
print("The total cost of the paint job: " + str(total_cost))