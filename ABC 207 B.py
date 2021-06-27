A, B, C, D = map(int, input().split())

blue = A
red = 0
counter = 0
diff = 0

if B >= C*D:
   print(-1)
else:

   while blue > red*D:
      blue = blue + B
      red = red + C
      counter = counter + 1
      diff = blue - red*D

   print(counter)

