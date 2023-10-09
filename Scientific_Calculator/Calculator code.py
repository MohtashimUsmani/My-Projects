import math as m
History1 = []


class Operation:
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2
        self.z = None
        self.__h = []

    def add(self):
        self.z = self.x + self.y
        self.__h = f"Result:{x}+{y}={self.z}"
        print(f"Result:{x}+{y}={self.z}")
        History1.append(self.__h)

    def sub(self):
        self.z = self.x - self.y
        self.__h = f"Result:{x}-{y}={self.z}"
        print(f"Result:{x}-{y}={self.z}")
        History1.append(self.__h)

    def mul(self):
        self.z = self.x * self.y
        self.__h = f"Result:{x}X{y}={self.z}"
        print(f"Result:{x}X{y}={self.z}")
        History1.append(self.__h)

    def div(self):
        if self.y != 0:
            self.z = self.x / self.y
            self.__h = f"Result:{x}/{y}={self.z}"
            print(f"Result:{x}/{y}={self.z}")
            History1.append(self.__h)
        else:
            self.z = "Division by zero is not allowed"

    def fac(self):
        if self.x < 0:
            print("Sorry factorial dost not exist for negative numbers")
        elif self.x == '0':
            print("The factorial of 0 is 1")
        else:
            self.z = m.factorial(self.x)
            self.__h = f"Result: Factorial {x}={self.z}"
            print(f"Result: Factorial {x}={self.z}")
            History1.append(self.__h)

    def sin(self):
        self.z = m.sin(m.radians(self.x))
        self.__h = f"Result: Sin {x}={self.z}"
        print(f"Result: Sin {x}={self.z}")
        History1.append(self.__h)

    def cos(self):
        self.z = m.cos(m.radians(self.x))
        self.__h = f"Result: Cos {x}={self.z}"
        print(f"Result: Cos {x}={self.z}")
        History1.append(self.__h)

    def tan(self):
        self.z = m.tan(m.radians(self.x))
        self.__h = f"Result: Tan {x}={self.z}"
        print(f"Result: Tan {x}={self.z}")
        History1.append(self.__h)

    def log(self):
        self.z = m.log(m.radians(self.x))
        self.__h = f"Result: Log {x}={self.z}"
        print(f"Result: Log {x}={self.z}")
        History1.append(self.__h)


x = None
y = None
choice = None


class Menu:

    @staticmethod
    def menu():
        text1 = 'CALCULATOR MENU'
        aline1 = "{:*^24}".format(text1)
        print(aline1)
        print('''NOTE: For using Factorial,Sin,Cos,Tan,Log. You have to enter only first number.
* Give Second Number input 0.        
        *   Available Operations
        *   Press-> 1. Addition (+)
        *   Press-> 2. Subtraction (-)
        *   Press-> 3. Multiplication (*)
        *   Press-> 4. Division (/)
        *   Press-> 5. Factorial (!)
        *   Press-> 6. sin
        *   Press-> 7. cos
        *   Press-> 8. tan
        *   Press-> 9. log''')
        global choice
        choice = int(input("Enter your choice 1/2/3/4/5/6/7/8/9:"))

    @staticmethod
    def input_number():
        global x
        x = int(input("Enter your first num:"))
        global y
        y = int(input("Enter your second num:"))

    @staticmethod
    def choice_execution():
        if choice == 1:
            operations.add()
        elif choice == 2:
            operations.sub()
        elif choice == 3:
            operations.mul()
        elif choice == 4:
            operations.div()
        elif choice == 5:
            operations.fac()
        elif choice == 6:
            operations.sin()
        elif choice == 7:
            operations.cos()
        elif choice == 8:
            operations.tan()
        elif choice == 9:
            operations.log()
        else:
            print("Wrong input")

    @staticmethod
    def history():
        print("        *   Press-> H. Show my Result\'s History")
        print("        *   Press-> Enter to continue")
        show_history = str(input()).upper()
        if show_history == 'H':
            text = "History"
            aline = "{:*^24}".format(text)
            print(aline)
            for i, r in enumerate(History1, start=1):
                print(f"{i}.{r}")


x_menu = Menu()

while True:
    x_menu.menu()
    x_menu.input_number()
    operations = Operation(x, y)
    x_menu.choice_execution()
    x_menu.history()
