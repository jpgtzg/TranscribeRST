# Written by Juan Pablo Gutiérrez
# 26 05 2024

import assemblyai as aai
import ollama

def get_topics(text) -> str : 
    prompt = "The following text corresponds to an explanation in a specific area. Do not summarize it, but rather divide the text into topics and subtopics"
    
    prompt = prompt + text
    
    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)