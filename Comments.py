#asks the user there age and name.

your_name = input("What's you name?")
try:
    your_age=int("What's your age?")
     ValueError:
        print("This is not a whole number")
#will calculate how old the user will be in 5 years time.

age_in_5 = your_age + 5

#tells the user the final print statement

print("Well {}, in five years time you will be {}".format(your_name,age_in_5))
