# Import things from another file
import usefull_tools as tools
from Student import Student
from Chef import Chef
from ChinesseChef import ChinesseChef

print(tools.roll_dice(3))

# List of python external modules in google by version u can access importing them --> Lib


student1 = Student("Lucia", "Tech", 3.1, False)
print(student1.on_honor_roll())

chef1 = Chef()
chefCh = ChinesseChef()

