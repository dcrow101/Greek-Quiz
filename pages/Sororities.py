import streamlit as st
import random

if 'current_question2' not in st.session_state:
    st.session_state.current_question2 = 0
if 'score2' not in st.session_state:
    st.session_state.score2 = 0
if 'correct2' not in st.session_state:
    st.session_state.correct2 = ""
if 'sororities' not in st.session_state:
    st.session_state.sororities = {
        1: 'Alpha Chi Omega', 2: 'Alpha Omicron Pi', 3: 'Alpha Phi', 
        4: 'Alpha Xi Delta', 5: 'Chi Omega', 6: 'Delta Delta Delta', 
        7: 'Delta Gamma', 8: 'Gamma Phi Beta', 9: 'Kappa Alpha Theta', 
        10: 'Kappa Delta', 11: 'Kappa Kappa Gamma', 12: 'Phi Mu', 
        13: 'Pi Beta Phi',
    }
if 'number2' not in st.session_state:
    st.session_state.number2 = random.choice(list(st.session_state.sororities.keys()))
if 'input2' not in st.session_state:
    st.session_state.input2 = ""

def get_question():
    return f"What is sorority number {st.session_state.number2}?"

def check_answer(user_answer):
    correct_answer = st.session_state.sororities[st.session_state.number2]
    return user_answer.strip().lower() == correct_answer.lower()

def clear():
    st.session_state.input2 = st.session_state.widget2
    st.session_state.widget2 = ""

columns = st.columns(2)
with columns[0]:
    st.image("sorority.png", use_column_width=True)
    st.write("")
with columns[1]:
    st.write(f"Question {st.session_state.current_question2 + 1}: {get_question()}")
    st.text_input("Your Answer", key="widget2", on_change=clear)
    user_input = st.session_state.input2

    if st.button("Next Question", key="button2"):
        if check_answer(user_input):
            st.session_state.score2 += 1
            st.session_state.correct2 = "🎉 Correct!"
        else:
            st.session_state.correct2 = f"❌ Incorrect. The correct answer was {st.session_state.sororities[st.session_state.number2]}."
        st.session_state.number2 = random.choice(list(st.session_state.sororities.keys()))
        st.session_state.current_question2 += 1
        st.rerun()

    st.write(f"Score: {st.session_state.score2}")
    st.write(st.session_state.correct2)
