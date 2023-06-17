score = 0

name = input("What is your name? ")

question1 = input("What year did 9/11 happen?\nA:2008\nB:2001\nC:2013\nAnswer: ")
if question1.lower() == "b":
    print("Well done! +1 point")
    score = score + 1
else:
    print("Incorrect!")

question2 = input("Pickels start out as what vegetable?\nA:Cucumber\nB:Tomato\nC:Gurkin\nAnswer: ")
if question2.lower() == "a":
    print("Well done! +1 point")
    score = score + 1
else:
    print("Incorrect!")

question3 = input("What month was Julius Caesar stabbed in?\nA:January\nB:February\nC:March\nAnswer: ")
if question3.lower() == "c":
    print("Well done! +1 point")
    score = score + 1
else:
    print("Incorrect!")

print(f"Thank you for playing my quiz {name}! Your score was {score}")