x=input('enter num of rows x')
y=input('enter num of columns y')
a=[[0 for i in range(0 , y)]for j in range(0 , x)]
a=input('enter matrix a')
for e in range(x):
	for f in range(y):
		b[e][f]=input()	
p=input("enter rows of matrix 1")
q=input("enter columns of matrix 1")
b=[[0 for i in range(0 , q)]for j in range(0 , p)]
b=input('enter matrix b')
for i in range(p):
	for j in range(q):
		b[i][j]=input()	
            result[h][l]+=a[h][k]*b[k][l]  
for s in range(len(result)):
    for h in range(len(result)):
      print (result[h][l],"\t")





