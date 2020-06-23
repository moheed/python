print("Hello World!")
s1="moheed"
s2="ahmad"
#replace all chars of s1 with '+' those not present in s2
#s1-s2 replace with +
ls1=list(s1)
s2map=dict()
for i,c in enumerate(s2):
    s2map[c]=i
for i,k in enumerate(ls1):
    if k not in s2map:
        ls1[i]='+'
print("".join(ls1))
        