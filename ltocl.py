def spl(l):
	cnt = 0
	ret = -1
	for i in range(len(l)-1):
		if l[i]=='(':
			cnt+=1
		if l[i]==')':
			cnt-=1
		if cnt==0:
			ret=i
	if ret == -1:
		return l, ""
	else:
		return l[:ret+1],l[ret+1:]

def T(l):
	if len(l)==1:
		return l
	if l[0]!='L':
		l1,l2 = spl(l)
		if l==l1:#parentheses
			return T(l[1:-1])
		return "("+T(l1)+T(l2)+")"
	var = l[1]
	l=l[3:]
	if not (var in l):
		return "(K"+T(l)+")"
	if len(l)==1:#must be Id
	 	return "(SKK)"
		#return "I"
	if l[0]=='L':#double abstraction
		return T("L"+var+"."+T(l))
	l1,l2 = spl(l)
	if l==l1:#parentheses
		l=l[1:-1]
	l1,l2 = spl(l)
	return "(S"+T("L"+var+"."+l1)+T("L"+var+"."+l2)+")"

def pretty(l):#expands lambda abstractions
	ret = ""
	abstr = False
	for c in l:
		if c=='L':
			abstr=True
			continue
		if c=='.':
			abstr=False
			continue
		if abstr:
			ret += "L"+c+"."
		else:
			ret+=c
	return ret

def clean(l):#cleans up parentheses
	if len(l)<=1:
		return l
	l1,l2 = spl(l)
	if l1[0]=='(' and l1[-1]==')':
		l1=l1[1:-1]
	l1 = clean(l1)
	while l2!="":
		l3,l2 = spl(l2)
		if len(l3)>1:
			l3="("+clean(l3[1:-1])+")"
		if len(l3)==3:
			l3=l3[1:-1]
		l1+=l3
	return l1


lamb = input()
print(clean(T(pretty(lamb))))
