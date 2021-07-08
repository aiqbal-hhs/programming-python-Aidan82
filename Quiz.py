# this is the variables.
points = 0
q1 = "2011"
q2 = "Markus Persson"
q3 = "1.4.2"
q4 = "42"
q5 = "Netherite"
q6 = "The Bee Update"
q7 = "Microsoft"
q8 = "1.16"

# Start of Quiz
print("Welcome to the Minecraft Quiz!")
name = input("Please insert a name! Name:")

name_1 = name.title()

print("Hello, {}! Do your best in my quiz! :)".format(name_1))

print("--")

#Question 1

print("Q1: When was Minecraft released? A. 2009, b. 2011..")


question_1 = input("Answer:")


if question_1 == q1: 

    print("Corret!")

    points += 1

else:
    print("Wrong! No points")

print("Points:{}".format(points))


print("--")

# Question 2
print("Q2: Who was the original creator of minecraft. a. MarkusPersson, b. JensBergensten, c. Microsoft")

question_2 = input("Answer:")

question_2_2 = question_2.title()

if question_2_2 == q2:
    print("Correct!")
    points += 1
else:

    print("Wrong! No points")

print("Points:{}".format(points))

print("--")

# Question 3
print("What update did they add the wither boss? a. 1.5, b. 1.4.2, c. 1.2, d. 1")
question_3 = input("Awnser:")

if q3 == question_3:
    print("Correct!")
    points += 1
else:
    print("Wrong! No points")

print("Points:{}".format(points))


print("--")

# Question 4
print("Q4: How old is the original Creater of Minecraft? a. 20, b. 60, c. 42")
question_4 = input("Answer:")

if question_4 == q4:
    print("Correct!")
    points += 1
else:
    print("Wrong! No points!")

print("Points:{}".format(points))


print("--")

# Question 5
print("Q5: What is the new best ore added in the nether update last year? a. Netherite b. Copper, c. Enderite")
question_5 = input("Awnser:")

question_5_5 = question_5.title()

if question_5_5 == q5:
    print("Correct!")
    points += 1
else:
    print("Wrong! No points!")

print("Points:{}".format(points))


print("--")

# Question 6
print("Q6: What update added Bees to Minecraft? a. Caves and Cliffs prt 1 b. The Village and Pillage update c. The Bee Update")
question_6 = input("Answer:")

question_6_6 = question_6.title()

if question_6_6 == q6:
    print("Correct!")
    points += 1
else:
    print("Wrong! No points!")

print("Points:{}".format(points))


print("--")

# Question 7
print("Q7: Who bought Minecraft? a. EA, b. Microsoft, c. Capcom")
question_7 = input("Answer:")

question_7_7 = question_7.title()

if question_7_7 == q7:
    print("Correct!")
    points += 1
else:
    print("Wrong! No Points!")

print("Points:{}".format(points))


print("--")

# Question 8
print("Q8: What recent update updated the nether? a. 1.16, b.1.15.2")
question_8 = input("Answer:")

if question_8 == q8:
    print("Correct!")
    points += 1
else:
    print("Wrong! No points!")


print("--")

#End of the Quiz
print("You finished the Quiz! Here's your results!")

print("Name:{}".format(name))
print("Points:{}".format(points))
