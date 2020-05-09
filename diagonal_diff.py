def diagonalDifference(arr):
    n = len(array)
    sum_a = 0
    sum_b = 0

    for row in range(n):
        for col in range(n):
           if row == col:
               sum_a += array[row][col]
           if row == n - col - 1:
               sum_b += array[row][col]

    output = sum_a - sum_b

    print(abs(output))

array =  [[11, 2, 4],
          [4, 5, 6],
          [10, 8, -12]]

diagonalDifference(array)