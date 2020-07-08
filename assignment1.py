name = input("What is your name?:").title().strip()

if name == "Joseph":
    message1 = "Hello, {name1}! The password is :W@12".format(name1 = name)
else:
    message2 = "Hello, {name1}! See you later.".format(name1 = name)
    print(message2)

