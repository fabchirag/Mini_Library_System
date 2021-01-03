class Student():
    def __init__(self):
        self.first_name = []
        self.last_name = []
        self.programming_books = ("python", "java", "bluej", "ruby", "php", "c++", "perl")
        self.sports_magazines = ("worldsoccer", "cyclingplus", "matchoftheday", "topgear")
        self.basket = []
        self.members = {}

    def describe_student(self):
        for name in self.first_name:
            print(f"Name of the Student: {self.first_name}".title())

    def register(self):
        x = input("Type your first name: ")
        y = input("Type your last name: ")
        self.members[x] = y
        print("Registration complete.")


    def login(self, login_name, lastname):
        if login_name in self.members.keys() or lastname in self.members.values():
            print("Login Successful!")
        else:
            print("Login Incorrect!")


    def logout(self):
        if self.members:
            print(f"Login out successful - {self.members}")
            return True
        else:
            print("Not Logged in User")
            return False


    def list_books_magazines(self):
        for x, y in zip(self.programming_books, self.sports_magazines):
            print(x.title(), y.title())

    def hire_book(self):
        h_book = input("Please Enter a book name from the list: ")
        if h_book in self.programming_books:
            self.basket.append(h_book)
            print("Book is hired...")
        else:
            print("Not avaliable in the library..!")


    def return_book(self):
        book_return = input("Type the book or magazine you would like to return: ")
        if book_return in self.basket:
            print("Book return complete")
        else:
            print("Book you have entered is not hired..")


class Admin(Student):
    def __init__(self):
        super().__init__()

    def add_student(self, first_name, last_name):
        self.members[first_name] = last_name
        print(f"{first_name.title()}, {last_name.title()} has been added to the system.")

    def remove_student(self):
        desired_key = self.members
        for key in desired_key:
            if key == desired_key:
                del self.members[key]
                print("Student has been Removed")
                break



user1 = Student()
user1.register()
user1.login("chirag", "limbachia")
user1.hire_book()
user1.return_book()
admin1 = Admin()
admin1.add_student("mike", "hussy")

