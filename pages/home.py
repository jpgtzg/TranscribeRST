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
        
            st.code("""Introduction
-------------

Java is a high-level multi-paradigm programming language famous for its ability to compile to platform independent bytecode. It was designed by James Gosling in 1990 at Sun Microsystems.

History
--------

One of Java's first demonstrations was the Star 7 PDA, which gave birth to the Jawa mascot, Duke. Today, it's one of the world's most popular programming languages. It powers enterprise web apps with Spring framework, big data pipelines with Hadoop, mobile apps on Android, and even things like the controller for NASA's Maestro Mars Rover.

What is Java?
-------------

Java compiles to bytecode that can run on any operating system without recompiling, which is made possible by executing the code with the Java Virtual Machine (JVM) or JVM. It's both a compiled and interpreted language at the same time.

Key Features
--------------

* Strongly typed language
* Curly brace syntax similar to C family
* Provides high-level features like garbage collection, runtime type checking, and reflection

Getting Started
-----------------

To get started with Java, install the Java Development Kit (JDK) and create a file ending in `.java`. Every Java program starts with a class name, which should also match the file name. The class is required to have a `main` method.

Example Code
--------------

```
class MyFirstJavaProgram {
    public static void main(String[] args) {
        int myVariable = 10;
        System.out.println("The value of myVariable is: " + myVariable);
    }
}
```

In this example, we define a class `MyFirstJavaProgram` with a `main` method. Inside the `main` method, we define a variable `myVariable` and print it to the standard output using the `System.out.println()` method.

Defining Functions
-------------------

Functions in Java are called methods. The `public` keyword means that it can be used outside of this class. And `static` means that it's a member of the class itself, as opposed to an instance of the class.

Example Code (continued)
-------------------------

```
class MyFirstJavaProgram {
    public static void main(String[] args) {
        int myVariable = 10;
        System.out.println("The value of myVariable is: " + myVariable);

        public static void printHelloWorld() {
            System.out.println("Hello, World!");
        }
    }
}
```

In this example, we define a method `printHelloWorld()` that prints "Hello, World!" to the standard output.

Defining Custom Classes
-------------------------

Custom classes in Java are blueprints for objects. We can add attributes and methods to them using the `new` keyword to instantiate an object from the class.

Example Code (continued)
-------------------------

```
class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void printInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person("John", 30);
        person.printInfo();
    }
}
```

In this example, we define a custom class `Person` with attributes and methods. We then instantiate an object from the class using the `new` keyword and call its method.

Conclusion
----------

Congratulations! You just built an enterprise-grade application using Java. This has been Java in 100 seconds. It's subscribed for more short videos like this, and if we somehow get to 100,000 likes on this video, I'll do a full Java tutorial. Thanks for watching, and I will see you in the next one.""")

home()
upload() 
        
st.write("Credits: Juan Pablo Gutiérrez, 2024")
