import streamlit as st
import difflib
import google.generativeai as genai

# Configure Gemini API Key
GEMINI_API_KEY = "your-gemini-api-key"  # Replace with your actual Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

# Predefined QnA Data
# Predefined QnA Data
QNA_DATA = {
    "How can I track my order?": "You can track your order in the 'Orders' section of the Zomato app under 'Track Order.'",
    "How long will my order take to be delivered?": "Delivery time depends on the restaurant and location.",
    "My order is delayed. What should I do?": "We apologize for the delay. Please check the 'Track Order' section or contact our delivery partner for updates.",
    "Can I change my delivery address after placing the order?": "Unfortunately, the delivery address cannot be changed once the order is placed.",
    "What happens if the delivery executive can't reach me?": "The delivery partner will try contacting you. If unreachable, the order may be canceled without a refund.",
    "I was charged, but my order was not placed. What should I do?": "If you were charged but did not receive confirmation, the amount will be refunded within 3-5 business days.",
    "How can I get a refund for a canceled order?": "Refunds are processed automatically and credited within 5-7 business days.",
    "My order was incorrect/missing items. What can I do?": "Please report the issue in the 'Help' section within 24 hours, and we will assist you.",
    "Can I get a refund if the food is bad?": "Please raise a complaint with photos in the 'Help' section, and we will investigate the issue.",
    "What payment methods are accepted?": "We accept credit/debit cards, UPI, wallets, and cash on delivery (COD) at select locations.",
    "How can I find vegetarian-only restaurants?": "Use the 'Filters' option and select 'Pure Veg' to find vegetarian restaurants.",
    "Does Zomato have contactless delivery?": "Yes, we offer contactless delivery. Choose 'Leave at Doorstep' during checkout.",
    "How can I check if a restaurant is open?": "Restaurant timings are displayed on their Zomato page under 'Opening Hours.'",
    "Can I place an order in advance?": "Yes! Some restaurants support scheduled orders.",
    "How do I reset my password?": "Go to 'Login,' click 'Forgot Password,' and follow the steps to reset it.",
    "How can I delete my Zomato account?": "You can request account deletion in the 'Account Settings' section. It may take up to 7 days.",
    "What is Zomato Gold / Pro membership?": "Zomato Gold/Pro offers exclusive discounts and benefits.",
    "How can I cancel my Zomato Pro subscription?": "You can cancel Zomato Pro in the 'Subscription' section, but refunds may not be available.",
    "Can I use one Zomato account on multiple devices?": "Yes, but for security reasons, simultaneous orders may not be allowed.",
    "How do I contact Zomato customer support?": "You can reach us through the 'Help' section in the app or visit our website.",
    "Is there a minimum order amount?": "Some restaurants have a minimum order value. This is displayed at checkout.",
    "How can I leave a review for a restaurant?": "You can rate and review restaurants in the 'Rate Your Order' section after your meal.",
    "Can I order from multiple restaurants in one order?": "Currently, you can only order from one restaurant per order.",
    "Does Zomato offer discounts or promo codes?": "Yes! Check the 'Offers' section for available promo codes and discounts.",
    "Can I order food for someone else in a different city?": "Yes! Simply change the delivery location while placing the order.",
    "What happens if the restaurant cancels my order?": "If a restaurant cancels your order, the amount will be refunded automatically.",
    "Can I add special instructions for my order?": "Yes! You can add special instructions in the 'Add a note for the restaurant' section.",
    "How can I apply a promo code?": "You can enter your promo code at checkout under 'Apply Coupon'.",
    "Why isn’t my coupon code working?": "Your coupon may have expired or reached its usage limit.",
    "What are Zomato reward points, and how can I use them?": "Zomato reward points can be earned from orders and redeemed for discounts.",
    "Can I transfer my Zomato Pro benefits to another account?": "No, Zomato Pro benefits are non-transferable.",
    "How does Zomato ensure food quality and hygiene?": "We partner with FSSAI-approved restaurants and conduct regular quality checks.",
    "What should I do if I receive expired or spoiled food?": "Please report the issue immediately in the 'Help' section.",
    "Can I request cutlery or extra condiments with my order?": "Yes! You can request them in the 'Special Instructions' section."
}

# Function to find the best matching question
def get_best_match(user_query):
    questions = list(QNA_DATA.keys())
    match = difflib.get_close_matches(user_query, questions, n=1, cutoff=0.5)
    return match[0] if match else None

# Function to get a short response from Gemini AI
def get_gemini_response(query):
    try:
        model = genai.GenerativeModel("gemini-pro")
        prompt = f"Answer the following user query in a short and concise way (under 30 words): {query}"
        response = model.generate_content(prompt)
        return response.text.strip() if response else "Sorry, I couldn't find an answer."
    except Exception as e:
        return f"Error connecting to Gemini API: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="BiteBot - Zomato Chatbot", page_icon="🍕", layout="wide")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [("bot", "Hello! How can I assist you today? 😊")]

st.markdown("<h1 style='text-align: center; color: #E74C3C;'>🍽️ Welcome to BiteBot! 🍽️</h1>", unsafe_allow_html=True)

st.markdown("<div style='max-width: 800px; margin: auto; padding: 20px;'>", unsafe_allow_html=True)
for role, text in st.session_state.chat_history:
    st.markdown(f"<div style='background-color: {'#E74C3C' if role == 'user' else '#FFD700'}; color: {'white' if role == 'user' else 'black'}; padding: 15px; margin: 10px 0; border-radius: 10px; max-width: 80%; clear: both;'><b>{'You' if role == 'user' else 'BiteBot'}:</b> {text}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Text input for user query
user_query = st.text_input("Type your question:")

if st.button("Send"):
    matched_question = get_best_match(user_query.strip())
    if matched_question:
        response = QNA_DATA[matched_question]
    else:
        response = get_gemini_response(user_query.strip())

    st.session_state.chat_history.append(("user", user_query))
    st.session_state.chat_history.append(("bot", response))
    st.rerun()

st.markdown("<div style='text-align: center; color: gray; font-size: 14px;'>Powered by BiteBot - Your Zomato AI Assistant 🍔</div>", unsafe_allow_html=True)
