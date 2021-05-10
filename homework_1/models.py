class RoomAndStudentDictinary:
    """Объект данного класса обладает методами:
    1. rooms_merged_dict - производит слияние двух списков (список комнат
    и список студентов) и возвращает словарь, ключами в котором являются
    номера комнат, значения - информация о имени комнаты и студентах в ней.
    2. find_students_dict - возвращает словарь, ключами в котором являются
    имена студентов, значения - id студента и номер комнаты"""


    def __init__(self, initial_rooms, initial_students):
        self.initial_rooms = initial_rooms
        self.initial_students = initial_students

    def rooms_merged_dict(self):
        rooms = self.initial_rooms
        studs = self.initial_students
        if len(studs) >= len(rooms):
            min_your_students = studs[:len(studs)]
            max_your_students = studs[len(rooms):len(studs)]
            self.dict_of_rooms = dict()
            list_of_students = []
            for room, student in zip(rooms, min_your_students):
                self.dict_of_rooms[room['id']] = {
                        'id': room['id'],
                        'name': room['name'],
                        'students': []}
                current_stud_room = student['room']
                if current_stud_room in self.dict_of_rooms:
                    room_add_student = self.dict_of_rooms.get(
                            current_stud_room)
                    room_add_student['students'].append(student['name'])
                else:
                    list_of_students.append(student)

            max_your_students += list_of_students

            for student in max_your_students:
                current_stud_room = student['room']
                if current_stud_room in self.dict_of_rooms:
                    room_add_student = self.dict_of_rooms.get(
                            current_stud_room)
                    room_add_student['students'].append(student['name'])
        else:
            self.dict_of_rooms = dict()
            list_of_students = []
            for index in range(len(rooms)):
                room = rooms[index]
                dict_of_rooms[room['id']] = {
                        'id': room['id'],
                        'name': room['name'],
                        'students': []}
                if index < len(studs):
                    current_stud = studs[index]
                    current_stud_room = current_stud['room']
                    if current_stud_room in self.dict_of_rooms:
                        room_add_student = self.dict_of_rooms.get(
                                current_stud_room)
                        room_add_student['students'].append(
                                current_stud['name'])
                    else:
                        list_of_students.append(current_stud)
            for student in list_of_students:
                current_stud_room = student['room']
                if current_stud_room in self.dict_of_rooms:
                    room_add_student = self.dict_of_rooms.get(
                            current_stud_room)
                    room_add_student['students'].append(student['name'])
        return self.dict_of_rooms

    def find_students_dict(self):
        self.find_stud = dict()
        for student in self.initial_students:
            self.find_stud[student['name']] = student
        return self.find_stud