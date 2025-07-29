import streamlit as st
import time

def app():
    # --- PAGE CONFIG ---
    # (Optional) Set page configuration. This should be the first Streamlit command.
    # st.set_page_config(page_title="Abhi's Birthday Surprise", layout="wide")

    # --- STYLING (CSS) ---
    # This block contains all the CSS for styling the page elements.
    st.markdown("""
    <style>
    /* Import a Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Keyframes for animations */
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #1a73e8, 0 0 12px #1a73e8, 0 0 15px #1a73e8; }
        50% { text-shadow: 0 0 15px #4285f4, 0 0 20px #4285f4, 0 0 25px #4285f4; }
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Main title styling */
    h1 {
        font-family: 'Poppins', sans-serif;
        text-align: center;
        color: #e0e0e0;
        animation: glow 3s ease-in-out infinite;
    }

    /* Styling for the main content cards (login and welcome) */
    .card {
        background: rgba(40, 40, 60, 0.6); /* Semi-transparent background */
        backdrop-filter: blur(10px); /* Frosted glass effect */
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        width: 100%;
        max-width: 500px;
        margin: auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Custom button styling */
    .stButton > button {
        background-color: #1a73e8;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s ease;
        display: block;
        margin: 1rem auto 0 auto; /* Center the button */
    }

    .stButton > button:hover {
        background-color: #4285f4;
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(66, 133, 244, 0.6);
    }
    
    /* Styling for the note inside the welcome card */
    .note-container {
        background-color: rgba(0, 0, 0, 0.2);
        border-left: 5px solid #4285f4;
        padding: 15px;
        margin: 20px 0;
        border-radius: 8px;
        font-style: italic;
        color: #d0d0d0;
        line-height: 1.6;
    }
    
    /* Center text inputs */
    .stTextInput {
        text-align: center;
    }

    </style>
    """, unsafe_allow_html=True)

    st.title("A Special Surprise for You 🎂")

    # --- Session State Initialization ---
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = None

    # --- Logged-in View ---
    if st.session_state.logged_in:
        # Wrap the welcome message and note in a styled card

        st.markdown(f"<h3 style='text-align: center;'>Hello, broski 💞!</h3>", unsafe_allow_html=True)

        note_text = """
        I know you will kinda not like all this work that I did, but Abhi, it's not out of any greed of appreciation or praise, I just felt like it, and I did. Also, you can't criticize something that I enjoy doing, now can you?
        <br><br>
        So this is just a little gift from my side. This is the most I can do as of now.
        <br>
        <b>Wish You a cheerful, blissful, heartful and soulful Birthday!</b>
        """
        st.markdown(f'<div class="note-container">{note_text}</div>', unsafe_allow_html=True)

        if st.button("Log Out"):
            with st.spinner("Logging out..."):
                time.sleep(2)
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Login View ---
    else:
        # Wrap the login form in a styled card
        st.info("Log in to see your surprise. 😉")
        with st.form("login_form"):
            name = st.text_input("Your Name")
            nickname = st.text_input("Your Nickname that I call you by")
            submit_button = st.form_submit_button("Let's Go!")

            if submit_button:
                if name and nickname:
                    if name.lower() == "abhijeet" and nickname.lower() == "abhi":
                        with st.spinner("Unlocking the surprise..."):
                            time.sleep(2)
                        st.session_state.logged_in = True
                        st.session_state.username = name
                        st.success("Surprise Unlocked!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Incorrect details. Are you sure you're my broski? 🤔")
                else:
                    st.warning("Please fill in both fields.")
        st.markdown('</div>', unsafe_allow_html=True)

