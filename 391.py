"""
#A my answer
D = [["E", "W"], ["N", "S"], ["NE", "SW"], ["NW", "SE"]]
C = input()
for i in range(4):
    if (C == D[i][0]):
        print(D[i][1])
    elif (C == D[i][1]):
        print(D[i][0])
        
#A answer
D = input()
ans = ""
for d in D:
    if d == "N":
        ans += "S"
    elif d == "S":
        ans += "N"
    elif d == "E":
        ans += "W"
    elif d == "W":
        ans += "E"

print(ans)
"""

"""
#B my answer
n, m = map(int, (input().split()))

#S = [input() for _ in range(n)]
S = []
    for i in range(n):
    S.append(input())
        
#T = [input() for _ in range(m)]
T = []
    for j in range(m):
    T.append(input())

for a in range(n - m + 1):
    for b in range(n - m + 1):
        for c in range(m):
            for d in range(m):
                if (S[a + c][b + d] != T[c][d]):
                    break
            else:
                continue
            break
        else:
            print(a + 1, b + 1)
            exit()
"""


#B answer
