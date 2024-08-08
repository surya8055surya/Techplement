from tabulate import tabulate

class Contact_Book:
    def __init__(self):
        self.__data = {}
    
    def addContact(self, name=None, phone_number=None):
        if name and phone_number:
            if phone_number not in self.__data:
                self.__data[phone_number] = [name, phone_number]
                print("Added successfully")
            else:
                print("Number already exists")
        else:
            print("Please enter all the values")

    def deleteContact(self, phone_number=None):
        if phone_number:
            if phone_number in self.__data:
                del self.__data[phone_number]
                print("Deleted successfully")
            else:
                print("Phone number does not exist in the database")
        else:
            print("Please enter a phone number")

    def editContact(self, name=None, phone_number=None):
        if phone_number and phone_number in self.__data:
            lst_info = self.__data[phone_number]
            if name:
                lst_info[0] = name
            self.__data[phone_number] = lst_info
            print("Data updated successfully")
        else:
            print("Phone number does not exist in the database")

    def searchContact(self, query=None, sort_field=None):
        if query:
            search_arr = []
            for key, val in self.__data.items():
                search_arr.append(val + [" ".join(val)])
                        
            result = set()
            for word in query.lower().split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)
            
            ans = []
            for i in result:
                ans.append(search_arr[i][:-1])
            
            indx = 0
            if sort_field == "name":
                indx = 0
            if sort_field == "phone_number":
                indx = 1
            ans.sort(key=lambda x: x[indx])

            self.viewContact(ans)
        else:
            return []

    def viewContact(self, data):
        headers = ["Name", "Phone Number"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                n = int(input("Enter your option: "))
                if n == 1:
                    name = input("Name: ")
                    phone_number = input("Phone Number: ")
                    if not name:
                        name = None
                    if not phone_number:
                        phone_number = None
                    self.addContact(name, phone_number)

                if n == 2:
                    phone_number = input("Phone Number: ")
                    if not phone_number:
                        phone_number = None
                    self.deleteContact(phone_number)
                
                if n == 3:
                    name = input("Name: ")
                    phone_number = input("Phone Number: ")
                    if not name:
                        name = None
                    if not phone_number:
                        phone_number = None
                    self.editContact(name, phone_number)
                
                if n == 4:
                    query = input("Search: ")
                    sort_by = input("Sort by (name/phone_number): ")
                    if not query:
                        query = None
                    if not sort_by:
                        sort_by = None
                    self.searchContact(query, sort_by)

                if n == 5:
                    new_data = []
                    for key, val in self.__data.items():
                        new_data.append(val)
                    self.viewContact(new_data)
                
                if n == 6:
                    break

            except Exception as e:
                print(f"An error occurred: {e}")

contact_book = Contact_Book()
contact_book.console()
