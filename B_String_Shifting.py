s = input()
l = []
for i in range(len(s)):
    l.append(s[i:]+s[:i])
l.sort()
print(l[0])
print(l[-1])