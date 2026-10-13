a = [1,2,3,4,5]
b = (6,7,8,9,10)
c = {11,12,13,14,15}

#리스트를 set과 tuple로 변환
seta = set(a)
tuplea = tuple(a)
print(type(seta), seta)
print(type(tuplea), tuplea)

#tuple을 set과 리스트로 변환
listb = list(b)
setb = set(b)
print(type(listb), listb)
print(type(setb), setb)

#set을 리스트와 tuple로 변환
listc = list(c)
tuplec = tuple(c)
print(type(listc), listc)
print(type(tuplec), tuplec)