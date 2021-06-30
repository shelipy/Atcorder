

S = int(46979)

h = S // 3600
m = (S % 3600)//60
s = (S % 3600)%60

output = str(h) + str(':') + str(m) + str(':') + str(s)


print(output)