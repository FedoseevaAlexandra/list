with open ('C:/Users/moonb/OneDrive/Desktop/input.txt','r') as f:
	l=f.read()
L=[]
L.extend(l)
L.sort()
with open('C:/Users/moonb/OneDrive/Desktop/output.txt','w') as f:
   f.write(''.join(L))
