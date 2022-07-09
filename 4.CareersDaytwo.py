
#list Holding Career options
career_options = ["Technology", "Medicine", "Engineering", "Law"]

#list holding career advices
career_advices = ["Find a job you enjoy", "Say yes to the things that scare you", "Set Realistics goals", "User your strengths", "Be willing to sacrifice some things to build the career you want"]

#list holding questions
career_questions = ["Do you like Technology and learning new exciting things?", "Are you more interested in saving people's lives?", "Are you interested in building exciting stuff e.g hoses or cars?","Do you like representing and defending the oppressed?"]

#Printing the career options
print("Below are the career options")
for career in career_options:
    print(career)

#Printing Career Advices
print("\nCareer Advices to take note before choosing......")
for advice in career_advices:
    print(advice)

#Determining which Career best fits user
print("\nChoose 'yes' or 'no' to determine career path to choose")
x = 0
for question in career_questions:
    option = input(career_questions[x] + ": ")
    if option == "yes":
        career_track = (career_options[x])
        break
    elif option == "no":
        pass
    else:
        print("Invalid Choice. Please choose 'yes' or 'no' ")
    x = x+1

print("You should pursue " + career_track)

