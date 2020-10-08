def Check(arr, row, col, num):
    for i in range(9):
        if(arr[row][i] == num):
            return False

    for i in range(9):
        if(arr[i][col] == num):
            return False

        for i in range(3):
            for j in range(3):
                if(arr[i + int(row / 3) * 3][j + int(col / 3) * 3] == num):
                    return False
    return True

def Solve(arr):
    row = -1
    col = -1

    for i in range(9):
        for j in range(9):
            if(arr[i][j] == 0):
                row = i
                col = j
                break

    if(row == -1):
        return True

    for num in range(1, 10):
        if(Check(arr, row, col, num)):
            arr[row][col] = num
            if(Solve(arr)):
                return True
            arr[row][col] = 0

    return False

if __name__ == "__main__":

    arr=  [[5, 3, 0, 0, 7, 0, 0, 0, 0],
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0],
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1],
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0],
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    if(Solve(arr)):
        for i in range(9):
            print(arr[i])

    else:
        print("Solution Doesn't exist")
