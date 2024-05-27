import google.generativeai as genai
import streamlit as st
def geminiFunction(system_prompt, user_prompt):
  gemini_api_key = str("AIzaSyCLzRcf5YrMmul3VDgaqoWX285t__q3A8w")
  genai.configure(api_key = gemini_api_key)
  model = genai.GenerativeModel("gemini-pro")
  chat_complition = model.generate_content([system_prompt, user_prompt])
  response = chat_complition.text
  return response
system_prompt = f"""Share your response in case study writing format. Format is given below. \
\n\nFormat Style:\n
1) Introduction :\n
2) About:\n
3) Pros:atleast mandatorily give one pros\n
4) Cons:\n
5) How to avoid cons:\n
6) Conclusion:\n
7) Helpful Suggestions:\n
8) Helpful Websites:\n
"""
user_prompt = st.text_input("Enter your querry here.")

if user_prompt:
  response = geminiFunction(system_prompt, user_prompt)
  st.write(response)