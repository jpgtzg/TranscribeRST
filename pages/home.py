# Written by Juan Pablo Gutiérrez
# 20 06 2024

import streamlit as st
import sys
from pathlib import Path
import time as t

sys.path.append(str(Path(__file__).resolve().parent.parent))

#from algorithm import audio, code_converter

def __init__ ():
    st.set_page_config(page_title="AI Docs", page_icon="🧠")
    pass

st.title("AI Docs")

def home(): 
    st.write("""Welcome to AI Docs! 
            This is a platform where you can upload lecture or meeting recordings to get 
            documentation code in *.rst* fie format for you Sphinx projects, enhancing the 
            overall documentation-making process and achieving a more efficient workflow.""")

def upload() : 
    st.write ("To get started, upload an audio file in *.mp3* format and click the 'Transcribe' button.")

    uploaded_file = st.file_uploader("Choose a file", type=['mp3'])
    transcribe_button = st.button("Transcribe")

    if uploaded_file and transcribe_button: 
        st.write("Transcribing..")
        
        t.sleep(3)
        
        #code = code_converter.get_code(audio.get_transcription(uploaded_file))
        with st.container(border=True): 
        
            st.write("Code: ")
        
            st.code("""Java
    =====================================

    Java: A High-Level Programming Language
    -----------------------------------------

    Java is a high-level multi-paradigm programming language famous for its ability to compile to platform-independent bytecode. It was designed by James Gosling in 1990 at Sun Microsystems.

    History
    -------

    One of Java's first demonstrations was the Star 7 PDA, which gave birth to the Java mascot, Duke. Today, it's one of the world's most popular programming languages. It powers enterprise web apps with Spring framework, big data pipelines with Hadoop, mobile apps on Android, and even things like the controller for NASA's Maestro Mars Rover.

    Innovations
    ------------

    What made Java innovative is that instead of compiling to machine code like C or C++, it compiles to bytecode that can run on any operating system without recompiling. This is made possible by executing the code with the Java Virtual Machine (JVM). It's both a compiled and interpreted language at the same time.

    Language Features
    -----------------

    * Strongly typed language with curly brace syntax similar to the C family.
    * Provides high-level features like garbage collection, runtime type checking, and reflection.

    Getting Started
    ---------------

    To get started, install the Java Development Kit (JDK). Then create a file ending in `.java`. Every Java program starts with a class name, which should also match the file name. The class is required to have a `main` method, where your code will start executing.

    Basic Syntax
    -------------

    * Define a variable by starting with a type, followed by a name and value.
    * Print it to the standard output using the built-in system class.
    * Define functions (methods) on the class. The `public` keyword means that it can be used outside of this class. The `static` keyword means that it's a member of the class itself.

    Object-Oriented Programming
    ----------------------------

    * Define custom classes, which are blueprints for objects.
    * Add attributes and methods to them.
    * Use the `new` keyword to instantiate an object from the class.

    Functional Programming
    ----------------------

    * Supports functional patterns like anonymous lambda methods.

    Compiling and Running
    --------------------

    * Compile your program using the compiler to generate a `.class` file, which contains the bytecode.
    * Use the Java command to tell the JVM to interpret and run that file.

    Conclusion
    ----------

    Congratulations! You just built an enterprise-grade application. This has been Java in 100 seconds. It's subscribed for more short videos like this, and if we somehow get to 100,000 likes on this video, I'll do a full Java tutorial.""")

home()
upload() 
        
st.write("Source code: [GitHub](https://github.com/jpgtzg/AIDocs)")
st.write("Credits: Juan Pablo Gutiérrez, 2024")
