# ⭐ North Star Support Bot

> AI-powered customer support chatbot for North Star Outdoors — an e-commerce business specializing in outdoor apparel and camping gear.

Built for the **Upwork Talent Accelerator: AI Chatbot Developer** simulated project.

🎥 **[Demo Video](https://drive.google.com/file/d/1Pz8_n_RKI-LPpWFx7GJoqR-NqMKDMnNS/view?usp=sharing)** ← *(link update coming soon)* 

---

## 🚀 Features

| Feature | Description |
|---|---|
| 📦 Order Tracking | Handles orders #111, #222, #333 with real-time simulated statuses |
| 🔄 Returns & Exchanges | Explains 30-day return policy with direct returns link |
| 🏔️ Product Recommendations | 2-step clarification flow → personalized category recommendation |
| 👤 Human Handoff | Smooth transfer to Live Agent with session reference number |
| ❓ Fallback Handling | Clear "didn't understand" response + guided menu options |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Groq Llama 3.3 70B |
| Language | Python 3.10+ |
| API | Groq API (free tier) |

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/kunwardhruv/northstar-chatbot
cd northstar-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
> ⚠️ Get your free API key instantly at [console.groq.com](https://console.groq.com) — no credit card required.

### 4. Run the app
```bash
streamlit run app.py
```

---

## 🖼️ Screenshots

### Welcome Message
![Welcome Message](https://github.com/user-attachments/assets/3adf5d95-cb4d-40ab-9675-68e051f0ad01)


---

### 📦 Order Tracking
```
User: "Where is my order?" / "Track my package"
→ Bot asks for order number
→ Try: 111, 222, 333, or any invalid number
```
![Order Tracking](https://github.com/user-attachments/assets/d794e264-e4ea-4580-866b-612d5080ab93)


---

### 🔄 Returns & Exchanges
```
User: "I want to return an item" / "How do I exchange a product?"
→ Bot explains 30-day return policy + provides returns link
```
![Returns and Exchanges](https://github.com/user-attachments/assets/ac1ae10b-d7e8-4e56-b334-a218eb4b10ed)


---

### 🏔️ Product Recommendations
```
User: "I need product recommendations" / "What gear for hiking?"
→ Bot asks activity type → asks budget → recommends category
```
![Product Recommendations](https://github.com/user-attachments/assets/46cab4b9-4a39-4217-a4ec-1abdf8f6ac80)
)

---

### 👤 Human Handoff
```
User: "Talk to a real person" / "Connect me to a live agent"
→ Bot transfers to Live Agent + generates session reference number
```
![Human Handoff](https://github.com/user-attachments/assets/90a81dc1-f7d9-4798-be4f-a43a12424012)


---

### ❓ Fallback Handling
```
User: "blah blah random" / "Do you sell cars?"
→ Bot responds with "didn't understand" + shows main menu
```
![Fallback Handling](https://github.com/user-attachments/assets/ba17b5a9-f5bc-44d0-890d-277ce0e7aefa)


---

## 📋 Mock Data Reference

| Order # | Status |
|---|---|
| #111 | ✅ Shipped — arriving tomorrow |
| #222 | 🔄 Processing — ships within 24 hours |
| #333 | 📬 Delivered — follow-up offered |
| Any other | ❌ Invalid — not found in system |

**Return Policy:** 30-day returns · Unused items · Original packaging required  
**Shipping:** Standard 3–5 days · Expedited 1–2 days

---

## 📁 Project Structure

```
northstar-chatbot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .streamlit/
    └── secrets.toml        # API keys (not committed to Git)
```

---

## 👨‍💻 Built By

**Dhruv Singh**  
B.Tech AI & Data Science — GGSIPU Delhi (CGPA 9.1)  
GitHub: [kunwardhruv](https://github.com/kunwardhruv) · [LinkedIn](https://linkedin.com/in/dhruv-singh-24nov2004)
