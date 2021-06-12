#xi=[ip1,ip2]
x1=[1,1]
x2=[1,-1]
x3=[-1,1]
x4=[-1,-1]
X1
1 and -1

X2
1 and -1

Bias

y = t
W1 =0, 1,0,1,2

W2 =0,1,2,1,2

b w =0,1,0,-1,-2

Output Y

xilist=[x1,x2,x3,x4]
y=[1,-1,-1,-1]
w1=w2=bw=0
b=1
def heb_learn():
global w1,w2,bw
print(&quot;dw1\tdw2\tdb\tw1\tw2\tb&quot;)
i=0
for xi in xilist:
dw1=xi[0]*y[i]
dw2=xi[1]*y[i]
db=y[i]
w1=w1+dw1
w2=w2+dw2
bw+=db
print(dw1,dw2,db,w1,w2,bw,sep=&#39;\t&#39;)
i+=1
print(&quot;Learning...&quot;)
heb_learn()
print(&quot;Learning completed&quot;)
print(&quot;Output of AND gate using obtained w1,w2,bw:&quot;)
print(&quot;x1\tx2\ty&quot;)
for xi in xilist:
print(xi[0],xi[1],w1*xi[0]+w2*xi[1]+b*bw, sep=&#39;\t&#39;)
print( &quot; lets define the function f as f(x) = 1 if f(x)&gt;1 and f(x)=-1 if f(x) &lt;=1&quot;)
for xi in xilist:
print(xi[0],xi[1],1 if w1*xi[0]+w2*xi[1]+b*bw&gt;0 else -1,sep=&#39;\t&#39;)
