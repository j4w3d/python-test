from itertools import combinations
t=int(raw_input())
res=[]
for i in range(t):
  c=int(raw_input())
  i=int(raw_input())
  p=map(int,raw_input().split())
  for j,k in combinations(p,2):
      if (j+k)==c:
        a=p.index(j)
        p.remove(j)
        res.append([a,p.index(k)+1])
        break;
#print res
for i in range(t):
   print('Case #%d:'%(i+1)),(res[i][0])+1,(res[i][1])+1



  
