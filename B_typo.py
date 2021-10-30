s = input()
t = input()
n = len(s)
change = 0
i = 0
while i < n-2:
    if s[i] != t[i]:
        if s[i] == t[i+1] and s[i+1] == t[i]:
            change += 1
            i += 1
        else:
            change += 2
    if change > 1:
        break
    i += 1
print('Yes' if change < 2 else 'No')