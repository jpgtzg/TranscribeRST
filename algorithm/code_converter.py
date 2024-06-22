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
    
    # Initialize an empty list to collect the chunks
    collected_text = []
    
    for chunk in stream:
        # Collect each chunk in the list
        collected_text.append(chunk['message']['content'])
        print(chunk['message']['content'], end='', flush=True)
        
    print('')
    
    # Join the collected chunks into a single string and return it
    return ''.join(collected_text)