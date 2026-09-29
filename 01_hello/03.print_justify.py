#5자리 확보 후 왼쪽 정렬
a = "{0:<5d}".format(200)
print(a+'끝')

#5자리 확보 후 우측 정렬
b = "{0:>5d}".format(200)
print(b)

c = "{0:^5d}" .format(200)
print(c)

d = "{0:>05d}".format(200)
print(d)