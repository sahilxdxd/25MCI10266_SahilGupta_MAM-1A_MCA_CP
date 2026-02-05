# Codeforces 2047B . 
# B. Replace Character
from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input().strip())

    freq = Counter(s)

    if len(freq) == 1:
        print("".join(s))
        continue

    max_char = max(freq, key=lambda c: freq[c])
    min_char = min((c for c in freq if c != max_char), key=lambda c: freq[c])

    for i in range(n):
        if s[i] == min_char:
            s[i] = max_char
            break

    print("".join(s))
