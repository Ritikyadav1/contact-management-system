#RITIK YADAV PROJECT
#CONTACT MANAGEMENT SYSTEM

def add():
        name = input("Enter name: ")
        if name not in dict:
            phone_number = input("Enter phone number: ")
            dict[name] = (phone_number)
            print("contact added successfully")
        else:
            print(f"contact {name} already exists.")
       
def search(name):
        if name in dict:
            print(f"Name: {name}")
            print(f"Phone Number:",dict[name])
        else: 
            print("contact is not found\n")
def update():
    name=input("enter the name of the contact")
    if name in dict:
        number=input("enter the new number")
        dict.update({name:number})
        print(" update done")
    else:
        print("contact not found ")
        
def delete():
    name=input("enter the name ")
    if name in dict:
        dict.pop(name)
        print("contact deleted successfully")
        
    else:
        print("contact is not saved")
dict={}            
while True:            
    print("\nCONTACT MANAGEMENT SYSTEM")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add()
    elif choice == '2':
           for key,value in dict.items():
                print(f'name: {key}: number: {value}')
                
    elif choice == '3':
        name=input("enter the name")
        search(name)
    elif choice == '4':
        update()
    elif choice == '5':
         delete()
    elif choice == '6':
        print("exited successfully")
        break 
else:
 print("invalid option , plz chhose valid option")
    
        
