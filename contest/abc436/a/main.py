n = int(input())

s = str(input())
r = ""
for i in range(n-len(s)):
    r += "o"
print(r+s)
