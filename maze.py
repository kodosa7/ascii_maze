import random, time


def do_the_maze(char_a, char_b):
    for i in range(1,10000):
        rand = random.randrange(0,3)
        if rand < 1:
            print(char_a, end="", flush=True)
        else:
            print(char_b, end="", flush=True)
        time.sleep(0.01)

do_the_maze("/", "\\")
