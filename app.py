import streamlit as st

# Page Config
st.set_page_config(page_title="My Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for Theme and Alignment
st.markdown(
    """
    <style>
    /* Main Background and Headers */
    .stApp { background-color: #E3F2FD; }
    [data-testid="stSidebar"] { background-color: #BBDEFB; }
    h1, h2, h3 { color: #1565C0; }

    /* Fix the Slider: Thumb and the red/orange line (Track) */
    div[data-testid="stSlider"] [data-baseweb="slider"] > div [role="slider"] {
        background-color: #1565C0 !important;
    }
    /* This targets the colored part of the slider track */
    div[data-testid="stSlider"] [data-baseweb="slider"] > div > div > div {
        background-color: #1565C0 !important;
    }
    div[data-testid="stThumbValue"] { color: #1565C0 !important; }

    /* Fix the Tabs (My Projects): Underline and Text */
    button[data-baseweb="tab"] p { color: #1565C0 !important; }
    div[data-testid="stTabHighlight"] { background-color: #1565C0 !important; }

    /* Fix the Progress Bars (Project Progress) */
    div[data-testid="stProgress"] > div > div > div > div {
        background-color: #1565C0 !important;
    }
/* This targets all Streamlit buttons */
    .stButton > button {
        background: linear-gradient(135deg, #BBDEFB 0%, #90CAF9 100%) !important;
        # color: #1565C0 !important;
        font-weight: 600 !important;
        border-radius: 15px !important;
        border: 1px solid #E3F2FD !important;
        transition: 0.3s;
        height: 3em;
        width: 100%;
    }

    /* Add a slight hover effect to make it feel interactive */
    .stButton > button:hover {
        border: 1px solid #1565C0 !important;
        background: linear-gradient(140deg, #BBDEFB 25%, #90CAF9 100%) !important;
        font-weight: 900 !important;
        color: #0D47A1 !important;
        transform: scale(1.02);
    }

/* Shrinks the gap between columns in the Skills section */
[data-testid="column"] {
    width: calc(25% - 5px) !important;
    flex: 1 1 calc(25% - 5px) !important;
    min-width: calc(25% - 5px) !important;
}

div[data-testid="stHorizontalBlock"] {
    gap: 0.5rem !important; /* This is the magic line that brings them closer */
}

/* This makes the progress bar color match your theme */
.stProgress > div > div > div > div {
    background-image: linear-gradient(to right, #BBDEFB, #1565C0) !important;
}

    </style>

    """,
    unsafe_allow_html=True
)

# Sidebar for Navigation/Bio
with st.sidebar:
    st.image("https://www.pngall.com/wp-content/uploads/13/Cinnamoroll-Background-PNG.png")
    st.title("John Gil T. Cabalida")
    st.write("Applied AI - G02")

    st.divider()
    st.markdown(
    """
    <img src="https://cdn3.emoji.gg/emojis/9183-cinnasleep.png" style="width: 43px; vertical-align: middle; margin-right: 3px;">
    <a href="https://github.com/jgcjgc123123" target="_blank" style="text-decoration: none; color: #1565C0;  font-size: 14px;">my github</a>
    <br>
    <img src="https://cdn3.emoji.gg/emojis/8383-cinnamusic.png" style="width: 43px; vertical-align: middle; margin-right: 3px;">
    <a href="https://facebook.com/user66six" target="_blank" style="text-decoration: none; color: #1565C0;  font-size: 14px;">my facebook</a>
    <br>
    <img src="https://cdn3.emoji.gg/emojis/7623-cinnaangry.png" style="width: 43px; vertical-align: middle; margin-right: 3px;">
    <a href="mailto:johngil.cabalida@cit.edu" style="text-decoration: none; color: #1565C0;  font-size: 14px;">johngil.cabalida@cit.edu</a>
    """,
    unsafe_allow_html=True
)

    st.divider()
    st.caption("© February 2026")
    
 
# Main Header
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="https://cdn3.emoji.gg/emojis/6346-cinnasmile.png" style="width: 70px; margin-right: 6px;">
        <h1 style = "font-weight: 500;">My Bio</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Columns for Layout

col1, spacer, col2 = st.columns([1, 0.1, 1])

with col1:
    st.header("About Me")
    st.write("""
    Hi! I am Cabalida, an IT student in Cebu Institute of 
    Technology-University. With this Applied AI subject,
    I'm playing around with Streamlit in building my first basic app!
    """)

    st.header("Goals")
    st.checkbox("Finish Applied AI Streamlit activity", value=True)
    st.checkbox("Study for Networking 2 Prelims tomorrow", value=False)
    st.checkbox("Start working on Capstone 1 Problem Exploration", value=False)
    st.checkbox("Go to sleep", value=False)


with col2:
    st.header("Interests")
    
    st.write("🎨 UI/UX Design")
    st.progress(85)

    st.write("💻 Coding")
    st.progress(70)
    
    st.write("✨ Applied AI")
    st.progress(90)

    st.header("Skills")
    s1, s2, s3, s4 = st.columns(4)
    with s1:
     st.button("Python", use_container_width=True)
    with s2:
     st.button("React", use_container_width=True)
    with s3:
     st.button("AWS", use_container_width=True)
    with s4:
     st.button("Figma", use_container_width=True)

st.divider()

# Portfolio Section (Tabs)
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="https://cdn3.emoji.gg/emojis/49683-cinnamoroll-roll.png" style="width: 55px; margin-right: 10px;">
        <h1 style = "font-weight: 500;">My Works</h1>
    </div>
    """,
    unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["Kocoa", "E-vents", "Eupemia"])

with tab1:
    st.write("Kocoa E-Commerce | [Github](https://github.com/RoverCyrill/CSIT340-Kocoa)")
    st.image("Screenshot 2026-02-15 085624.png")
    st.write("Last semester, I worked with my teammates in coming up with a simple e-commerce website in our React subject. That taught me to be more of a team player, and strengthening my skills in that area.")
with tab2:
    st.write("E-vents Tickets | [Figma](https://www.figma.com/proto/AT4yuhsrrMGk7PAK6aVBOW/E-vents--Event-Management-and-Ticketing-System?node-id=35-145&p=f&t=idwAxkbQg5MmrmcY-1&scaling=scale-down&content-scaling=fixed&page-id=6%3A319) ")
    st.image("e-vents.png")
    st.write("Another team project that I contributed to, perhaps longer ago. I made screens of the mobile prototype in Figma and I remember contributing to this project as being fun.")
with tab3:
    st.write("Eupemia Accessories | [Figma](https://www.figma.com/proto/zmOr59oiOMehtILpVlcWAn/Eupemia-Website?node-id=89-78&starting-point-node-id=89%3A78&scaling=scale-down-width&content-scaling=fixed&t=v5yuk0QxGgY8HCQ0-1)")
    st.image("eupemia.png")
    st.write("Now this one is so long ago and is actually my first ever prototype in Figma, but I love it so much because I made this in honor of our real life business which is kinda on hold for now as I am stil a student... who knows if I might come back to this in the future and make it an actual thing.")

st.divider()

# Certs Section
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="https://cdn3.emoji.gg/emojis/58835-cinnamoroll-earsup.png" style="width: 55px; margin-right: 10px;">
        <h1 style = "font-weight: 500;">My Certificates</h1>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    inner_c1, inner_c2, inner_c3 = st.columns([1, 3, 1])
    with inner_c2:
        st.image("blob.png", use_container_width=True)

with col2:
    inner_c4, inner_c5, inner_c6 = st.columns([1, 3, 1])
    with inner_c5:
        st.image("blob (1).png", use_container_width=True)

st.write("I got these certificates from last semester's AWS Cloud elective powered by Accenture.")

st.divider()

# Contact Form Component
st.markdown(
    f"""
    <div style="display: flex; align-items: center;">
        <img src="https://cdn3.emoji.gg/emojis/6231-cinnarainbow.png" style="width: 60px; margin-right: 10px;">
        <h1 style = "font-weight: 500;">My Inbox</h1>
    </div>
    """,
    unsafe_allow_html=True
)
name = st.text_input("Your Name:")
message = st.text_area("Drop a message for me!")
if st.button("Submit"):
    st.balloons()
    st.write(f"Thanks for visiting, {name}!")