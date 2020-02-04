import json

student = {
    "first_name": "Udayaditya",
    "last_name": "Singh"
}

json_data = json.dumps(student, indent=5)
print(json_data)
print(json.loads(json_data))
