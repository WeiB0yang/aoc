from collections import deque
from collections import defaultdict


with open('inp.txt','r') as f:
    inp = f.read().strip().split('\n')

d = defaultdict(int)
stack = []
for i, e in enumerate(inp):
    if e.startswith('$ cd') and '..' not in e:
            cwd = e.split()[-1]
            p = stack.pop() if stack else ()
            pwd = (*p, cwd) 
            stack.append(pwd)
            d[pwd] = 0
    
    elif '..' in e:
        stack = [stack.pop()[:-1]]
    
    elif e[0].isdigit():
        dir_total = int(e.split()[0])
        d[pwd] += dir_total
        for i, p in enumerate(pwd):
            if len(pwd[:-i]) > 0:
                d[pwd[:-i]] += dir_total

p1 = sum(v for v in d.values() if v <= 100000)
p2 = [i for i in sorted(d.values()) if i >= 572957][0]

print(p1)
print(p2)
