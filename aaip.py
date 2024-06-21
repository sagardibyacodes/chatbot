import streamlit as st
import ollama

class AI_Assistant:
    def main(self):
        st.title("Project Chat bot version 1.0")
        full_transcript = [{"role": "system", "content": "Sagar."}]
        user_input = st.text_input("Ask here:")
        if st.button("Send"):
            full_transcript.append({"role": "user", "content": user_input})
            response = ollama.chat(
                model="llama3",
                messages=full_transcript,
                stream=True,
            )
            full_response = ""
            for chunk in response:
                full_response += chunk['message']['content']
                if chunk['message']['content'].endswith('.'):
                    st.write("Bot:", full_response)
                    full_response = ""

ai_assistant = AI_Assistant()
ai_assistant.main()
