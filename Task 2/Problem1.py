
text=input()
pattern=input()

count=0
for i in range(len(text)-len(pattern)+1):
  sub=text[i:i+len(pattern)]
  if sub==pattern:
   count=count+1

print(count) 
