# Chatbot program
# Function to respond user queries
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Predefined rules and responses
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm fine, Thank you for asking!"
    elif "what is your name" in user_input:
        return "I'm just a computer program, Is there anything else I can help you with ?"
    elif "what can you do" in user_input:
        return "I can respond to some basic queries based on predefined rules."
    elif "who created you" in user_input:
        return "I was created by DIPTANSHU CHOWDHURY on 25 September 2023 at 14:35 PM"
    elif "messi or ronaldo" in user_input:
        return " Both players have won multiple Ballon d’Or awards and have set numerous records in their careers." \
               " Some people may prefer Messi’s play style, while others may prefer Ronaldo’s. It often comes down to personal preference."
    elif "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Please ask another question."


# Main loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)

