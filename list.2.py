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
x=''
with open ('input.txt','r') as f:
	while True:
	   l=f.readline()
	   x+=l.rstrip()
	   if len(l)==0:
		   break
y=list(x)
l2=len(y)
l4=max(y)
l5=min(y)
l1=sorted(y)
l3=l1[::-1]
#l3=l.sort(reverse=True) nu lucreaza
lj=y+[111]
l1=str(l1)
l3=str(l3)
y=str(y)
lj=str(lj)
l2=str(l2)
l4=str(l4)
l5=str(l5)
with open ('output.txt','w') as f:
   f.write('continutul listei\n')
   f.write(y)
   f.write('\nlista sortata in ordine crescatoare\n')
   f.write(l1)
   f.write('\nlista sortata in ordine descrescatoare\n')
   f.write(l3)
   f.write('\nnumarul de elemente din lista=')
   f.write(l2)
   f.write('\nelementul MAX=')
   f.write(l4)
   f.write('\nelementul MIN=')
   f.write(l5)
   f.write('\nlista initiala elementul+111\n')
   f.write(lj)
x=list(x)
x.insert(2,222)
x=str(x)
with open ('output2.txt','w') as f:
   f.write('lista initiala elementul+222\n')
   f.write(x)
print(x)

        
