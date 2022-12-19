n = int(input("Enter number of digits:"))
a = list(map(int, input("Enter set of Numbers:\n").split()))
s = 0
for i in range(n):s = s+a[i]
print(s/n)
input()