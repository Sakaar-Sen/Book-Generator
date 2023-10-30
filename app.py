import streamlit as st
import bookgen
import pandas as pd
import numpy as np
import time

st.markdown(
    """
    <style>
    .gradient-text {
        background: linear-gradient(45deg, #ff6f61, #ffcd5e);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-size: 50px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="gradient-text">Book Generator</p>', unsafe_allow_html=True)
st.sidebar.title("Navigation")


navigation_options = ["Create New", "Explore", "Tips & Tricks"]
selected_navigation = st.sidebar.selectbox("Select a section", navigation_options)

if selected_navigation == "Create New":
    st.write("Knowledge of any domain at your Fingertips!")

    topic_name = st.text_input("Enter the topic name: ")

    if topic_name:
        s = time.perf_counter()
        st.write("Generating book for topic: ", topic_name)
        st.write("Please be patient as this can take around 30-60 seconds.")
        success = bookgen.main(topic_name)
        if success:
            elapsed = time.perf_counter() - s
            st.write(f"Book generated successfully in {round(elapsed, 2)} seconds. Please download the book by clicking below.")

            topic_name = bookgen.processTopicName(topic_name)
            pdf = open(f"{topic_name}.pdf", "rb").read()

            st.download_button(
                label="Download book",
                data=pdf,
                file_name=f"{topic_name}.pdf",
                mime="application/pdf"
            )
            
            topic_name = ""

        else:
            st.write("Book generation failed. Please try again.")
        
        

    


elif selected_navigation == "Explore":
    st.write("Download books that have already been generated.")
    
    topic_name = "Docker in Computers"
    pdf = open(f"{topic_name}.pdf", "rb").read()
    st.download_button(
    label=f"{topic_name}",
    data=pdf,
    file_name=f"{topic_name}.pdf",
    mime="application/pdf",
    )


    topic_name = "Quantum Computing"
    pdf = open(f"{topic_name}.pdf", "rb").read()
    st.download_button(
    label=f"{topic_name}",
    data=pdf,
    file_name=f"{topic_name}.pdf",
    mime="application/pdf")


    topic_name = "Dark Matter"
    pdf = open(f"{topic_name}.pdf", "rb").read()
    st.download_button(
    label=f"{topic_name}",
    data=pdf,
    file_name=f"{topic_name}.pdf",
    mime="application/pdf")


elif selected_navigation == "Tips & Tricks":
    st.markdown("Tips & Tricks for better results:")
    st.write("1. Add domain in the topic name. For example, instead of Docker, use Docker in Computers")
    st.write("2. Add difficulty level in the topic name. For example, instead of Python, use Python for Beginners or Python for Experts")
    st.write("3. Avoid very lengthy or vague topic names, as they might lead to less relevant content.")
    
