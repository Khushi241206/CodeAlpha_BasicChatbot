def chatbot_response(user_input):
    user_input=user_input.lower()
    if user_input=="hello":
        return "Hi!"
    elif user_input=="how are you?":
        return "I'm fine, thank you!"
    elif user_input=="bye":
        return "Goodbye!"
    else:
        return "I didn't understand that."

def main():
    print("Welcome to MyChatbot! (type 'bye' to exit)\n")
    while True:
        user_input=input("You:")
        reply=chatbot_response(user_input)
        print("Bot:",reply)

        if user_input.lower()=="bye":
            break
main()