rows = int(input("Enter the number of rows: "))
k = 2 * rows - 2
# Outer loop in reverse order
for i in range(rows, -2, -2):
    # Inner loop will print the number of space.
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")