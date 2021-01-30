row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")


# column 2, row 3 would be entered as:

# ```
# 23
# ```
column = int(position[0])-1
rows = int(position[1])-1



map[rows][column] = 'x'
print(f"{row1}\n{row2}\n{row3}")
