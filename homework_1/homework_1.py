import models
import utils

print('Enter the name of the file with rooms (e.g. rooms.json)')
room_input = input()
print('Enter the name of the file with students (e.g. students.json)')
students_input = input()
your_rooms = utils.read_rooms(room_input)
your_students = utils.read_students(students_input)

dict_of_rooms = dict()
list_of_students = []
dict_find_students = dict()

if len(your_students) >= len(your_rooms):
    min_your_students = your_students[:len(your_rooms)]
    max_your_students = your_students[len(your_rooms):len(your_students)]
    del your_students
    
    for room, student in zip(your_rooms, min_your_students):
        new_room = models.Room(room['id'], room['name'])
        dict_of_rooms[room['id']] = {
            'id': new_room.room_pk,
            'name': new_room.room_name,
            'students': new_room.students
        }
        new_student = models.Student(student['id'], student['name'], student['room'])
        dict_find_students[new_student.student_name] = new_student
        current_stud_room = student['room']
        if current_stud_room in dict_of_rooms:
            room_add_student = dict_of_rooms.get(current_stud_room)
            room_add_student['students'].append(new_student.student_name)
        else:
            list_of_students.append(student)

    del min_your_students
    max_your_students += list_of_students
    del list_of_students
    
    for student in max_your_students:
        new_student = models.Student(student['id'], student['name'], student['room'])
        dict_find_students[new_student.student_name] = new_student
        current_stud_room = student['room']
        if current_stud_room in dict_of_rooms:
            room_add_student = dict_of_rooms.get(current_stud_room)
            room_add_student['students'].append(new_student.student_name)
    del max_your_students
else:
    for index in range(len(your_rooms)):
        new_room = models.Room(your_rooms[index]['id'], your_rooms[index]['name'])
        dict_of_rooms[your_rooms[index]['id']] = {
            'id': new_room.room_pk,
            'name': new_room.room_name,
            'students': new_room.students
        }
        if index < len(your_students):
            current_stud_room = your_students[index]['room']
            new_student = models.Student(your_students[index]['id'], your_students[index]['name'], current_stud_room)
            dict_find_students[new_student.student_name] = new_student
            if current_stud_room in dict_of_rooms:
                room_add_student = dict_of_rooms.get(current_stud_room)
                room_add_student['students'].append(new_student.student_name)
            else:
                list_of_students.append(new_student)
    for student in list_of_students:
        current_stud_room = student.student_room
        if current_stud_room in dict_of_rooms:
            room_add_student = dict_of_rooms.get(current_stud_room)
            room_add_student['students'].append(student.student_name)

utils.write_merge('format', dict_of_rooms)

find_to = False
while find_to != 'q':
    print(r'Find room - press "r"')
    print(r'Find student - press "s"')
    print(r'For exit - press "q"')
    find_to = str(input())
    if find_to == 'r':
        utils.find_room(dict_of_rooms)
    if find_to == 's':
        utils.find_student(dict_find_students)