import streamlit as st

# Initialize session state
if 'low' not in st.session_state:
    st.session_state.low = 1
if 'high' not in st.session_state:
    st.session_state.high = 100
if 'guess' not in st.session_state:
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
if 'done' not in st.session_state:
    st.session_state.done = False

# Title
st.title("Machine Guessing Game")
st.write("Think of a number between 1 and 100. The machine will try to guess it!")

# Display the machine's guess
if not st.session_state.done:
    st.write(f"Is your number **{st.session_state.guess}**?")
else:
    st.write(f"Yay! The machine guessed it right! Your number is **{st.session_state.guess}**.")

# Buttons for user feedback
if not st.session_state.done:
    if st.button("Too Low"):
        st.session_state.low = st.session_state.guess + 1
    elif st.button("Too High"):
        st.session_state.high = st.session_state.guess - 1
    elif st.button("Correct"):
        st.session_state.done = True

    # Update the guess
    if st.session_state.low <= st.session_state.high:
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    else:
        st.write("Hmm, something seems off. Are you sure about your feedback?")

# Reset button
if st.button("Restart"):
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    st.session_state.done = False

