import streamlit as st

def main():
    st.title("Binary Search: Guess Your Number")
    st.write("Think of a number within the range [1, 100], and I will guess it.")
    st.write("Provide feedback if my guess is 'too low', 'too high', or 'correct'.")

    # Initialize or reset session state variables
    if "low" not in st.session_state:
        st.session_state.low = 1
    if "high" not in st.session_state:
        st.session_state.high = 100
    if "guess" not in st.session_state:
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

    # Display the current guess
    st.write(f"My guess is: **{st.session_state.guess}**")
    
    # Feedback buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Too Low"):
            st.session_state.low = st.session_state.guess + 1
    with col2:
        if st.button("Too High"):
            st.session_state.high = st.session_state.guess - 1
    with col3:
        if st.button("Correct"):
            st.success(f"Yay! I guessed your number: **{st.session_state.guess}**")
            st.balloons()
            reset_game()
            return

    # Update the guess for the next round
    if st.session_state.low <= st.session_state.high:
        st.session_state.guess = (st.session_state.low + st.session_state.high) // 2
    else:
        st.error("Oops! Something went wrong. Did you make a mistake?")

def reset_game():
    """Resets the game to the initial state."""
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = (st.session_state.low + st.session_state.high) // 2

if __name__ == "__main__":
    main()

