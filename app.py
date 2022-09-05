import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List")

# Define add task button.
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else: # Show a warning message if empty entry added.
        tkinter.messagebox.showerror(title="Warning!", message="Please enter a task.")

# Define delete task button.
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except: # Show a warning message if no task been selected.
        tkinter.messagebox.showerror(title="Warning!", message="Please select a task.")

# Define load tasks button and read tasks from tasks.data file
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.data", "rb"))
        listbox_tasks.delete(0, tkinter.END)
        for task in tasks:
            listbox_tasks.insert(tkinter.END, task)
    except: # show a message if file tasks.data cannot be found.
        tkinter.messagebox.showerror(title="Warning!", message="Cannot find tasks.data file.")

# define save button and save tasks into tasks.data file.
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.data", "wb"))


# create a frame task.
frame_task = tkinter.Frame(root)
frame_task.pack()

# Create a list box to the left of frame.
listbox_tasks = tkinter.Listbox(frame_task, width=50, height=5)
listbox_tasks.pack(side=tkinter.LEFT)

# Create scrollbar to the right of the frame
scrollbar = tkinter.Scrollbar(frame_task)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

# add scrollbar.
listbox_tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_tasks.yview)

# Create entry box to add item to the list.
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

# create and add task button.
add_task_button = tkinter.Button(root, text="Add task", width=25, command=add_task)
add_task_button.pack()

# create and add delete button.
delete_task_button = tkinter.Button(root, text="Delete task", width=25, command=delete_task)
delete_task_button.pack()

# Create and add load tasks button.
load_tasks_button = tkinter.Button(root, text="Load task", width=25, command=load_tasks)
load_tasks_button.pack()

# Create and save tasks button.
save_tasks_button = tkinter.Button(root, text="Save task", width=25, command=save_tasks)
save_tasks_button.pack()

root.mainloop()
