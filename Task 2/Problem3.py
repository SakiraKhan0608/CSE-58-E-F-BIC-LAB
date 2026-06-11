# pattern = input().strip()
# comp={'A':'T','T':'A','C':'G','G':'C'}
# result=""

# for c in reversed(pattern):
#   result+=comp[c]

# print(result)



string=input()

s=""
for char in string:
   if char=='A':
    s+='T'
   elif char=='T':
    s+='A'
   elif char=='G':
    s+='C'
   elif char=='C':
    s+='G'

rev=s[::-1]
print(rev)
