# Written by Juan Pablo Gutiérrez
# 19 06 2024

from openai import OpenAI
import streamlit as st
client = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])

def get_code(text, user_context) -> str :
    prompt = f'The following text corresponds to documentation about a certain topic. Convert them into .rst code for sphinx: \n\n {text}'
    
    if user_context:
        prompt = f"Context: {user_context}\n\n" + prompt
    
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a documentation code converter. The following text corresponds to documentation about a certain topic. Convert them into .rst code for sphinx."},
            {'role' : 'user' , 'content' : prompt}
        ],
    )

    return result.choices[0].message.content