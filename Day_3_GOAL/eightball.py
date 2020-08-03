from random import choice

yes = [
    "It is certain.",
    "As I see it, yes.",
    "It is decidedly so.",
    "Most likely.",
    "Outlook good.",
    "Signs point to yes.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
]

no = [
    "Don’t count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

maybe = [
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Reply hazy, try again.",
    "Concentrate and ask again."
]


def get_answer():
    answers = yes + no + maybe
    return choice(answers)


def prompt_user():
    question = str(input('Ask the Magic Eightball a Yes/No question: '))
    return question


if __name__ == '__main__':
    question = prompt_user()
    print(question)
    answer = get_answer()
    print(answer)
