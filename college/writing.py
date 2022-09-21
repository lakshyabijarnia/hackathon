with open("tables.txt","w") as file:
    table=input("Enter the no you want the table of: ")
    for i in range(1,11):
        file.write("{} X {} = {}\n".format(table,i,int(table)*i))

file = open("tables.txt",'r')
# print(file.readline())
print(file.read())
file.close()