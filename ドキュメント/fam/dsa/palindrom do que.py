word=input("enter a word:")
queue=list(word)
print(queue)
is_palindrome=True
while len(queue)>1:
    front=queue.pop(0)
    rear=queue.pop()  

    if front!=rear:
      is_palindrome=False
      break
if is_palindrome:
    print(f"word {word} is palindrome")
else:
    print(f"word {word} is not palindrome")   