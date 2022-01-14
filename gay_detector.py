from data import Question

questions_prompt = [
    "Do you like guys? \n a) Yes \n b) a bit \n c) HELLLLLLLLL NAW!\n\n",
    "Whats you favourite colour? \n a) pink \n b) black \n c) red\n\n",
    "Who do yo like? \n a) Jame Charles \n b) Justine Bieber \n c) Jay Z\n\n",
    "Are you gay? \n a) Yes \n b) a bit \n c) THE FUCK YOU SAY TO ME BITCH!\n\n",
    "Do you use condoms when having sex? \n a) No \n b) sometimes \n c) Of course\n\n",
    "Would you like to suck a dick? \n a) yes \n b) depends on the flavour of the dick that i'm sucking \n c) thats gay dude\n\n",
]

questions = [ 
    Question(questions_prompt[0], "c"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "b"),
    Question(questions_prompt[3], "b"),
    Question(questions_prompt[4], "b"),
    Question(questions_prompt[5], "b"),
]

def start_the_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.ans:
            score += 1
    if score == 6:
        print("Your score is " + str(score) + " congragulations your not gay")
    elif score > 1 < 6:
        print("Your score is " + str(score) + " Your sometimes gay")
    elif score == 0:
        print("Why are you gay")


start_the_test(questions)

