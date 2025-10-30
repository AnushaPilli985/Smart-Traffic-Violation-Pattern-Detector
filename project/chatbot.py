import random
responses ={
    "hello":"Hello! How Can I help you",
    "hi":"Hi there!",
    "how are you":"I,m just a chatbod,but  a I'm doing good!",
    "bye":"Goodbye! Have a good day!"
}
def chatbot():
    while True:
        user_input=input("You:").lower()
        if user_input=="exit":
            print("Chatbot: GoodBye")
            break
        response=responses.get(user_input, "Sorry, I don't understand,")
        print(f"chatbot:{response}")
chatbot()        


