age = input('Are you a cigarette addict older than 75 years old? Yes/No :').title().strip()
chronic = input('Do you have a severe chronic disease? Yes/No :').title().strip()
immuni = input('Is your immune system too weak? Yes/No :').title().strip()
if age == 'No' and chronic == 'No' and immuni == 'No':
    print("You are not in risky group") 
elif age == 'Yes' or chronic == 'Yes' or immuni == 'Yes':
    print("You are in risky group")
else:
      print("Please just enter Yes or No")   
