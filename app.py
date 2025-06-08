import streamlit as st
import requests

st.set_page_config(page_title="Joy – Client Coach", page_icon="😊")

st.markdown("### 😊 Meet Joy – Your Client Coach & Credit Cheerleader")
st.markdown("""
**Role Title:** Client Coach  
**Name:** Joy  
**Mission:** Joy inspires and educates your clients throughout their credit journey—offering helpful tips, motivational messages, and strategies for building long-term credit success.

---

🎯 **Joy’s Top Responsibilities**

**Client Motivation**  
- Cheer clients on through ups and downs  
- Celebrate wins and progress  
- Provide words of encouragement during setbacks  

**Credit Education**  
- Teach smart credit habits  
- Explain how credit scores work  
- Offer realistic ways to improve credit daily  

**Positive Reinforcement**  
- Send reminders to stay consistent  
- Highlight credit milestones  
- Reinforce the importance of patience and effort  

---

🛠️ **Joy’s Toolbox**  
- Credit tip guides  
- Encouraging message templates  
- Educational worksheets  
- SMS/email check-in scripts  

---

💬 **Motto:**  
**Joy keeps your clients inspired, informed, and moving forward—one credit win at a time!**
""")

user_question = st.text_input("💬 Ask Joy a question about motivation, credit habits, or support:")

def query_ollama(prompt):
    full_prompt = f"You are Joy, a warm and encouraging Client Coach for a credit repair company. Answer client questions with positivity, practical advice, and gentle guidance. Keep it friendly and supportive.\n\nQuestion: {prompt}\n\nAnswer:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Sorry, Joy is taking a little break right now."

if user_question:
    with st.spinner("Joy is thinking..."):
        answer = query_ollama(user_question)
        st.markdown(f"**Joy's Answer:**\n\n{answer}")

