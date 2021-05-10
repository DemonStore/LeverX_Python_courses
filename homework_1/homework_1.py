import models
import utils

arguments = utils.parsing()

your_rooms = utils.read_file(arguments.rooms)
your_students = utils.read_file(arguments.students)

information = models.RoomAndStudentDictinary(your_rooms, your_students)
dict_for_file = information.rooms_merged_dict()
dict_for_students = information.find_students_dict
if arguments.format == 'json':
    utils.WriteMergedFile(
            arguments.new_file_name,
            dict_for_file).write_merged_json()
elif arguments.format == 'xml':
    utils.WriteMergedFile(
        arguments.new_file_name,
        dict_for_file).write_merged_xml()
else:
    print(r'You have to choose between "json" and "xml"')

find_to = False
while find_to != 'q':
    print(r'Find room - press "r"')
    print(r'Find student - press "s"')
    print(r'For exit - press "q"')
    find_to = str(input())
    if find_to == 'r':
        utils.Find().find_room(dict_for_file)
    if find_to == 's':
        utils.Find().find_student(dict_for_students)