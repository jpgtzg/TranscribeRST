# Written by Juan Pablo Gutiérrez
# 19 06 2024

import ollama

def get_code(text) -> str :
    prompt = "The following text corresponds to documentation about a certain topic. Convert them into .rst code for sphinx"
    
    prompt = prompt + text
    
    stream = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
    )

    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        
    print('')
    
    return chunk['message']['content']