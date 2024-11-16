class ToDo:
    def __init__(self):
        self.task = []  

    def add_task(self, task):
        self.task.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.task, start=1):
            done = "*" if task["done"] else " "
            print(f"{i}. {task['task']} [{done}]")

    def delete_task(self, task_number):
        try:
            del self.task[task_number - 1]  
        except IndexError:
            print("Invalid Task Number.")

    def mark_done(self, task_number):
        try:
            self.task[task_number - 1]["done"] = True  
        except IndexError:
            print("Invalid Task Number.")

    @staticmethod
    def main():
        to_do = ToDo() 

        while True:
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Mark Task as Done")
            print("5. Quit")

            choice = input("Choose an option: ")
            if choice == "1":
                task = input("Enter a task: ")
                to_do.add_task({"task": task, "done": False})
            elif choice == "2":
                to_do.view_tasks()
            elif choice == "3":
                try:
                    task_number = int(input("Enter the task number to delete: "))
                    to_do.delete_task(task_number)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "4":
                try:
                    task_number = int(input("Enter the task number to mark as done: "))
                    to_do.mark_done(task_number)
                except ValueError:
                    print("Please enter a valid number.")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    ToDo.main()