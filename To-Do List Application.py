tasks = []
while True:
    print("Welcome to the To-Do List Application!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    choice = int(input(f"Enter your choice: "))
    if choice == 1:
        task1 = str(input("Enter the task description: "))
        tasks.append(task1)
        print(f"Task {task1} added to the to-do list!")

    if choice == 2:
        print("Your To-Do List:\n")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    if choice == 3:
        try:
            remove = int(input("Enter the task number to remove: "))
            if 1 <= remove <= len(tasks):
                del_task = tasks.pop(remove - 1)
                print(f"Task '{del_task}' removed from the to-do list!")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

    if choice == 4:
        print("Goodbye!")
        exit()
