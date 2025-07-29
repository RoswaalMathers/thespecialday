<div align="center">

# A Little Surprise for My Broski 🎂

</div>

Hey Abhi,

Happy Birthday! I know you're not big on grand gestures, but I couldn't resist putting together this little digital thing for you. It's just a small web app I built to celebrate your special day. I had a lot of fun making it, and I hope it brings a smile to your face! 😊

This is just my way of saying you're awesome.

---

### ✨ What's Inside?

*   A "top-secret" login page (only you should know the credentials 😉).
*   A personal note from me to you on the home page.
*   A special poem that I felt captured our weird and wonderful friendship.
*   Some flashy animations because... why not? ✨

---

### 🚀 How to Run This Thing (If You're Curious)

If you ever want to run this on your own computer, here’s how:

1.  **Get the files:**
    Make sure you have all the project files in one folder.

2.  **Set up a virtual space:**
    It's good practice to create a virtual environment. Open your terminal in the project folder and run:
    ```bash
    python -m venv venv
    ```
    Then activate it:
    *   On Windows: `.\venv\Scripts\activate`
    *   On macOS/Linux: `source venv/bin/activate`

3.  **Install the magic spells (dependencies):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the app!**
    ```bash
    streamlit run main.py
    ```

---

### 💻 A Peek Under the Hood

I built this using Python and a cool library called Streamlit. It was fun to piece it all together! If you're ever curious to see the code I wrote, I've tucked it away in the collapsible sections below.

<details>
<summary><strong>main.py</strong> (The App's Conductor 🎵)</summary>

```python
import streamlit as st
from streamlit_option_menu import option_menu
import home, poem

#set page config
try:
    st.set_page_config(
        page_title="Broski's Special Day",
        page_icon=":tada:",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
except:
    pass

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None


class MultiApp:
    def __init__(self):
        if st.session_state.logged_in:
            self.apps = [
                {"title": "Home", "function": home.app},
                {"title": "Poem", "function": poem.display_poem}
                
            ]
        else:
            self.apps = [
                {"title": "Home", "function": home.app}
            ]

    def run(self):

        # Inject custom CSS
        st.markdown(
            """
            <style>
            /* Target the outermost navbar wrapper with class 'menu' */
            [data-testid = "st.menu"] {
                background-color: transparent ; /* Or match your theme */
                border-radius: 30px !important;
                box-shadow: none !important;
                margin-top: 10px;
                padding: 0 !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )


        # only display the menu if the user is logged in
        if st.session_state.logged_in:
            menu_items = ["Home","Poem"]
            icons_list = ["house", "book"]
        
        else:
            menu_items = ["Home"]
            icons_list = ["house"]

        selected = option_menu(
            menu_title=None,
            options=menu_items,
            icons=icons_list,
            orientation="horizontal",
            default_index=0,
            styles={
                "container": {
                    # "padding": "0", 
                    "background-color": "#1f1f2e",
                    "border-radius": "10px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "color": "white",
                    "margin": "0",
                    "left": "0px",
                },
                "nav-link-selected": {
                    "color": "black",
                    "background-color": "#fce4ec",
                },
            }
        )



        for app in self.apps:
            if app["title"] == selected:
                app["function"]()

app = MultiApp()
app.run()
```

</details>

<details>
<summary><strong>home.py</strong> (The Welcome Mat & Login Gate 🔑)</summary>

```python
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
```

</details>

<details>
<summary><strong>poem.py</strong> (The Heartfelt Words 📜)</summary>

```python
import streamlit as st

def display_poem():
    """
    Displays the title and the styled, animated poem in the Streamlit app.
    """
    # --- STYLING (CSS) ---
    # This block applies the same modern, animated style as the home page.
    st.markdown("""
    <style>
    /* Import a Google Font for the title */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Keyframes for animations */
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #ff69b4, 0 0 12px #ff69b4, 0 0 15px #ff69b4; }
        50% { text-shadow: 0 0 15px #ff85c1, 0 0 20px #ff85c1, 0 0 25px #ff85c1; }
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

    /* Styling for the poem container card */
    .poem-container {
        background: rgba(40, 40, 60, 0.6); /* Semi-transparent background */
        backdrop-filter: blur(10px); /* Frosted glass effect */
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        width: 100%;
        max-width: 600px; /* Made slightly wider for the poem */
        margin: 2rem auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        color: #e0e0e0; /* Light text color for dark background */
        font-family: 'Georgia', serif; /* Keep the classic font for the poem */
        font-size: 1.15em;
        line-height: 1.8;
        text-align: center;
        white-space: pre-wrap; /* Preserves line breaks from the string */
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("A Special Poem for You 🎂")

    # --- The Poem ---
    # Cleaned up the poem string for consistent formatting.
    poem_text = """
After all we've said till now,
I still find myself short on words somehow.
Can’t help but wonder when and where,
Two starry minds found this bond so rare. 🌌<br>

From just some casual IG chats,
To being mirrors—reflecting facts.
Calling out flaws, but with gentle care,
Helping each other steer clear of despair.

It wasn’t just fate or passing chance,
That pulled us into this shared expanse.
Some stars aligned, in a quiet way,
And wrote this friendship into play. ✨

You talk with heart, no masks, no games,
Just honesty running through your veins.
So rare it feels, so clean, so true—
I trust the world a bit more, 'cause of you.

You call me senpai, and I chuckle inside,
Your respect is loud, no need to hide.
And yet we banter, like little kids,
Trading chaos and sussy skits. 😆

From 3AM talks that wander and flow,
To quiet times where no words show—
I’ve found a peace in you, a light,
That makes even darkest nights feel right. 🌙

So here’s to you, Abhi—my constant star,
The best person I've got, by far.
On your birthday, I hope you see,
How much your presence means to me. 🎂💫
"""

    # --- Displaying the Poem in the Styled Box ---
    st.markdown(f'<div class="poem-container">{poem_text}</div>', unsafe_allow_html=True)
```

</details>

<br>

...anyway, that's all from me. **Wish You a cheerful, blissful, heartful and soulful Birthday!** 🎉

