# Written by Juan Pablo Gutiérrez
# 19 06 2024

from openai import OpenAI
import streamlit as st
client = OpenAI(api_key=st.secrets["OPENAI"]["OPENAI_API_KEY"])

def get_code(text) -> str :
    prompt = "The following text corresponds to documentation about a certain topic. Convert them into .rst code for sphinx"
    
    prompt = prompt + text
    
    result = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a documentation code converter. The following text corresponds to documentation about a certain topic. Convert them into .rst code for sphinx."},
            {'role' : 'user' , 'content' : prompt}
        ],
    )

    return result.choices[0].message.content