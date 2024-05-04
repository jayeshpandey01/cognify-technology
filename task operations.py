class task:
    
    def __init__(self, name, due_date , id):
        self.id = id
        self.name = name
        self.due_date = due_date

class task_managament:
    def create_task(id, title, discription):
        id = id
        name = title
        description = discription
        print("Created Task!")
    def read_tasks():
        print("Read Tasks!")
    def update_task(task_name):
        name = task_name
        print("Update Task!")
    def add(task_name, date):
        name = task_name
        due_date = date
        
        print("Added Task!")
    def delete(task_name):
        name = task_name
        print("Deleted Task!")
    
def main():
    task_manager = task_manager()

    while True:
        print("\nMenu:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task_manager.create_task(id, title, description)
        elif choice == '2':
            task_manager.read_tasks()
        elif choice == '3':
            id = int(input("Enter task ID to update: "))
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            task_manager.update_task(id, title, description)
        elif choice == '4':
            id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(id)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()