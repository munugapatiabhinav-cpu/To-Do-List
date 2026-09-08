task1 = []
com_tasks = []


while True:
    print("                                     TO-DO LIST")
    n = 0
    
    n = int(input("If your wish is to see your list (Type 1), or if your wish is to create a new task to complete (Type 0):"))
    

    if n==0:
        new_task = str(input("Enter the task you want to complete:"))
        if new_task not in task1:
            task1.append(new_task)
        else:
            print("You already have this task in you list")
        
    elif n==1:
        
        i = 1
        for tasks in task1:
            print(i,")",tasks)
            i += 1
        n-=1
        a = str(input("Have you completed any tasks (Type yes or no ):"))
        if a=="yes":
            z = int(input("Enter the task no. you have completed:"))
            com_tasks.append(task1[z-1])
        elif a=="no":
            print("Okay, no problem you still have time to do it now.")
        else:
            print("Invalid input")
        w = str(input("Do you want to view you completed tasks list (Type yes or no):"))
        if w=="yes":
            b = 1
            for com in com_tasks:
                print(b,")",com)
                b += 1
        elif w=="no":
            continue
        else:
            print("Invaid Input")
        p = str(input("Do you want to view the percentage of progress that you made:(Type yes or no)"))
        if p=="yes":
            print("The percentage of progress you achieved is",(len(com_tasks)/len(task1))*100,"%")
    else:
        print("Invalid Input")
            
            

    





    






    