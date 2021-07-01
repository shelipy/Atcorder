#N, A, B = map(int,input().split())
N,A,B = 100,4,16
count = 0
for i in range(N+1):
    str_N = str(N)
    length = len(str_N)

    sum = 0
    for j in range(len(str_N)):
        sum = sum + int(str_N[j])
        print(i, j, sum)
    if A <= sum <= B: 
        count += 1
print(count)

