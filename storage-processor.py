#imports libraries needed

import json

try :#Opens and reads the JSON task list
     with open('storage.json', 'r') as file:
         data = json.load(file)
except json.JSONDecodeError:  # Handle empty or invalid JSON file
        data = [] 

print(type(data))
#declares variables and format we need for the list
task = input('Whats your task?\n').strip()
new_task = {"task": task}
data.append(new_task)
#writes input in the json file


with open('storage.json', 'w') as file:
     json.dump(data, file)
print('saved')


for item in data:
    print(f"Task:data['task']")  
    print(f"Completed:data['completed']")  

