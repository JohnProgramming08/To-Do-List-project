from display import Display
from operations import Operations

#creates the window and adds commands to the buttons
if __name__ == "__main__":
  display = Display()
  display.frames()
  display.create_listbox()
  operations = Operations(display.entry, display.listbox)
  display.buttons(operations.delete_task, operations.add_task, operations.mark_task_done, operations.mark_task_progress)
  display.root.mainloop()


