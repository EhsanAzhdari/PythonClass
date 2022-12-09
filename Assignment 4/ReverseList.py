List_Len = int(input("Enter the length of the list : "))
User_List = []
for i in range(1, List_Len+1):
    User_Input = int(input(f"Enter Number {i} : "))
    User_List.append(User_Input)
    
Reverse_List = []
for i in range(List_Len-1, -1, -1):
    Reverse_List.append(User_List[i])
    
print("List Of User : " , User_List)
print("Reverse List : " , Reverse_List)
