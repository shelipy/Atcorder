N, K = map(int, input().split())


for _ in range(K):
   if N % 200 == 0:
      N = int(N/200)
   else:
      N = str(N)
      N = N + '200' 
      N = int(N)
print(N)


# 200を追加する操作は、N * 1000 + 200　にすると、文字列を介さないため、スマート