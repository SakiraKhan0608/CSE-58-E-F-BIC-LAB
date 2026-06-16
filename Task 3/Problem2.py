pattern=input()
text=input()
d=int(input())

for i in range(len(text)-len(pattern)+1):
  substr=text[i:i+len(pattern)]
  mismatch=0
  for j in range(len(pattern)):
    if pattern[j]!=substr[j]:
      mismatch+=1

  if mismatch<=d:
    print(i)
