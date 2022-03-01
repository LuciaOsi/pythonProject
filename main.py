# This is a sample Python script.
print('Saludos\nLu')  # \n starts a new line
print('\'')  # prints symbols that have special meaning
name = input("Enter ur name:")  # By default the input is always a string, be carefull with numbers
print(len(name))
print("Hello " + name)
friends = ["Marga", "Vicky", "Isa", 2, True]
colors = ["Rojo", "Azul", "Amarillo"]
friends[-1]  # Starts from the bottom of the list
friends[1:]  # Gets the element of the list in the position 1 to the botton of the list
friends.extend(colors)  # Appends the colors to the friends list
print(friends)
new_tuple = (2, 5)  # Tuples are inmutable
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
is_male = False
if is_male or True and True:
    print("True")
elif not(is_male):
    print("Is male")
else:
    print("False")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
