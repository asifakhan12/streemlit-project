import streamlit as st

# Custom Python questions
python_questions = [
    {"question": "1: What keyword is used to define a function in Python?", "correct_answer": "def", "incorrect_answers": ["function", "define", "func"]},
    {"question": "2: Which of the following data types is **immutable** in Python?", "correct_answer": "Tuple", "incorrect_answers": ["List", "Dictionary", "Set"]},
    {"question": "3: What will `len([1, 2, 3, 4])` return?", "correct_answer": "4", "incorrect_answers": ["3", "5", "None"]},
    {"question": "4: Which loop is used when the number of iterations is unknown?", "correct_answer": "while", "incorrect_answers": ["for", "do-while", "loop"]},
    {"question": "5: What is the correct way to open a file in Python?", "correct_answer": "open('file.txt', 'r')", "incorrect_answers": ["open_file('file.txt')", "file.open('file.txt')", "read('file.txt')"]},
    {"question": "6: Which keyword is used to handle exceptions in Python?", "correct_answer": "try", "incorrect_answers": ["catch", "except", "finally"]},
    {"question": "7: Which function is used to get the length of a string?", "correct_answer": "len()", "incorrect_answers": ["size()", "count()", "length()"]},
    {"question": "8: How do you start a comment in Python?", "correct_answer": "hashTag", "incorrect_answers": ["//", "/*", "--"]},
    {"question": "9: What will `5 // 2` return?", "correct_answer": "2", "incorrect_answers": ["2.5", "3", "2.0"]},
    {"question": "10: Which module is used for working with JSON in Python?", "correct_answer": "json", "incorrect_answers": ["pickle", "csv", "os"]},
    {"question": "11: What is the output of `bool([])`?", "correct_answer": "False", "incorrect_answers": ["True", "None", "Error"]},
    {"question": "12: Which method is used to remove the last item from a list?", "correct_answer": "pop()", "incorrect_answers": ["remove()", "delete()", "discard()"]},
    {"question": "13: How do you create an empty dictionary?", "correct_answer": "{}", "incorrect_answers": ["[]", "()", "None"]},
    {"question": "14: Which keyword is used to return a value from a function?", "correct_answer": "return", "incorrect_answers": ["yield", "break", "continue"]},
    {"question": "15: What will `type(10.5)` return?", "correct_answer": "float", "incorrect_answers": ["int", "double", "decimal"]},
    {"question": "16: Which built-in function is used to convert a string to lowercase?", "correct_answer": "lower()", "incorrect_answers": ["downcase()", "small()", "tolowercase()"]},
    {"question": "17: Which keyword is used to create a class in Python?", "correct_answer": "class", "incorrect_answers": ["struct", "object", "define"]},
    {"question": "18: Which operator is used for exponentiation?", "correct_answer": "**", "incorrect_answers": ["^", "//", "$"]},
    {"question": "19: Which function is used to get user input in Python?", "correct_answer": "input()", "incorrect_answers": ["scan()", "read()", "get()"]},
    {"question": "20: What is the default value of an uninitialized variable in Python?", "correct_answer": "None", "incorrect_answers": ["0", "Undefined", "Empty String"]}
]

# Streamlit app
st.set_page_config(page_title="Python Quiz App", page_icon="🐍", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🐍 Python Quiz Challenge 🏆</h1>
""", unsafe_allow_html=True)

# Initialize session state variables
if "questions" not in st.session_state:
    st.session_state.questions = python_questions
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.submitted = False
    st.session_state.selected_answer = None

# Check if quiz is finished
if st.session_state.current_question >= len(st.session_state.questions):
    st.markdown(f"""
        <h2 style='text-align: center; color: #27AE60;'>🎉 Quiz Completed! 🎉</h2>
        <h3 style='text-align: center; color: #F39C12;'>Your Final Score: {st.session_state.score}/{len(st.session_state.questions)}</h3>
    """, unsafe_allow_html=True)
    if st.button("Restart Quiz", key="restart"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.submitted = False
        st.session_state.selected_answer = None
        st.rerun()
    st.stop()

# Get current question
question_data = st.session_state.questions[st.session_state.current_question]

st.markdown(f"<h2 style='color: #D35400;'>{question_data['question']}</h2>", unsafe_allow_html=True)
options = question_data["incorrect_answers"] + [question_data["correct_answer"]]
options.sort()

selected_answer = st.radio("Select an answer:", options, index=None, key=f"question_{st.session_state.current_question}")

# Submit Button
if st.button("Submit", key="submit"):
    if selected_answer is None:
        st.warning("⚠️ Please select an answer before submitting.")
    else:
        st.session_state.submitted = True
        st.session_state.selected_answer = selected_answer
        if selected_answer == question_data["correct_answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! The correct answer is {question_data['correct_answer']}")

# Show Next Button only if answer is submitted
if st.session_state.submitted and st.session_state.selected_answer is not None:
    if st.button("Next Question ➡️", key="next"):
        st.session_state.current_question += 1
        st.session_state.submitted = False
        st.session_state.selected_answer = None
        st.rerun()



