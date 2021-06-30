#ABC81B

N = int(input())
A = list(map(int,input().split()))

Frag = 0
count2 = 0
while Frag == 0:
    count = 0
    for i in range(N):
        if A[i] % 2 == 0:
            count += 1
    if count == N:
        A = list(map(lambda x: int(x/2), A))
        count2 += 1
        Frag = 0

    else:
        Frag =1
print(count2)