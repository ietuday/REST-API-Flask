from typing import List
import json


class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Team(object):
    def __init__(self, students: List[Student]):
        self.students = students


student1 = Student(first_name="Jake", last_name="Doyle")
student2 = Student(first_name="Jason", last_name="Durkin")

team = Team(students=[student1, student2])
# json_data = json.dumps(team.__dict__, indent=4)
# Serialization
json_data = json.dumps(team, default=lambda o: o.__dict__, indent=4)
print(json_data)
# Deserialization
decoded_team = Team(**json.loads(json_data))
print(decoded_team)
