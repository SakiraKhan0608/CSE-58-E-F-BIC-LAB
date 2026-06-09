pattern = input().strip()
comp={'A':'T','T':'A','C':'G','G':'C'}
result=""

for c in reversed(pattern):
  result+=comp[c]

print(result)
