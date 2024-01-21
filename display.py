import tkinter as tk


class Display:
  #creating root window
  def __init__(self):
    self.root = tk.Tk()
    self.root.config(bg = "white")
    self.root.title("To-Do List")
    self.root.geometry("425x500")
    self.root.resizable(False, False)

  #setting up the frames
  def frames(self):
    self.button_frame = tk.LabelFrame(self.root, pady = 10, padx = 10, bg = "grey")
    self.button_frame.grid(row = 3, column = 0, columnspan = 2, sticky = "W")
    
  #creating a listbox and filling it with the tasks
  def create_listbox(self):
    self.heading = tk.Label(self.root, text = "Tasks:", font = ("Ariel", 18), bg = "white")
    self.heading.grid(row = 0, column = 0, sticky = "W")

    self.listbox = tk.Listbox(self.root, bg = "light blue", width = 35, height = 15)
    self.listbox.grid(row = 1, column = 0)

    file = open("tasks.txt", "r")
    self.data = file.readlines()
    file.close()

    #puts the data into an intuitive format
    self.seen_data = []
    for line in self.data:
      new_line = line.strip()
      self.seen_data.append(new_line)

    for line in self.seen_data:
      
      status = line[-5:]
      if status == "-done":
        status = "done"
        new_line = f"|{status}|: {line[:-5]}"

      elif status == "-todo":
        status = "to-do"
        new_line = f"|{status}|: {line[:-5]}"

      else:
        status = "in progress"
        new_line = f"|{status}|: {line[:-12]}"
      
      index = self.seen_data.index(line)
      self.seen_data[index] = new_line
      self.listbox.insert(tk.END, new_line)

    self.heading_2 = tk.Label(self.root, text = "Enter task to add:", bg = "white")
    self.heading_2.grid(row = 4, column = 0, sticky = "W")

    self.entry = tk.Entry(self.root, width = 30, bg = "light blue")
    self.entry.grid(row = 5, column = 0)

    self.entry.insert(0, "task")

  #creates all the buttons
  def buttons(self, delete, add, done, progress):
    self.heading_3 = tk.Label(self.root, text = "Buttons:", bg = "white")
    self.heading_3.grid(row = 2, column = 0, sticky = "W")
    
    self.delete_button = tk.Button(self.button_frame, text = "Delete Task", command = delete)
    self.delete_button.grid(row = 0, column = 0, padx = 5, pady = 5)

    self.add_button = tk.Button(self.button_frame, text = "Add Task", command = add)
    self.add_button.grid(row = 0, column = 1, padx = 5, pady = 5)

    self.done_button = tk.Button(self.button_frame, text = "Mark as done", command = done)
    self.done_button.grid(row = 0, column = 2, padx = 5, pady = 5)

    self.progress_button = tk.Button(self.button_frame, text ="Mark as in progress", command = progress)
    self.progress_button.grid(row = 1, column = 0, columnspan = 3, padx = 5, pady = 5)
    

