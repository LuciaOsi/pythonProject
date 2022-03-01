from Question import Question

question_prompts = [
    "Color of apples?\n(a) Blue\n(b) Purple\n(c) Red\n\n",
    "Color of bananas?\n(a) Blue\n(b) Yellow\n(c) Red\n\n",
    "Color of kiwi?\n(a) Green\n(b) Purple\n(c) Red\n\n"
]

questions_answers = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Score: " + str(score)+"/"+str(len(questions)))


run_test(questions_answers)
