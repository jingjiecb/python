# def febonaci(n):
#     return 1/(5**0.5)*(((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)
#
# for i in range(6):
#     print(int(febonaci(i)))


# li=[['a',1],['c',3]]
# li2=[[['c',3],['a',1]],[['a',1],['c',3]]]
# print(li2.count(li))

# import re
# reg = re.compile(re.escape('hello'), re.IGNORECASE)
# src='Hello World, HELLO PYTHON'
# res=reg.sub('My', src)
# print(res)

# src='abc'
# for s in src:
#     print(s)

# print(ord('a'),ord('z'),ord('A'),ord('Z'))
#
# print("avc"[2])

# src=['12','3']
# print(' '.join(src))

# s1={2,1,3}
# s2={1,2,3}
# s3={3,2,1}
# li=[s1,s2]
# print(li[1]==s3)

# s1=set(range(5))
# print(s1)

# li=[[1],[2,3]]
# print(sum(li,[]))


# import sys
#
# src = sys.stdin.readlines()
# src = list(map(lambda x: x.strip('\n'), src))
# print(src)

# li=[0,1,2,3]
# print(li[-1])
# from functools import cmp_to_key
#
# li=[9,8,7]
# def cmp(a,b):
#     if 10-a>10-b:
#         return 1
#     return -1
# li.sort(key=cmp_to_key(cmp))
# print(li)

import sys
src=sys.stdin.readlines()
src=list(map(lambda x:x[:-1],src))
print("\n'",end='')
print(r'\n'.join(src),end='')
print("'")
# from collections import defaultdict
#
# e=defaultdict(set)
#
# print({1})