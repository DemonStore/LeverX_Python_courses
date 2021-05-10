import argparse
import json
import xml.etree.ElementTree as xmlET


def parsing():
    parse_file = argparse.ArgumentParser()
    parse_file.add_argument(
            '-stud', '--students',
            type=str,
            required=True,
            help='File with list of students (e.g. students.json)')
    parse_file.add_argument(
            '-rms', '--rooms',
            type=str,
            required=True,
            help='File with list of rooms (e.g. rooms.json)')
    parse_file.add_argument(
            '-nfn', '--new_file_name',
            type=str,
            required=True,
            help='Merged file name')
    parse_file.add_argument(
            '-frm', '--format',
            type=str,
            required=True,
            choices=['xml', 'json'],
            help='Format for merged file')
    arguments = parse_file.parse_args()
    return arguments


def read_file(context_file):
    with open(context_file, 'r') as file_pointer:
        returned_list = json.loads(file_pointer.read())
    return returned_list


class WriteMergedFile:
    """Класс служит для записи файл объединенного списка студентов
    и комнат. В зависимости от передаваемого параметра файл может
    быть в форматах json и xml"""


    def __init__(self, new_file_name, context):
        self.name = new_file_name
        self.context = context

    def write_merged_json(self):
        name = self.name + '.json'
        with open(name, 'w') as fp_format:
            fp_format.write(json.dumps(self.context))

    def write_merged_xml(self):
        name = self.name + '.xml'
        rooms = xmlET.Element('rooms')

        for the_room, value in self.context.items():
            name_add_room = str(value['name'])
            add_room = xmlET.SubElement(rooms, name_add_room)
            add_id = xmlET.SubElement(add_room, 'id')
            add_id.text = str(value['id'])
            add_students = xmlET.SubElement(add_room, 'students')
            
            for stud in value['students']:
                the_stud = xmlET.SubElement(add_students, str(stud))

        xml = xmlET.tostring(rooms, encoding='unicode')

        with open(name, 'w') as fp_format:
            fp_format.write(xml)


class Find:
    """Класс служит для поиска студента или комнаты"""


    def find_room(self, rooms):
        print('What number of room do you find?')
        number_of_room = int(input())
        room = rooms.get(number_of_room, None)
        if room:
            print('Room id: ', room['id'])
            print('Room name: ', room['name'])
            print('Count of students: ', len(room['students']))
            print('Students: ', room['students'])
        else:
            print(f"There is no room with number {number_of_room} \n")

    def find_student(self, students):
        print('What student do you find?')
        name = input()
        stud = students.get(name, None)
        if stud:
            print('Student id: ', stud['id'])
            print('Student name: ', stud['name'])
            print('Room: ', stud['room'], '\n')
        else:
            print(f"There is no student with name {name}")