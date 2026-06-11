
# pattern=input().strip()
# genome=input().strip()

# pos=[]

# for i in range (len(genome)-len(pattern)+1):
#   if genome[i:i+len(pattern)]==pattern:
#     pos.append(str(i))

# print(" ".join(pos))




pattern=input()
genome=input()

for i in range(len(genome)-len(pattern)+1):
  substring=genome[i:i+len(pattern)]
  if substring==pattern:
    print(i,end=" ")
