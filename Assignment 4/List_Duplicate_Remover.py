List_Len = int(input("Enter the length of the list : "))
User_List = []
for i in range(1, List_Len+1):
    User_Input = int(input(f"Enter Number {i} : "))
    User_List.append(User_Input)

Free_Duplicate_List = []
for i in range(List_Len):
   if User_List[i] not in Free_Duplicate_List:
       Free_Duplicate_List.append(User_List[i])


print("List Of User : " , User_List)
print("Duplicate Remove List : " , Free_Duplicate_List)