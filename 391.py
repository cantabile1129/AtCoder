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


#C answer
N, Q = map(int, input().split())
ans = 0
cnt = [0] + [1] * N
pos = list(range(N + 1))
ans_list = []
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        P, H = query[1:]
        # 鳩 P は移動する前は巣 pos[P] にいる
        # 鳩 P が移動することで 巣 pos[P] にいる鳩の数が 2 から 1 に減る場合, ans を 1 減らす
        if cnt[pos[P]] == 2:
            ans -= 1
        # 巣 pos[P] の鳩の数を 1 減らす
        cnt[pos[P]] -= 1

        # 鳩 P がいる巣を H に変更する
        pos[P] = H
        # 巣 H の鳩の数を 1 増やす
        cnt[pos[P]] += 1
        # 鳩 P が移動することで 巣 H にいる鳩の数が 1 から 2 に増える場合，ans を 1 増やす
        if cnt[pos[P]] == 2:
            ans += 1
    else:
        ans_list.append(ans)
print(ans_list)
