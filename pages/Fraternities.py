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
        4: ['Alpha Tau Omega', 'ATO'], 
        5: ['Beta Theta Pi', 'Beta'], 
        6: ['Delta Tau Delta', 'Delts'], 
        7: ['Delta Upsilon', 'DU'], 
        9: ['Phi Kappa Psi', 'Phi Psi'], 
        10: ['Phi Delta Theta', 'Phi Delt'], 
        11: ['Phi Kappa Theta', 'Phi Kap'], 
        12: ['Pi Kappa Phi', 'Pi Kap'], 
        13: ['Sigma Alpha Epsilon', 'SAE'], 
        14: ['Sigma Chi', 'Sig Chi'], 
        15: ['Sigma Phi Epsilon', 'Sig Ep'], 
        16: ['Theta Xi', 'Theta X'], 
        17: ['Triangle']
    }
if 'question_pool' not in st.session_state:
    st.session_state.question_pool = list(st.session_state.fraternities.keys())
    random.shuffle(st.session_state.question_pool)
if 'number' not in st.session_state:
    st.session_state.number = st.session_state.question_pool.pop()
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
        
        # Get next question
        if not st.session_state.question_pool:
            st.session_state.question_pool = list(st.session_state.fraternities.keys())
            random.shuffle(st.session_state.question_pool)
        
        st.session_state.number = st.session_state.question_pool.pop()
        st.session_state.current_question += 1
        st.rerun()

    st.write(f"Score: {st.session_state.score}")
    st.write(st.session_state.correct)