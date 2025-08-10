import streamlit as st

def show_media():
    """
    Displays the title and a properly contained, styled video player.
    """
    # --- STYLING (CSS) ---
    # This CSS is updated to correctly handle a responsive iframe inside a container.
    st.markdown("""
    <style>
    /* Import a Google Font for the title */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    /* Keyframes for animations */
    @keyframes glow {
        0%, 100% { text-shadow: 0 0 10px #29b6f6, 0 0 12px #29b6f6, 0 0 15px #29b6f6; }
        50% { text-shadow: 0 0 15px #81d4fa, 0 0 20px #81d4fa, 0 0 25px #81d4fa; }
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

    /* Outer container with the glassmorphism style */
    .card-container {
        background: rgba(40, 40, 60, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 15px;
        padding: 1.5rem;
        width: 100%;
        max-width: 800px;
        margin: 2rem auto;
        animation: fadeIn 0.8s ease-out;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    
    /* Responsive container for the iframe */
    .video-wrapper {
        position: relative;
        overflow: hidden;
        width: 100%;
        padding-top: 56.25%; /* 16:9 Aspect Ratio */
        border-radius: 8px; /* Rounded corners for the video itself */
    }

    /* Iframe styling */
    .video-wrapper iframe {
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        width: 100%;
        height: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("Media For You")
    st.markdown("<p style='text-align: center; color: #d0d0d0; font-style: italic;'>A little something I wanted to share.</p>", unsafe_allow_html=True)

    # --- Building the Video Player with HTML ---
    # We use the YouTube embed URL and construct an iframe manually.
    video_embed_url = "https://www.youtube.com/embed/KgayxOF4Y7E"
    
    video_html = f"""
    <div class="card-container">
        <div class="video-wrapper">
            <iframe
                src="{video_embed_url}"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen>
            </iframe>
        </div>
    </div>
    """
    
    # Render the custom HTML
    st.markdown(video_html, unsafe_allow_html=True)
