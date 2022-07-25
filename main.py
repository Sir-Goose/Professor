import random


def main():
    level = get_level()

    i = 0
    question_dict = {}
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        solution = generate_solution(x, y)
        question = generate_question(x, y)

        j = 0
        r = 0
        while j < 3:
            if r == 3:
                print(str(question) + str(solution))
                break
            guess = input(question)
            if guess == str(solution):
                break
            else:
                print("EEE")
                r = r + 1

        # question_dict[question] = solution
        i = i + 1

    # guess = input(question)
    # if guess == str(solution):


def get_level():
    while True:
        level = input("Level: ")
        if level == '1' or level == '2' or level == '3':
            level = int(level)
            return level


def generate_integer(level):
    if level == 1:
        number = random.randint(0, 9)
        return number
    if level == 2:
        number = random.randint(10, 99)
        return number
    if level == 3:
        number = random.randint(100, 999)
        return number


def generate_question(x, y):
    question = (str(x) + " + " + str(y) + " = ")
    return question


def generate_solution(x, y):
    solution = (x + y)
    return solution


if __name__ == "__main__":
    main()
