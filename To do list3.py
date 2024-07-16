from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():  
    task_string = task_field.get().strip()  # Strip leading/trailing whitespace
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Task field is empty.')  
    else:    
        tasks.append(task_string)   
        try:
            the_cursor.execute('insert into tasks (title) values (?)', (task_string,))
            the_connection.commit()  # Commit the transaction
            list_update()    
            task_field.delete(0, 'end')
        except Exception as e:
            messagebox.showerror('Error', f'Failed to add task: {e}')

def list_update():    
    clear_list()    
    try:
        the_cursor.execute('select title from tasks')
        for row in the_cursor.fetchall():
            tasks.append(row[0])
            task_listbox.insert('end', row[0])
    except Exception as e:
        messagebox.showerror('Error', f'Failed to fetch tasks: {e}')

def delete_task():  
    try:  
        selected_task = task_listbox.curselection()
        if selected_task:
            index = selected_task[0]
            task_value = task_listbox.get(index)
            tasks.remove(task_value)    
            the_cursor.execute('delete from tasks where title = ?', (task_value,))
            the_connection.commit()  # Commit the transaction
            list_update()
        else:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
    except Exception as e:
        messagebox.showerror('Error', f'Error: {e}')
  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        tasks.clear()    
        try:
            the_cursor.execute('delete from tasks')
            the_connection.commit()  # Commit the transaction
            list_update()
        except Exception as e:
            messagebox.showerror('Error', f'Failed to delete tasks: {e}')

def clear_list():   
    task_listbox.delete(0, 'end')  

def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    tasks.clear()    
    try:
        the_cursor.execute('select title from tasks')
        for row in the_cursor.fetchall():
            tasks.append(row[0])
    except Exception as e:
        messagebox.showerror('Error', f'Failed to retrieve tasks: {e}')

if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("To-Do List")  
    guiWindow.geometry("665x400+550+250")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg="#F0F0F0")  # Light gray background
   
    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    tasks = []  
    
    functions_frame = Frame(guiWindow, bg="#F0F0F0")  # Light gray background
    functions_frame.pack(side="top", expand=True, fill="both", padx=20, pady=20)  
    
    task_label = Label(functions_frame, text="TO-DO LIST",  
                       font=("Arial", "20", "bold"),  
                       bg="#F0F0F0", fg="#333333")  # Dark gray text color
    task_label.pack(anchor='w')  
    
    task_field = Entry(functions_frame, font=("Arial", "14"), width=50)  
    task_field.pack(pady=10)  
    
    add_button = Button(functions_frame, text="Add Task", width=12, font=("Arial", "12", "bold"),  
                        bg='#4CAF50', fg='white',  # Green button with white text
                        command=add_task)  
    add_button.pack(side='left', padx=5)  
    
    del_button = Button(functions_frame, text="Delete Task", width=12, font=("Arial", "12", "bold"),  
                        bg='#FF5733', fg='white',  # Red button with white text
                        command=delete_task)  
    del_button.pack(side='left', padx=5)  
    
    del_all_button = Button(functions_frame, text="Delete All", width=12, font=("Arial", "12", "bold"),  
                            bg='#FF5733', fg='white',  # Red button with white text
                            command=delete_all_tasks)  
    del_all_button.pack(side='left', padx=5)  
    
    exit_button = Button(functions_frame, text="Exit / Close", width=58, font=("Arial", "12", "bold"),  
                         bg='#3498DB', fg='white',  # Blue button with white text
                         command=close)  
    exit_button.pack(side='bottom', pady=10, fill='x')  
    
    task_listbox = Listbox(functions_frame, width=65, height=10, font=("Arial", "12"),  
                           bg='white', fg='black',  # White background with black text
                           selectmode='SINGLE')  
    task_listbox.pack(pady=10, fill='both', expand=True)  
    
    retrieve_database()  
    list_update()  
    
    guiWindow.mainloop()  
    
    the_connection.close()
