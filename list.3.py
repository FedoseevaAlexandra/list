x=''
with open ('input.txt','r') as f:
	while True:
	   l=f.readline()
	   x+=l
	   if len(l)==0:
		   break
y=list(x.split('\n'))
y.sort()
z=str(y)
with open('output.txt','w') as f:
   f.write(z)
