M=input()
m=raw_input()
N=input()
n=raw_input()
m=set(m.split())
n=set(n.split())
sym_diff=m.union(n)-m.intersection(n)
print type(sym_diff)
sym_diff=list[sym_diff]
for i in sym_diff:
    print i
