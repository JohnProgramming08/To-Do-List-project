from colorama import Fore


print("To Do List Prototype\n")

file = open("prototype.txt", "r")

data = file.readlines()

#removing all escape characters 
seen_data = []
for line in data:
  new_line = line.strip()
  seen_data.append(new_line)

file.close()

#adding a number before each task
iteration = 1
for line in seen_data:
  new_line = f"{iteration}: {line}"
  index = iteration - 1
  seen_data[index] = new_line
  iteration += 1

#printing tasks in colour based on status
for line in seen_data:
  status = line[-4:]
  if status == "done":
    print(Fore.GREEN + line)

  elif status == "todo":
    print(Fore.RED + line)

  else:
    print(Fore.YELLOW + line)
print(Fore.WHITE)

print("\nPlease select an option:")
print("1: Remove a task")
print("2: Add a task")
print("3: Mark a task as in progress")
print("4: Mark a task as done")
option = input("option: ")

#removes selected task and deletes it 
if option == "1":
  task = input("Select a task to remove: ")
  for line in seen_data:
    task_number = line[0]
    if task == task_number:
      index = seen_data.index(line)
      data.pop(index)

      #saves new list of tasks to file
      file = open("prototype.txt", "w")
      
      index = 0
      for value in data:
        escape = value[-1:]
        if escape != "\n":
          data[index] = f"{value}\n"
        
        index += 1

      file.writelines(data)
      file.close()
      break

#adds a task to the file and saves it
if option == "2":
  task = input("Enter a task to add: ")
  task += "-todo\n"

  data.append(task)
  seen_data.append(task)

  file = open("prototype.txt", "w")

  index = 0
  for value in data:
    escape = value[-1:]
    if escape != "\n":
      data[index] = f"{value}\n"
        
    index += 1

  file.writelines(data)
  file.close()

#marks a task as in progress and saves it
if option == "3":
  task = input("Select a task to mark as in progress: ")
  for line in seen_data:
    if task == line[0]:
      new_line = f"{line[:-5]}-in progress\n"
      data_new_line = new_line[3:]
      
      index = seen_data.index(line)
      seen_data[index] = new_line
      data[index] = data_new_line

      file = open("prototype.txt", "w")
      
      index = 0
      for value in data:
        escape = value[-1:]
        if escape != "\n":
          data[index] = f"{value}\n"
        
        index += 1
      
      file.writelines(data)
      file.close()
      break

if option == "4":
  task = input("Select a task to mark as done: ")
  for line in seen_data:
    if task == line[0]:
      new_line = f"{line[:-12]}-done\n"
      data_new_line = new_line[3:]
      
      index = seen_data.index(line)
      data[index] = data_new_line
      seen_data[index] = new_line

      file = open("prototype.txt", "w")

      index = 0
      for value in data:
        escape = value[-1:]
        if escape != "\n":
          data[index] = f"{value}\n"
        
        index += 1

      file.writelines(data)
      file.close()


