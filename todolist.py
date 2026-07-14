tasks = list()
toggle = False

def ToDoList():
    if len(tasks) == 0:
        print()
        print("No tasks")
        print()
    else:
        print()
        print("To-Do List: ")
        for i in range(len(tasks)):
            if toggle and tasks[i][1]:
                continue
            mark = "x" if tasks[i][1] else " "
            print(f'{i + 1}. [{mark}] {tasks[i][0]}')
        print()

while True:
    # navigation bar
    print("Menu: ")
    print("1. Show To-do list.")
    print("2. Add a new task.")
    print("3. Delete a task.")
    print("4. Mark a task as done.")
    print("5. Edit a task")
    print("6. Toggle showing completed tasks")
    print("exit")
    print()

    choice = input("Enter your choice: ")

    # 1 Show the to-do list
    if choice == "1":
            ToDoList()
    # 2 Add a new task
    elif choice == "2":
        print()
        print("'cancel' to exit")
        print()
        new_task = input("Enter a new task: ")
        if new_task == "cancel":
            print()
            continue
        tasks.append([new_task, False])
        print("Task added!")
        print()

    # 3 Delete a task
    elif choice == "3":
        if len(tasks) == 0:
            print()
            print("No tasks to delete.")
            print()
            continue
        else:
            ToDoList()
            print("'cancel' to exit")
            print()
            task_delete = input("Choose the task number to delete: ")
            if task_delete == "cancel":
                print()
                continue
            # checking if input is digit
            elif not task_delete.isdigit():
                print()
                print("Error")
                print()
                continue
            # checking input if out of bounds
            elif (int(task_delete) - 1 >= len(tasks)) or int(task_delete) - 1 < 0:
                print()
                print("Error")
                print()
                continue
            tasks.pop(int(task_delete) - 1)
            print("Task deleted.")
            print()

    # 4 Mark as done
    elif choice == "4":
        if len(tasks) == 0:
            print()
            print("No tasks to mark as done.")
            print()
            continue
        else:
            ToDoList()
            print("'cancel' to exit")
            print()
            mark_as_done = input("Enter your choice: ")
            if mark_as_done == 'cancel':
                print()
                continue
            # checking if input is digit
            elif not mark_as_done.isdigit():
                print()
                print("Error")
                print()
                continue
            # checking input if out of bounds
            elif (int(mark_as_done) - 1 >= len(tasks)) or int(mark_as_done) - 1 < 0:
                print()
                print("Error")
                print()
                continue
            tasks[int(mark_as_done) - 1][1] = True
            print(f"Marked task {mark_as_done} as done")
            print()
    # 5 Edit a task
    elif choice == "5":
        if len(tasks) == 0:
            print()
            print("No tasks to edit.")
            print()
            continue
        else:
            ToDoList()
            print("'cancel' to exit")
            print()
            edit_task = input("Choose a task number to edit: ")
            if edit_task == 'cancel':
                print()
                continue
            # checking if input is digit
            elif not edit_task.isdigit():
                print()
                print("Error")
                print()
                continue
            # checking input if out of bounds
            elif (int(edit_task) - 1 >= len(tasks)) or int(edit_task) - 1 < 0:
                print()
                print("Error")
                print()
                continue
            new_text = input("Edit the task: ")
            tasks[int(edit_task) - 1][0] = new_text
            print()
            print("Task edited.")
            print()
    # 6 Toggle showing completed tasks
    elif choice == "6":
        toggle = True if toggle == False else False
        print()
        print(f"Hiding completed tasks: {toggle}")
        print()
    # Exit
    elif choice == "exit":
        print('Exiting program...')
        print("Goodbye!")
        break
    # wrong input
    else:
        print()
        print("Wrong input! Try Again")
        print()
        continue