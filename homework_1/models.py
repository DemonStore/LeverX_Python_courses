class Student:
    def __init__(self, student_pk, student_name, student_room):
        self.student_pk = student_pk
        self.student_name = student_name
        self.student_room = student_room
        
    def __str__(self):
        return self.student_name
    
    def __repr__(self):
        return self.student_name
    

class Room:
    def __init__(self, room_pk, room_name, students=None):
        self.room_pk = room_pk
        self.room_name = room_name
        if not students:
            self.students = []
            
    def __str__(self):
        return self.room_name
    
    def __repr__(self):
        return self.room_name