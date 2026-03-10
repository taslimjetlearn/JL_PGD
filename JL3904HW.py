n = int(input("Enter the size of the square matrix: "))

matrix = []

# taking input for the matrix
for i in range(n):
    row = []
    for j in range(n):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

# printing the matrix
print("Matrix:")
for row in matrix:
    print(row)

# calculating trace
trace = 0
for i in range(n):
    trace = trace + matrix[i][i]

print("Trace of the matrix:", trace)