# NAMES = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]

def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [ f"Hello, my name is {name}." for name in names ]


def assign_rooms(names):
    list = []
    index = 1
    for name in names:
        list.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index += 1
    return list

def printer(names):
    for badges in batch_badge_creator(names):
        print(badges)
    for assigned in assign_rooms(names):
        print(assigned)
    




    
