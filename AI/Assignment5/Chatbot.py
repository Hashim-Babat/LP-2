import gradio as gr
from nltk.chat.util import Chat, reflections

# Define chatbot logic with more comprehensive patterns
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you with train booking today?"]],
    [r"i want to book a ticket|book ticket", ["Sure! Where would you like to travel from and to?"]],
    [r"from (.*) to (.*)", ["Great! When would you like to travel from %1 to %2?"]],
    [r"on (.*)", ["Noted. How many tickets would you like to book for %1?"]],
    [r"book (.*) tickets?", ["Got it. %1 tickets booked! You'll receive a confirmation soon."]],
    [r"what is the train schedule from (.*) to (.*)", ["You can check the train schedule on the official IRCTC site or mobile app."]],
    [r"is there any train available from (.*) to (.*)", ["Yes, multiple trains are available daily. Would you like me to list some?"]],
    [r"what is the fare from (.*) to (.*)", ["The fare varies based on class and train type. Please check the fare calculator on the IRCTC website."]],
    [r"i want to cancel my ticket", ["Sure. Please provide your PNR number for cancellation."]],
    [r"my pnr number is (.*)", ["Your cancellation request for PNR %1 has been received. Refund will be processed shortly."]],
    [r"what is the status of my booking", ["Please provide your PNR number to check your booking status."]],
    [r"how can i make payment", ["You can pay using UPI, Net Banking, Credit/Debit Card, or IRCTC wallet."]],
    [r"what are the available payment options", ["We support UPI, Net Banking, Cards, and Wallets."]],
    [r"can i choose my seat", ["Yes, you can choose your seat during the booking process if available."]],
    [r"i want a window seat", ["We'll try our best to allocate a window seat based on availability."]],
    [r"can i book for someone else", ["Yes, you can book tickets for others. Just provide their details during booking."]],
    [r"how can i get a refund", ["Refunds are processed back to the original payment method within 5-7 business days."]],
    [r"what documents are required during travel", ["You need a valid ID proof like Aadhar, PAN, or Driving License along with your ticket."]],
    [r"thank you|thanks", ["You're welcome! Have a safe journey."]],
    [r"quit|bye", ["Goodbye! Have a nice day."]],
    [r"(.*)", ["I'm not sure I understood. Can you please rephrase that or ask something else related to train booking?"]],
]

chatbot = Chat(pairs, reflections)

# Define response function
def respond(message, history):
    reply = chatbot.respond(message)
    return reply

# Use ChatInterface for a nice UI
demo = gr.ChatInterface(
    fn=respond,
    title="Train Booking Bot",
    description="Chat with me to book your train tickets!",
    theme="soft",
)

# Launch the app
demo.launch()
