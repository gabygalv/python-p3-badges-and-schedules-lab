def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    name_list = []
    for name in names:
        name_list.append(f"Hello, my name is {name}.")
    return name_list

def assign_rooms(names):
    rooms = range(1,9)

    room_assignments = []
    for room in rooms:
        room_assignments.append(f"Hello, {names[room -1]}! You'll be assigned to room {room}!")
    
    return room_assignments

def printer(names):
    for name in batch_badge_creator(names):
        print(name)

    for room in assign_rooms(names):
        print(room)