m, n = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(list(map(int,input().split())))

target = int(input())

low, high = 0, m*n-1
found = False

while low<=high:
    mid = (low+high)//2
    row = mid//n
    col = mid%n

    if matrix[row][col]==target:
        found = True
        break
    elif matrix[row][col]<target:
        low=mid+1
    else:
        high=mid-1

if found:
    print("True")
else:
    print("False")


# 3 4
# 1 3 5 7
# 10 11 16 20
# 23 30 34 60
# 16
