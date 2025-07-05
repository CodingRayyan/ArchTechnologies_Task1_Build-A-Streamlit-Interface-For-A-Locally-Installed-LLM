import streamlit as st
import requests
import json

st.set_page_config(page_title="Local LLM Chat with Ollama", page_icon="🤖")

st.title("🦙 Local LLM Chatbot (Ollama + Streamlit)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

prompt = st.text_input("Ask your question:", key="user_input")

col1, col2 = st.columns(2)

with col1:
    if st.button("Send", key="send_button"):
        if prompt.strip():
            
            st.session_state.chat_history.append(("You", prompt.strip()))

            
            try:
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={"model": "mistral", "prompt": prompt},
                    stream=True,  
                    timeout=120,
                )

                answer = ""
                
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        try:
                            data = json.loads(line)
                            chunk = data.get("response", "")
                            answer += chunk
                        except Exception:
                            continue  

                if not answer:
                    answer = "No response received."
            except requests.exceptions.RequestException as e:
                answer = f"Error: Could not reach LLM server. {e}"

            
            st.session_state.chat_history.append(("LLM", answer))
        else:
            st.warning("Please enter a question before sending.")

with col2:
    if st.button("Reset Chat", key="reset_button"):
        st.session_state.chat_history = []


st.markdown(
    """
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 700px;
        margin: 0 auto; /* center in page */
    }
    .chat-bubble {
        padding: 12px 16px;
        margin: 6px 0;
        border-radius: 16px;
        max-width: 80%;
        word-wrap: break-word;
        font-size: 16px;
        color: black;
    }
    .user {
        align-self: flex-end;
        background-color: darkgreen; /* red */
    }
    .llm {
        align-self: flex-start;
        background-color: darkgray; /* blue */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.subheader("Conversation History")
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for speaker, text in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f'<div class="chat-bubble user"><strong>You:</strong> {text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bubble llm"><strong>LLM:</strong> {text}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

with st.sidebar.expander("👨‍💻 Developer's Intro"):
    st.markdown("- **IBM Certifed Advanced LLM FineTuner**")
    st.markdown("- **Google Certified Soft Skill Professional**")
    st.markdown("- **Hugging Face Certified in Fundamentals of Large Language Models (LLMs)**")
    st.markdown("- **Have expertise in EDA, ML, Reinforcement Learning, ANN, CNN, CV, RNN, NLP, LLMs.**")
    st.markdown("[💼Visit Rayyan's LinkedIn Profile](https://www.linkedin.com/in/rayyan-ahmed-504725321/)")
    st.markdown("[💼Visit Rayyan's Github Profile](https://github.com/CodingRayyan)")

with st.sidebar.expander("📖 About Project"):
    st.markdown("- **This chatbot is a local LLM interface powered by [Ollama](https://ollama.com/) and Streamlit.**")
    st.markdown("- **It lets you chat with a model running on your own computer — completely private and offline.**")
    st.markdown("- **📝 **Note:** This project is developed as part of an internship at **ArchTechnologies**.**")
    st.markdown("- **[Visit Arch Technologies](https://www.linkedin.com/company/archtechnologiespk/)**")

with st.sidebar.expander("🛠️ Technologies Used"):
    st.markdown("- **Python 3.11.11**")
    st.markdown("- **Streamlit**")
    st.markdown("- **Requests Library**")
    st.markdown("- **Ollama (local LLM server)**")
    st.markdown("- **LLM-Mistral**")
