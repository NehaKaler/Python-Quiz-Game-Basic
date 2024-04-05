print("Welcome to the quiz")

playing = input("Do you want play? ")

if playing.lower() != "yes":
    quit()

print("Wishing you all the best ")
score = 0

answer = input("What is the capital of India")
if answer.lower() == "new delhi":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("What is the square of 2")
if answer == "4":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("Is whale a mammal or a reptile?")
if answer.lower() == "mammal":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

answer = input("Which world wonder is in India?")
if answer.lower() == "taj mahal":
    print('Correct!')
    score += 1
else:
    print('Incorrect')

print('Your score is : ' + str(score))
print('i.e. ' + str((score/4)*100) + '%')