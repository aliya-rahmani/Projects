import math

def gcd(x,y):
	while(y):
		x,y=y,x%y
	return x

def fadd(a,b,c,d):
	n1=(a*d)+(b*c)
	d1=b*d
	if(n1!=0):
		g=gcd(abs(n1),d1)
		n1=n1/g
		d1=d1/g
		return [n1,d1]
	else:
		return [0,1]

def solution(m):
	l=len(m)
	num=[]
	den=[]
	for i in range(l):
		num.append([0]*l)
		den.append([1]*l)
	for i in range(l):
		tot=0
		for j in range(l):
			tot+=m[i][j]
		num[i][i]=1
		for j in range(l):
			if(m[i][j]!=0):
				frac = fadd(num[j][i],den[j][i],-1*m[i][j],tot)
				num[j][i]=frac[0]
				den[j][i]=frac[1]
	term=[]
	for i in range(l):
		fl=0
		for j in range(l):
			if(m[i][j]!=0):
				fl=1
				break
		if(fl==0):
			term.append(i)
	prob=1
	for i in range(l):
		lcm=den[i][0]
		for j in range(l):
			lcm=(lcm*den[i][j])/gcd(lcm,den[i][j])
		for j in range(l):
			num[i][j]=(num[i][j]*lcm)/den[i][j]
			den[i][j]=1
		if(i==0):
			prob=lcm
	# gauss method
	num1=[0]*l
	den1=[1]*l
	num1[0]=prob
	for i in range(l):
		for j in range(l):
			if(i==j or num[j][i]==0):
				continue
			n1=(num[i][i]*den[j][i])
			if(num[j][i]<0):
				n1*=-1
			d1=abs(den[i][i]*num[j][i])
			for k in range(l):
				if(k==i):
					num[j][k]=num[i][i]
					den[j][k]=den[i][i]
				else:
					num[j][k]*=n1
					den[j][k]*=d1
				frac=fadd(num[j][k],den[j][k],-1*num[i][k],den[i][k])
				num[j][k]=frac[0]
				den[j][k]=frac[1]
			num1[j]*=n1
			den1[j]*=d1
			frac=fadd(num1[j],den1[j],-1*num1[i],den1[i])
			num1[j]=frac[0]
			den1[j]=frac[1]
	ans_n=[]
	ans_d=[]
	for i in range(l):
		n1=abs(num1[i]*den[i][i])
		d1=abs(den1[i]*num[i][i])
		if(n1==0):
			ans_n.append(0)
			ans_d.append(1)
		else:
			g=gcd(n1,d1)
			ans_n.append(n1/g)
			ans_d.append(d1/g)
	cd=1
	for i in term:
		cd=(cd*ans_d[i])/gcd(cd,ans_d[i])
	ans=[]
	for i in term:
		ans.append((ans_n[i]*cd)/ans_d[i])
	ans.append(cd)
	return ans


print solution([[0,1,0,0,0,1],
	[4,0,0,3,2,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0],
	[0,0,0,0,0,0]])