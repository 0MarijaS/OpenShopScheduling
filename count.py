from copy import deepcopy

m = 4
n = 4

c=0
for i in range(n):
	for j in range(m):
		for k in range(i, n):
			for l in range(j, m):
				if i == k and j == l:
					continue
				c+=1
				
print(c)
