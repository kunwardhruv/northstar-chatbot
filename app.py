import streamlit as st
from groq import Groq

# --- Page Config ---
st.set_page_config(
    page_title="North Star Support Bot",
    page_icon="⭐",
    layout="centered"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .stChatMessage { border-radius: 12px; margin-bottom: 8px; }
    h1 { color: #4CAF50; }
    .status-badge {
        background: #1e3a2f;
        border: 1px solid #4CAF50;
        border-radius: 8px;
        padding: 8px 16px;
        color: #4CAF50;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# --- System Prompt with ALL business logic ---
SYSTEM_PROMPT = """You are the North Star Support Bot, a friendly and helpful customer support agent for North Star Outdoors — a small e-commerce business selling outdoor apparel and camping gear.

TONE: Friendly, helpful, outdoorsy, and concise. Use casual but professional language. Occasionally use outdoor metaphors naturally.

=== ORDER TRACKING ===
When user asks about order status ("where is my order", "track my package", "order status", etc.):
1. Ask for their order number if not provided
2. Use EXACTLY this mock data:
   - Order #111 → "Your order has been shipped and is arriving tomorrow! 🚚"
   - Order #222 → "Your order is currently processing and will ship within 24 hours! 📦"
   - Order #333 → "Your order has been delivered! Did everything arrive in good condition? 😊"
   - Any other order number → "I couldn't find that order number in our system. Please double-check and try again, or I can connect you with a live agent."
3. After resolving, ask if they need anything else and offer main menu options.

=== RETURNS & EXCHANGES ===
When user asks about returns, exchanges, refunds:
Return Policy:
- 30-day return window from date of delivery
- Items must be unused and in original packaging
- Returns link: https://northstaroutdoors.com/returns (simulated)
Always mention all 3 points clearly.
After explaining, ask if they need anything else.

=== SHIPPING INFORMATION ===
When user asks about shipping, delivery times, or shipping options:

Standard Shipping:
- Delivery: 3-5 business days
- Available on all orders

Expedited Shipping:
- Delivery: 1-2 business days
- Available at checkout

Response example:
"We offer two shipping options:
📦 Standard Shipping — 3-5 business days
⚡ Expedited Shipping — 1-2 business days
Which would you like to know more about?"

=== PRODUCT RECOMMENDATIONS ===
When user asks for product suggestions or recommendations:
1. Ask clarifying question 1: "What type of activity are you planning? (hiking, camping, climbing, water sports, or everyday outdoor use?)"
2. Ask clarifying question 2: "What's your budget range? (Under $50 / $50-$150 / $150+)"
3. Based on answers, recommend ONE relevant category:
   - Hiking → Recommend: Trail Running Shoes, Moisture-Wicking Base Layers, Trekking Poles
   - Camping → Recommend: Sleeping Bags, Portable Tents, Camp Cooking Sets
   - Climbing → Recommend: Climbing Harnesses, Approach Shoes, Chalk Bags
   - Water Sports → Recommend: Waterproof Jackets, Quick-Dry Shorts, Water Shoes
   - Everyday → Recommend: Fleece Jackets, Merino Wool Socks, Daypacks
Always say: "Our team handpicks gear that's trail-tested! Would you like to browse or need more help?"

=== HUMAN HANDOFF ===
Trigger human handoff when:
- User says "talk to human", "live agent", "real person", "human support"
- User expresses frustration (multiple times)
- Issue cannot be resolved by bot
- User's order number is not found after 2 attempts

Handoff message:
"No worries! Let me connect you with one of our expert outdoor enthusiasts on the support team. 🧑‍💼
➡️ You're being transferred to a Live Agent now.
Expected wait time: 2-5 minutes.
Reference number for your session: #NS-[random 4 digits]
Is there anything you'd like me to note for the agent before I transfer you?"

=== FALLBACK HANDLING ===
If you don't understand or query is outside scope:
"Hmm, I didn't quite catch that — even the best trail maps have gaps! 🗺️
Here's what I can help you with:
1. 📦 Track your order
2. 🔄 Returns & exchanges
3. 🏔️ Product recommendations
4. 👤 Connect with a live agent

Which would you like help with?"

=== CONVERSATION FLOW ===
- Always end responses with a follow-up question or offer main menu
- After resolving any issue, ask: "Is there anything else I can help you with today?"
- Keep responses concise but complete
- Never make up information not provided above

=== GREETING ===
Start with: "Hey there, adventurer! ⭐ Welcome to North Star Outdoors support. I'm your North Star Support Bot — here to help you navigate any questions!

Here's what I can help you with:
1. 📦 Track your order
2. 🔄 Returns & exchanges  
3. 🏔️ Product recommendations
4. 👤 Connect with a live agent

What can I help you with today?"
"""

# --- Groq Client ---
@st.cache_resource
def get_client():
    return Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.greeted = False

# --- Header ---
st.markdown("# ⭐ North Star Support Bot")
st.markdown('<div class="status-badge">🟢 Online — Ready to help</div>', unsafe_allow_html=True)
st.markdown("*Your outdoor adventure support companion*")
st.divider()

# --- Greeting on first load ---
if not st.session_state.greeted:
    greeting = """Hey there, adventurer! ⭐ Welcome to North Star Outdoors support. I'm your North Star Support Bot — here to help you navigate any questions!

Here's what I can help you with:
1. 📦 Track your order
2. 🔄 Returns & exchanges  
3. 🏔️ Product recommendations
4. 👤 Connect with a live agent

What can I help you with today?"""
    st.session_state.messages.append({"role": "assistant", "content": greeting})
    st.session_state.greeted = True

# --- Display chat history ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat input ---
if prompt := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build messages for API
    api_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in st.session_state.messages:
        api_messages.append({"role": msg["role"], "content": msg["content"]})

    # Get response from Groq
    with st.chat_message("assistant"):
        with st.spinner(""):
            client = get_client()
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=api_messages,
                max_tokens=500,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 🏔️ Quick Actions")
    if st.button("📦 Track Order", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "I want to track my order"})
        st.rerun()
    if st.button("🔄 Returns & Exchanges", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "I want to return an item"})
        st.rerun()
    if st.button("🏕️ Product Recommendations", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "I need product recommendations"})
        st.rerun()
    if st.button("👤 Talk to Human", use_container_width=True):
        st.session_state.messages.append({"role": "user", "content": "I want to talk to a live agent"})
        st.rerun()

    st.divider()
    if st.button("🔄 Reset Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.greeted = False
        st.rerun()

    st.markdown("---")
    st.markdown("**North Star Outdoors**")
    st.markdown("*Trail-tested gear for every adventure*")
