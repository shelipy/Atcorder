N = int(input())
#N = 3
t = [0] * N
l = [0] * N
r = [0] * N

#t[0],t[1],t[2] = 1,2,3
#l[0],l[1],l[2] = 1,2,2
#r[0],r[1],r[2] = 2,3,4


ans = 0
for i in range(N):
    #上から順番に代入していく
    t[i], l[i], r[i] = map(int, input().split())

for i in range(N):
    if t[i] == 1:
        l[i] = l[i] * 2
        r[i] = r[i] * 2
    elif t[i] == 2:
        l[i] = l[i] * 2
        r[i] = r[i] * 2 - 1
    elif t[i] == 3:
        l[i] = l[i] * 2 + 1
        r[i] = r[i] * 2
    else:
        l[i] = l[i] * 2 + 1
        r[i] = r[i] * 2 - 1

for i in range(N):
    for j in range(i+1,N):
        ans += (min(r[i],r[j]) - max(l[i],l[j]) >= 0)

print(ans)