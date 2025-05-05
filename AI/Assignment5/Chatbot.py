import gradio as gr
from nltk.chat.util import Chat, reflections

# Define chatbot logic
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you with train booking today?"]],
    [r"i want to book a train", ["Sure! Where would you like to travel from and to?"]],
    [r"from (.) to (.)", ["Great! When would you like to travel from %1 to %2?"]],
    [r"on (.*)", ["Noted. How many tickets would you like to book for %1?"]],
    [r"book (.*) tickets?", ["Got it. %1 tickets booked! You'll receive a confirmation soon."]],
    [r"thank you|thanks", ["You're welcome! Have a safe journey."]],
    [r"quit|bye", ["Goodbye! Have a nice day."]],
    [r"(.*)", ["I'm not sure I understood. Can you please rephrase that?"]],
]

chatbot = Chat(pairs, reflections)

# Define response function
def respond(message, history):
    reply = chatbot.respond(message)
    return reply

# Use ChatInterface for a nice UI
demo = gr.ChatInterface(
    fn=respond,
    title="🚆 Train Booking Bot",
    description="Chat with me to book your train tickets!",
    theme="soft",
)

# Launch the app
demo.launch()