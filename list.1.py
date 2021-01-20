#Se citesc elementele unei liste, care reprezintă numere întregi (pozitive și negative). Să se afișeze la ecran:
	#a) conținutul (elementele) listei /lista1
	#b) lista sortată în ordine crescătoare / lista2
	#c) lista sortată în ordine descrescătoare / lista3
	#d) numărul de elemente din listă
	#e) elementul MAX
	#f) elementul MIN
	#g) să se adauge la coadă în lista inițială elementul – 111. 
	   # Să se afișeze lista nou-formată. / lista4
	#h) să se adauge pe poziția a doua din lista inițială elementul – 222. 
	   # Să se afișeze lista nou-formată. / lista5
l=[5,7,9,0,-3,-9,1]
print('conținutul listei',l)
l1=sorted(l)
print('lista sortată în ordine crescătoare',l1)
l3=l
l3.sort(reverse=True)
print('lista sortată în ordine descrescătoare',l3)
print('numărul de elemente din listă',len(l))
print('elementul MAX=',max(l))
print('elementul MIN=',min(l))
lj=l.extend([111])
print(lj)
l5=l.insert(2,222)
print(l5)
