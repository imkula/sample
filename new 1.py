class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("No tasks.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
