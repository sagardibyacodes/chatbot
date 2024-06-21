import streamlit as st
import ollama

class AI_Assistant:
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    def write_message_history(self):
        for msg in st.session_state["messages"]:
            if msg["role"] == "user":
                st.chat_message(msg["role"]).write(msg["content"])
            else:
                st.chat_message(msg["role"]).write(msg["content"])

    def generate_response(self):
        response = ollama.chat(model='llama3', stream=True, messages=st.session_state["messages"])
        for partial_resp in response:
            token = partial_resp["message"]["content"]
            st.session_state["full_message"] += token
            yield token

    def handle_user_input(self):
        if prompt := st.chat_input():
            st.session_state["messages"].append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            st.session_state["full_message"] = ""
            st.chat_message("assistant").write_stream(self.generate_response())
            st.session_state["messages"].append({"role": "assistant", "content": st.session_state["full_message"]})

    def main(self):
        st.title("Project Chat bot version 1.0")
        st.markdown("##")
        self.write_message_history()
        self.handle_user_input()

ai_assistant = AI_Assistant()
ai_assistant.main()
