def spl(l):#splits l into first argument and the rest
	cnt = 0
	succ=True
	for i in range(len(l)):
		if l[i]=='(':
			cnt+=1
		if l[i]==')':
			cnt-=1
		if cnt==0:
			return succ,l[:i+1],l[i+1:]
		if cnt<0:
			succ=False
	return False,l,""

def step(l):#makes one step of computation
	l=clean(l)
	for i in range(len(l)):
		if i>0 and l[i-1]!='(':
			continue
		if l[i]=='I':
			if i+1==range(len(l)) or l[i+1]==')':
				continue
			return l[:i]+l[i+1:]
		if l[i]=='K':
			s1,l1,l2 = spl(l[i+1:])
			s2,l2,l3 = spl(l2)
			if not (s1 and s2) or l2=="":
				continue
			else:
				return l[:i]+l1+l3
		if l[i]=='S':
			s1,l1,l2 = spl(l[i+1:])
			s2,l2,l3 = spl(l2)
			s3,l3,l4 = spl(l3)
			if not(s1 and s2 and s3) or l3=="":
				continue
			else:
				return l[:i]+l1+l3+"("+l2+l3+")"+l4
	return l

def clean(l):#cleans up parentheses
	if len(l)<=1:
		return l
	s,l1,l2 = spl(l)
	if l1[0]=='(' and l1[-1]==')':
		l1=l1[1:-1]
	l1 = clean(l1)
	while l2!="":
		s,l3,l2 = spl(l2)
		if len(l3)>1:
			l3="("+clean(l3[1:-1])+")"
		if len(l3)==3:
			l3=l3[1:-1]
		l1+=l3
	return l1

def compute(term):
	print (term)
	while True:
		nterm = clean(step(term))
		if nterm==term:
			break
		print ("="+nterm)
		term=nterm
p = "S(S(KS)(S(KK)(S(KS)(S(K(SI))(S(KK)I)))))(K((S(KK))I))"
pi1 = "SI(K(S(KK)I))"
pi2 = "SI(K(KI))"
compute(pi1+"("+p+"xy)")
compute(pi2+"("+p+"xy)")
