import random

greetings = ["hello", "hi", "hey", "hola"]
greeting_responses = ["Hello!", "Hi there!", "Hey!", "Greetings!", "Hola!"]

# List of questions and corresponding responses
questions = ["how are you", "how's your day", "how are you doing"]
question_responses = ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm fine, how about you?"]

# List of random responses
random_responses = ["Interesting!", "Tell me more.", "I'm not sure, can you elaborate?"]

# Function to return a random response from a list of options
def get_random_response(responses):
    return random.choice(responses)

# Response generation based on user input
def generate_response(user_input):
    user_input = user_input.lower()

    if user_input in greetings:
        return get_random_response(greeting_responses)
    elif user_input in questions:
        return get_random_response(question_responses)
    else:
        return get_random_response(random_responses)

# conversation loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = generate_response(user_input)
    print("Chatbot:", response)

