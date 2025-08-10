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
After all that I've said till now,
I still find myself short on words somehow.
Can’t help but wonder when and where,
Two starry minds found this bond so rare. 🌌<br>

From just some casual in-game chats,
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

