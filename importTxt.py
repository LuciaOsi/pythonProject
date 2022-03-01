# Read
# shopping_list = open("shoppingList.txt", "r")
# print(shopping_list.readable())
# print(shopping_list.read())
# print(shopping_list.readline())
# print(shopping_list.readlines()[2])
# Read all lines in a file
'''
for item in shopping_list.readlines():
    print(item)
shopping_list.close()
'''

# Write
'''
shopping_list = open("shoppingList.txt", "a")
shopping_list.write("\nNew item for the shopping list")
shopping_list.close()
'''
# Create a new file
'''
shopping_list = open("NEWshoppingList.txt", "w")
shopping_list.write("\nNew item for the shopping list")
shopping_list.close()
'''

shopping_list = open("index.html", "w")
shopping_list.write("<p>This is a paragraph</p>")
shopping_list.close()

# open("shoppingList.txt", "w")
# print(shopping_list.readable())
# Append
# open("shoppingList.txt", "a")
# Read and Write
# open("shoppingList.txt", "r+")
