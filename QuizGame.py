#Quiz Game

questions = ("1. Which famous play features a character named Romeo?",
             "2. What is the largest mammal in the world?",
             "3. What is the main ingredient in guacamole?",
             "4. Who painted the Mona Lisa?")

options = (("A. Romeo and Juliet", "B. Rapunzel", "C. Titanic", "D. Fast & furious"),
           ("A. Elephant", "B. Mouse", "C. Blue Whale", "D. Girrafe"),
           ("A. Apple", "B. Strawberry", "C. Macha", "D. Avocado"),
            ("A. Albert Einstein", "B. Leonardo Da Vinci", "C. Picasso", "D. Bob Ross"))

answers = ("A", "C", "D", "B")
guesses = []
question_num = 0
score = 0

for question in questions:
    print("=========================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")

    question_num += 1

print()
print("======================")
print("=====  RESULTS  ======")
print("======================")
print()

print("Correct answers = ", end = "")
for answer in answers:
    print(answer, end = " ")
print()
print("Correct answers = ", end = "")
for guess in guesses:
    print(guess, end = " ")

print()
total = float((score / 4) * 100)
print(f"You got {score} out of 4 - {total}%")
if score == 4:
    print("GOOD JOB! ☻☺☻☺")
else:
    print("GO AND STUDY!")





