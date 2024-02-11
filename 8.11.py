def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

# Create a list containing short text messages
text_messages = [
    "How are you doing???",
    "Don't forget to get our groceries!",
    "I'm on my way!!"
]

# Create an empty list to store sent messages
sent_messages = []

# Call the send_messages() function with a copy of the original list
send_messages(text_messages[:], sent_messages)

# Print both lists to verify the original list has retained its messages
print("\nOriginal Messages:")
show_messages(text_messages)
print("\nSent Messages:")
show_messages(sent_messages)
