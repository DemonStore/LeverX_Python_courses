import json
import models

def read_rooms(file_rooms):
    with open(file_rooms, 'r') as fp_rooms:
        rooms = json.loads(fp_rooms.read())
    return rooms


def read_students(file_students):
    with open(file_students, 'r') as fp_students:
        students = json.loads(fp_students.read())
    return students


def write_merge(new_file_name, context):
    name = new_file_name + '.json'
    with open(name, 'w') as fp_format:
        fp_format.write(json.dumps(context))


def find_room(rooms):
    print('What number of room do find?')
    number_of_room = int(input())
    room = rooms.get(number_of_room, None)
    if room:
        print('Room id: ', room['id'])
        print('Room name: ', room['name'])
        print('Students: ', room['students'])
    else:
        print("There is no this room number ", number_of_room)


def find_student(students):
    print('What student do find?')
    name = input()
    stud = students.get(name, None)
    if stud:
        print('Student id: ', stud.student_pk)
        print('Student name: ', stud.student_name)
        print('Room: ', stud.student_room, '\n')
    else:
        print("There is no ", name)