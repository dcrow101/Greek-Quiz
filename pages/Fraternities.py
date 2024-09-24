import streamlit as st
import random

if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'correct' not in st.session_state:
    st.session_state.correct = ""
if 'fraternities' not in st.session_state:
    st.session_state.fraternities = {
        4: 'Alpha Tau Omega', 5: 'Beta Theta Pi', 6: 'Delta Tau Delta', 
        7: 'Delta Upsilon', 9: 'Phi Kappa Psi', 10: 'Phi Delta Theta', 
        11: 'Phi Kappa Theta', 12: 'Pi Kappa Phi', 13: 'Sigma Alpha Epsilon', 
        14: 'Sigma Chi', 15: 'Sigma Phi Epsilon', 16: 'Theta Xi', 17: 'Triangle',
    }
if 'number' not in st.session_state:
    st.session_state.number = random.choice(list(st.session_state.fraternities.keys()))
if 'input' not in st.session_state:
    st.session_state.input = ""

def get_question():
    return f"What is fraternity number {st.session_state.number}?"

def check_answer(user_answer):
    correct_answer = st.session_state.fraternities[st.session_state.number]
    return user_answer.strip().lower() == correct_answer.lower()

def clear():
    st.session_state.input = st.session_state.widget
    st.session_state.widget = ""

columns = st.columns(2)
with columns[0]:
    st.image("fraternity.png", use_column_width=True)
    st.write("")
with columns[1]:
    st.write(f"Question {st.session_state.current_question + 1}: {get_question()}")
    st.text_input("Your Answer", key="widget", on_change=clear)
    user_input = st.session_state.input

    if st.button("Next Question", key="button1"):
        if check_answer(user_input):
            st.session_state.score += 1
            st.session_state.correct = "🎉 Correct!"
        else:
            st.session_state.correct = f"❌ Incorrect. The correct answer was {st.session_state.fraternities[st.session_state.number]}."
        st.session_state.number = random.choice(list(st.session_state.fraternities.keys()))
        st.session_state.current_question += 1
        st.rerun()

    st.write(f"Score: {st.session_state.score}")
    st.write(st.session_state.correct)
