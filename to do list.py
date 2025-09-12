import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

FILE_NAME = "todo_gui.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return
    tasks.append({"task": task, "done": False})
    update_listbox()
    task_entry.delete(0, tk.END)
    save_tasks(tasks)

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✓" if task["done"] else " "
        listbox.insert(tk.END, f"[{status}] {task['task']}")

def mark_done():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Info", "Please select a task to mark as done.")
        return
    for i in selected_indices:
        tasks[i]["done"] = True
    update_listbox()
    save_tasks(tasks)

def delete_task():
    selected_indices = listbox.curselection()
    if not selected_indices:
        messagebox.showinfo("Info", "Please select a task to delete.")
        return
    for i in reversed(selected_indices):
        tasks.pop(i)
    update_listbox()
    save_tasks(tasks)

def edit_task():
    selected_indices = listbox.curselection()
    if len(selected_indices) != 1:
        messagebox.showinfo("Info", "Please select exactly one task to edit.")
        return
    idx = selected_indices[0]
    current_text = tasks[idx]["task"]
    new_text = simpledialog.askstring("Edit Task", "Modify task:", initialvalue=current_text)
    if new_text is not None and new_text.strip() != "":
        tasks[idx]["task"] = new_text.strip()
        update_listbox()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Warning", "Task text cannot be empty.")

def sort_tasks_alpha():
    tasks.sort(key=lambda x: x["task"].lower())
    update_listbox()
    save_tasks(tasks)

def sort_tasks_status():
    # Sort with undone first, then done
    tasks.sort(key=lambda x: x["done"])
    update_listbox()
    save_tasks(tasks)

# Create main window
root = tk.Tk()
root.title("To-Do List App")

# Load tasks
tasks = load_tasks()

# UI Elements
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.grid(row=0, column=0, padx=(0,10))

add_button = tk.Button(frame, text="Add Task", width=10, command=add_task)
add_button.grid(row=0, column=1)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=15)
listbox.pack(padx=10, pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

mark_done_button = tk.Button(btn_frame, text="Mark as Done", width=15, command=mark_done)
mark_done_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

edit_button = tk.Button(btn_frame, text="Edit Task", width=15, command=edit_task)
edit_button.grid(row=0, column=2, padx=5)

sort_alpha_button = tk.Button(root, text="Sort Alphabetically", width=20, command=sort_tasks_alpha)
sort_alpha_button.pack(pady=2)

sort_status_button = tk.Button(root, text="Sort by Status", width=20, command=sort_tasks_status)
sort_status_button.pack(pady=2)

update_listbox()

root.mainloop()