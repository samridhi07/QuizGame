print("Welcome to the quiz game")

score = 0 

playing = input("Are you playing? ")

if playing.lower() != "yes":
    quit()

print("Let's start the game")


answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer. Try again!")


answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer. Try again!")


answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer. Try again!")


answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply':
    print("Correct Answer")
    score += 1
else:
    print("Incorrect Answer. Try again!")


print("You got " + str(score) + " questions correct!")