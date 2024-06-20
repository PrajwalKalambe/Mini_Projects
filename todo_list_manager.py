def operation(num):
    match num:
        case 1:
            print(list)
        case 2:
            ele=int(input("Enter number to append:-"))
            list.append(ele)
        case 3:
            ele=int(input("Enter number to append:-"))
            pos=int(input("Enter position :-"))
            list.insert(pos,ele)
        case 4:
            ele=int(input("Enter number to delete:-"))
            list.remove(ele)
        case 5:
            list.pop()
        case 0:
            exit()
        case default:
            print("Invalid Input by the user.")


list=[]
num=-1
while(num!=0):
    print("\n")
    print("Enter the operation you want to perform :-")
    print("1.Show 2.Append 3.Add 4.Delete 5.Pop-last  0.Exit")
    num=int(input("Enter Number:- "))
    operation(num)