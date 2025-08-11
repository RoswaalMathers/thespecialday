import streamlit as st
import base64
import textwrap  # Import the textwrap library
from pathlib import Path

def image_to_base64(image_path):
    """Converts a local image file to a base64 string for embedding in HTML."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None
    
def autoplay_audio(file_path: str):
    """
    Plays an audio file automatically in a Streamlit app.
    """
    # Open the audio file in binary read mode
    with open(file_path, "rb") as f:
        # Read the file and encode it to Base64
        data = f.read()
        b64 = base64.b64encode(data).decode()
        
        # Create the HTML for the audio player
        md = f"""
            <audio autoplay="true" loop="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        # Embed the HTML in the Streamlit app
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def display_poem():
    # Play the audio file automatically
    audio_file = "happybirthday.mp3"
    autoplay_audio(audio_file)


    # --- STYLING (CSS) ---
    st.markdown("""
    <style>
    /* Import a Google Font for the title */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Great+Vibes&display=swap');

    /* Keyframes for animations */
    @keyframes glow-pink {
        0%, 100% { text-shadow: 0 0 10px #ff69b4, 0 0 12px #ff69b4, 0 0 15px #ff69b4; }
        50% { text-shadow: 0 0 15px #ff85c1, 0 0 20px #ff85c1, 0 0 25px #ff85c1; }
    }
    
    @keyframes glow-gold {
        0%, 100% { text-shadow: 0 0 10px #ffd700, 0 0 12px #ffd700, 0 0 15px #ffd700; }
        50% { text-shadow: 0 0 15px #ffec8b, 0 0 20px #ffec8b, 0 0 25px #ffec8b; }
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
        animation: glow-pink 3s ease-in-out infinite;
    }

    /* Styling for the main content cards */
    .card {
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 2rem;
        width: 100%;
        max-width: 700px;
        margin: 2rem auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Poem container specific styles */
    .poem-container {
        color: #e0e0e0;
        font-family: 'Georgia', serif;
        font-size: 1.15em;
        line-height: 1.8;
        text-align: center;
        white-space: pre-wrap;
    }
    
    /* Two-column layout styling */
    .two-column-layout {
        display: flex;
        align-items: center;
        gap: 2rem;
    }
    .image-column {
        flex: 2;
    }
    .text-column {
        flex: 3;
    }
    .column-image {
        width: 100%;
        border-radius: 15px;
        border: 3px solid rgba(255, 255, 255, 0.3);
    }
    .birthday-title {
        font-family: 'Great Vibes', cursive;
        font-size: 3em;
        text-align: center;
        color: #f0e68c;
        animation: glow-gold 3s ease-in-out infinite;
        line-height: 1.2;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("A Special Poem for You 🎂")

    # --- The Poem Card ---
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
    
    # FIX: Use textwrap.dedent to remove unwanted leading whitespace
    clean_poem = textwrap.dedent(poem_text).strip()
    
    st.markdown(f'<div class="card poem-container">{clean_poem}</div>', unsafe_allow_html=True)

    # --- Two-Column Birthday Wish and Image Card ---
    image_path = "abhi.png"
    base64_image = image_to_base64(image_path)

    if base64_image:
        birthday_card_html = f"""
        <div class="card">
            <div class="two-column-layout">
                <div class="image-column">
                    <img src="data:image/png;base64,{base64_image}" class="column-image">
                </div>
                <div class="text-column">
                    <h2 class="birthday-title">Happiest Birthday sweet lil abhi ✨</h2>
                </div>
            </div>
        </div>
        """
        st.markdown(birthday_card_html, unsafe_allow_html=True)
    else:
        st.warning(f"Could not find '{image_path}'. Make sure it's in the same folder as your script.")

