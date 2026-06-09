
pattern=input().strip()
genome=input().strip()

pos=[]

for i in range (len(genome)-len(pattern)+1):
  if genome[i:i+len(pattern)]==pattern:
    pos.append(str(i))

print(" ".join(pos))
