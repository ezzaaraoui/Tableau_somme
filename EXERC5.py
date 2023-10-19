T1=[]
T2=[]
T=[]

n1=int(input("donner la taille de tableau T1 : "))

for i in range(0,n1):
    T1.append(int(input(f"donner element de tableau 1 la case {i+1} : ")))
for i in range(0,n1):
    T2.append(int(input(f"donner element de tableau 2 la case {i+1} : ")))

for i in range(0,n1):
    T.append(T1[i]+T2[i])

print(T)