import pandas as pd
Data = {
    'Student_ID': [],
    'Name': [],
    'Math Score': [],
    'English Score': [],
    'Comments': [],
    'Grade': [],
}


class Student:

    def __init__(self):
        self.student_id = None
        self.name = None
        self.math = None
        self.English = None
        self.Comments = None
        self.Grade = None

    def input_data(self):
        self.student_id = int(input("Enter your Student ID:"))
        Data['Student_ID'].append(self.student_id)
        self.name = str(input("Enter your Student Name:"))
        Data['Name'].append(self.name)
        self.math = int(input("Enter Math\'s Score:"))
        Data['Math Score'].append(self.math)
        self.English = int(input("Enter English\'s Score:"))
        Data['English Score'].append(self.English)
        self.Comments = str(input("Give comments as Student performance:"))
        Data['Comments'].append(self.Comments)
        print("YOUR STUDENT DATA HAS BEEN ENTERED")
        if self.math + self.English > 199:
            self.Grade = 'A'
        elif self.math + self.English > 150:
            self.Grade = 'B'
        elif self.math + self.English > 100:
            self.Grade = 'C'
        else:
            self.Grade = 'F'
        Data['Grade'].append(self.Grade)


student = Student()


class Menu(Student):

    @staticmethod
    def f_menu():
        print('''\n MENU
*   Press-> 0. Add Student Data
*   Press-> 1. Calculate Grades
*   Press-> 2. Comments
*   Press-> 3. Specific Student Information''')

    @staticmethod
    def action():
        choice = int(input("Enter your choice:"))
        if choice == 0:
            student.input_data()
        elif choice == 1:
            print("Grades calculated successfully")
            df = pd.DataFrame(Data)
            print('\n', df[['Student_ID', 'Name', 'Math Score', 'English Score', 'Grade']])
        elif choice == 2:
            print("Comments Based on there performance")
            df = pd.DataFrame(Data)
            print('\n', df[['Student_ID', 'Name', 'Comments']])
        elif choice == 3:
            name1 = input("Enter student name:")
            found = False
            for i in range(len(Data['Name'])):
                if name1 == Data['Name'][i]:
                    found = True
                    df = pd.DataFrame(Data).iloc[i]
                    print("\n", df)
                    break
            if not found:
                print("Student with name", name1, "not found")
        else:
            print("Invalid Input")


menu = Menu()

while True:
    menu.f_menu()
    menu.action()
