def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    return [ "Hello, my name is " + name + "." for name in names ]


def assign_rooms(names):
    list = []
    index = 1
    for name in names:
        list.append(f"Hello, {name}! You'll be assigned to room {index}!")
        index += 1
    return list

def printer(names):
    return None
