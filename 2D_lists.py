number_grid = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [0]
]

animal_grid = [
 ["dog", "cat", "rabbit"],
 ["fish", "dolphin", "mouse"],
 ["giraffe", "cow", "rinho"],
 ["donkey"]
]

# print(number_grid[0][2])
print(len(number_grid))

'''
for row in number_grid:
    for col in row:
        print(col)
'''

for words in animal_grid:
    for word in words:
        translation = ""
        print(translation)
        for letter in word:
            if letter in "AEIOUaeiou":
                translation += "g"
            else:
                translation += letter
        print(translation)