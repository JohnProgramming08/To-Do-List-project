import tkinter as tk


class Operations:
  #setting up lists of data and display widgets
  def __init__(self, entry, listbox):
    self.entry = entry
    self.listbox = listbox
    
    file = open("tasks.txt", "r")
    self.data = file.readlines()
    file.close()

    self.seen_data = []
    for line in self.data:
      new_line = line.strip()
      status = new_line[-5:]
      
      if status == "-done":
        status = "done"
        new_line = f"|{status}|: {new_line[:-5]}"

      elif status == "-todo":
        status = "to-do"
        new_line = f"|{status}|: {new_line[:-5]}"

      else:
        status = "in progress"
        new_line = f"|{status}|: {new_line[:-12]}"
        
      self.seen_data.append(new_line)

  #adds a task to listbox and saves it
  def add_task(self):
    self.task_name = self.entry.get()
    self.new_task_name = f"|to-do|: {self.task_name}"

    self.listbox.insert(tk.END, self.new_task_name)
    self.seen_data.append(self.new_task_name)
    
    self.entry.delete(0, tk.END)
    self.entry.insert(0, "Task added!")

    self.data.append(f"{self.task_name}-todo")
    for line in self.data:
      if line[-1:] != "\n":
        new_line = f"{line}\n"
        index = self.data.index(line)
        self.data[index] = new_line

    file = open("tasks.txt", "w")
    file.writelines(self.data)
    file.close()

  #deletes a task from listbox and saves it
  def delete_task(self):
    try:
      selected_task = self.listbox.get(tk.ANCHOR)
      self.listbox.delete(tk.ANCHOR)

      index = self.seen_data.index(selected_task)
      self.seen_data.pop(index)
      self.data.pop(index)

      file = open("tasks.txt", "w")
      file.writelines(self.data)
      file.close()
  
      self.entry.delete(0, tk.END)
      self.entry.insert(0, "Task deleted!")

    except:
      self.entry.delete(0, tk.END)
      self.entry.insert(0, "No task selected!")

  #marks a task as done and saves it
  def mark_task_done(self):
    try:
      task = self.listbox.get(tk.ANCHOR)
      index = self.seen_data.index(task)
      unseen_task = self.data[index]
    
      if unseen_task[-6:] == "-todo\n" or unseen_task[-6:] == "-done\n":
        unseen_task = f"{unseen_task[:-6]}-done\n"
        self.data[index] = unseen_task
      
        new_task = f"|done|: {unseen_task[:-6]}"
        self.seen_data[index] = new_task

        self.listbox.delete(tk.ANCHOR)
        self.listbox.insert(index, new_task)

      else:
        unseen_task = f"{unseen_task[:-13]}-done\n"
        self.data[index] = unseen_task

        new_task = f"|done|: {unseen_task[:-6]}"
        self.seen_data[index] = new_task

        self.listbox.delete(tk.ANCHOR)
        self.listbox.insert(index, new_task)

      file = open("tasks.txt", "w")
      file.writelines(self.data)
      file.close()

      self.entry.delete(0, tk.END)
      self.entry.insert(0, "Task marked as done!")

    except:
      self.entry.delete(0, tk.END)
      self.entry.insert(0, "No task selected!")

  #marks a task as in progress and saves it
  def mark_task_progress(self):
    try:
      task = self.listbox.get(tk.ANCHOR)
      index = self.seen_data.index(task)
      unseen_task = self.data[index]
    
      if unseen_task[-6:] == "-todo\n" or unseen_task[-6:] == "-done\n":
        unseen_task = f"{unseen_task[:-6]}-in progress\n"
        self.data[index] = unseen_task
        
        new_task = f"|in progress|: {unseen_task[:-13]}"
        self.seen_data[index] = new_task

        self.listbox.delete(tk.ANCHOR)
        self.listbox.insert(index, new_task)

      file = open("tasks.txt", "w")
      file.writelines(self.data)
      file.close()

      self.entry.delete(0, tk.END)
      self.entry.insert(0, "Task marked as in progress!")

    except:
      self.entry.delete(0, tk.END)
      self.entry.insert(0, "No task selected!")
      

    
  
      
      
      
      