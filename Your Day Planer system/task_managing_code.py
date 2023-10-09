x = []


def add_task():
    task_name = str(input("Enter your task:"))
    task_priority = str(input("Enter task priority (High,Medium,low):"))
    task_due_date = input("Enter your task due date:")
    task_status = "not done"
    task = (task_name, task_priority, task_status, task_due_date)
    x.append(task)
    print(f"Your {task[0]} task added!")


def see_task():
    if not x:
        print("there is no task")
    else:
        print("-current tasks-")
        for task in x:
            print(f"Task:{task[0]}, priority:{task[1]}, Status:{task[2]}  | {task[3]}")


def mark_task():
    mark_task1 = str(input("Enter the name of task to mark as completed:"))
    update_task = []
    task_found = False
    global x
    for task in x:
        if task[0] == mark_task1:
            task = list(task)
            task[2] = "done"
            tuple(task)
            print(f"Task has been Marked")
            task_found = True
        else:
            print("no such task")
        update_task.append(task)
    if not task_found:
        print("there is no such task")
    x = update_task


def del_task():
    name_del_task = str(input("Enter the task name you want to delete:"))
    update_del_task = []
    task_del = False
    global x
    for task in x:
        if task[0] == name_del_task:
            print(f"Your task has been deleted")
            task_del = True
        else:
            update_del_task.append(task)
    if not task_del:
        print("there is no such task")
    x = update_del_task


def exist():
    print("thanks for your time")


while True:
    print('''-Task Management Menu-
* press 1 to add a task
* press 2 to see tasks list
* press 3 to mark task as completed
* press 4 to delete your task
* press 5 to exist''')
    choice = int(input("Enter your Choice from 1/2/3/4/5 :"))
    if choice == 1:
        add_task()
    elif choice == 2:
        see_task()
    elif choice == 3:
        mark_task()
    elif choice == 4:
        del_task()
    elif choice == 5:
        exist()
        break
    else:
        print("invalid input plzz chose from given function")