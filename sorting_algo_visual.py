import matplotlib.pyplot as plt
import numpy as np

total_values = 50

l = np.random.randint(0,20,total_values)

x = np.arange(0,total_values,1)

n = len(l)
col = ['blue' for i in range(total_values)]
for i in range(n):
    
    for j in range(0,n-i-1):
       
        plt.bar(x,l,color=col)
        
        plt.pause(0.00001)
        plt.clf()
        print(l)
        
        if l[j]>l[j+1]:
            
            l[j],l[j+1]=l[j+1],l[j]
            col[j+1] = 'red'
            for i in range(j+1):
                col[i] = 'blue'

for i in range(n):
    col[i]='purple'
plt.bar(x,l,color=col)           
plt.show()