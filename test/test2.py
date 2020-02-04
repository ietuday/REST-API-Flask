# there is the __dict__ on any python object,
# which is a dictionary used to store an object’s (writable)
# attributes. We can use that for working with JSON, and that
# works well.


import json


class Student(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


student = Student(first_name='Udayaditya', last_name='Singh')
json_data = json.dumps(student.__dict__)

print(json_data)
print(Student(**json.loads(json_data)))


# The double asterisks ** in the Student(**json.load(json_data)
# line may look confusing. But all it does is expanding the
#  dictionary. In this case, it is equivalent to:
# d = json.loads(json_data)
# Student(first_name=d["first_name"], last_name=d["last_name"])
