text="python is great and python is easy"
freq={}
for word in text.split():
    freq[word]=freq.get(word,0)+1
print(freq)

list=[1,2,3,4,5,5,5,6,4]

list.sort(reverse=True)
if len(list)>=2:
    second_largest=list[1]
    print(second_largest)
else:
    print("none")    

for i in range(2,0):
    print(i)
