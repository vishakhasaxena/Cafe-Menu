def task():
    tasks=[] #empty list
    print("-WELCOME TO YOUR TO-DO LIST-")
    total_task= int(input("Enter the number of task you want to do today.")) #6
    for i in range(1, total_task+1):
        task_name=input(f"Enter your {i} task = ")
        tasks.append(task_name)
        
    print(f"Today's task are\n{tasks}")
    while True:
        operation=int(input("Enter 1 -Add\n2-Update\n3-Delete\n4-View\n5-Exit\Stop"))
        if operation==1:
            add=input("Enter the task you want to add")
            tasks.append(add)
            print(f"Your {add} task has been successfully added.")
        elif operation==2:
            updated_task=input("Enter the task that has to be update")
            if updated_task in tasks:
                updated_value=input("Enter the new updated task =")
                ind=tasks.index(updated_task)
                tasks[ind]=updated_value
                print(f"New task is {updated_value}")    
            else:
                print("The the task is not present")
        elif operation==3:
            delete_task=input("Enter the task you want to delete =")
            if delete_task in tasks:
                ind=tasks.index(delete_task)
                del tasks[ind]
                print(f"Your task {delete_task} has been deleted")
            else:
                print("The the task is not present")
        elif operation==4:
            print(f"Your tasks are: {tasks}")
        elif operation==5:
            print("Closing the program.")
            break
        else:
            print("Invalid Input")
task()
                        