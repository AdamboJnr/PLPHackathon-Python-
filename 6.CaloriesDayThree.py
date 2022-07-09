#Get number of grams of fats

fats_grams = int(input("Enter Number of fats in grams: "))

#Get number of grams of cabohydrates
cabohydrates_grams = int(input("Enter Number of cabohydrates in grams: "))

#Calculating number of Calories in fats
fats_calories = fats_grams * 9

#Calculating number of calories in Carbs
cabohydrates_calories = cabohydrates_grams * 4

#print the output
print("Calories from fats are: " + str(fats_calories) + " grams")
print("Calories from cabohydrates are: " + str(cabohydrates_calories) + " grams")