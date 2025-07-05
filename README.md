# ArchTechnologies_Task1_Build-A-Streamlit-Interface-For-A-Locally-Installed-LLM
Ollama | Mistral 7b | Streamlit | Requests Library | Python 3.11.11

### Prepared By: Rayyan Ahmed - [My Linkedin Profile](https://www.linkedin.com/in/rayyan-ahmed-504725321/)

# 🦙 Local LLM Chatbot (Ollama + Streamlit)

This is a **local chatbot interface** built with [Streamlit](https://streamlit.io/) and [Ollama](https://ollama.com/). It allows you to chat with large language models (LLMs) like Mistral, running directly on your own computer — completely private and offline!

---

## 👨‍💻 Developer

This project is developed by **Your Name Here** as part of an internship at **ArchTechnologies**.  
I am passionate about artificial intelligence, building practical AI solutions, and bringing privacy-focused tools to end users.

---

## 📖 About the Project

This chatbot provides a secure, offline conversational interface with large language models hosted locally on your hardware.  
It features:
- A **chat-like interface** with user messages right-aligned and model responses left-aligned.
- A **conversation history panel** to review past interactions.
- A **sidebar** with information about the developer, project purpose, and technologies used.
- A **reset chat** feature for clearing conversations instantly.

This project demonstrates how to integrate a local LLM (running with Ollama) into a user-friendly Streamlit web app.

---

## 🛠️ Technologies Used

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – framework for building interactive data apps
- [Requests](https://docs.python-requests.org/) – HTTP library for Python
- [Ollama](https://ollama.com/) – local LLM server to run models privately

---

## 🚀 Installation & Running

1. Clone this repo:
   ```git clone https://github.com/CodingRayyan/ArchTechnologies_Task1_Build-A-Streamlit-Interface-For-A-Locally-Installed-LLM.git
   cd ArchTechnologies_Task1_Build-A-Streamlit-Interface-For-A-Locally-Installed-LLM

ollama pull mistral

ollama serve

streamlit run app.py


