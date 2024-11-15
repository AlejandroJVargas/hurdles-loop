import random


def jump_hurdle():
    return "You jump over a hurdle"


def walk_hurdle():
    return "You walk over a hurdle"


max_track = 10


for _ in range(max_track):
    hurdles = random.choice([0, 1])
    if hurdles == 1:
        print(jump_hurdle())
    elif hurdles == 0:
        print(walk_hurdle())
    else:
        print("You couldnt walk or jump the hurdle")
