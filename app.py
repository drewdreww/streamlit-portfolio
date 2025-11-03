import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(
    page_title="Salvs Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Sidebar Navigation ---
with st.sidebar:
    st.image(
        "images/atabzzz.jpg",
        use_container_width=True,
    )
    st.title("Ralph Andrew Salvame")
    st.write("BS Computer Science")
    st.markdown("---")
    page_selection = st.radio(
        "Go to",
        ["🏠 Home", "📖 Autobiography", "💼 Projects", "📬 Contact"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.subheader("Find me online:")
    st.markdown("""
    <style>
    .social-links {
        font-size: 20px;
        line-height: 2.2;
    }
    .social-links a {
        text-decoration: none;
        
        font-weight: bold;
    }
    .social-links a:hover {
        color: #1E91FF; /* Hover effect */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="social-links">
        📘 <a href="https://www.facebook.com/ransalvame" target="_blank">Facebook</a><br>
        💻 <a href="https://github.com/drewdreww" target="_blank">GitHub</a><br>
    </div>
    """, unsafe_allow_html=True)


# --- Home Page ---
if page_selection == "🏠 Home":
    st.title("Welcome to My Digital Space! 👋")
    st.markdown("---")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "images/wow.jpg",
            caption="Ralph Andrew Salvame",
            use_container_width=True,
            output_format="PNG",
        )

    with col2:
        st.header("I'm Ralph Andrew Salvame.")
        st.subheader("Aspiring Developer, Tech Enthusiast, and Lifelong Learner.")
        st.write(
            """
            Hello! I'm passionate about building things for the web and exploring new technologies.
            This interactive web app, built with Streamlit, is my personal portfolio and a
            small window into my journey.
            """
        )
        st.markdown(
            """
            **What I'm currently focused on:**
            - 🚀 Honing my skills in Python and data science.
            - 🌐 Learning new web development frameworks.
            - 🤖 Exploring the world of AI and Machine Learning.

            Feel free to browse my portfolio, learn a bit about my story, or send me a message!
            """
        )
        st.toast("Welcome!", icon="🎉")

    st.markdown("---")
    st.subheader("My Core Competencies")
    # Using columns for a cleaner layout
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("**Data Analysis**", icon="📊")
        st.write("Turning data into actionable insights.")
    with c2:
        st.info("**Web Development**", icon="💻")
        st.write("Building responsive and user-friendly web apps.")
    with c3:
        st.info("**Problem Solving**", icon="💡")
        st.write("Deconstructing complex problems into elegant solutions.")


# --- Autobiography Page ---
elif page_selection == "📖 Autobiography":
    st.title("My Story 📖")
    st.markdown("---")

    st.header("The Journey So Far")

    with st.expander("🌱 Early Life ", expanded=True):
        st.write(
            """
            I like computers ever since :)
            """
        )

    with st.expander("🎓 Education "):
        st.write(
            """
            
            - **University of Southern Philippines Foundation** (2017 - 2023)
              - Degree: JHS/SHS
            - **Cebu Institute of Technology** (2023 - )
              - Degree: BS Computer Science (ongoing)
            """
        )

    with st.expander("🚀 Career "):
        st.write(
            """
            gimme job pls! im broke!
            """
        )

    st.markdown("---")
    st.subheader("Skill Development Over Time")
    st.write("A visual representation of my learning journey (dummy data).")

    # Create dummy data for a chart
    chart_data = pd.DataFrame(
    {
        "Kaboang": [10, 9, 10, 9, 10],
        "Web Dev": [1, 2, 2, 1, 2],
        "Data Science": [1, 2, 1, 1, 2],
    }
)
    
    st.line_chart(chart_data)

    st.subheader("My Hobbies")

    # Using columns for hobbies
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### 🏀 Basketbol")
        st.write("step keri")
    with col2:
        st.markdown("#### 🎮 Valorants")
        st.write("olav ta ser")
    with col3:
        st.markdown("#### 📺 Anime and Movies")
        st.write("kung laayon")

    # A simple progress bar for fun
    st.markdown("---")
    st.write("Stimulation level: ")
    st.caption("for this week alone")
    st.progress(98)


# --- Portfolio Page ---
elif page_selection == "💼 Projects":
    st.title("My Projects 💼")
    st.markdown("---")
    st.subheader("No Projects! Im cooked 🧑‍🍳")
    if st.button("CLICK!"):
        st.toast("gg na oks")
        st.toast("yoko na")
        st.toast("give me job")
        st.toast("no future T_T")
        st.toast("ohahay")
    
    


# --- Contact Page ---
elif page_selection == "📬 Contact":
    st.title("Get In Touch! 📬")
    st.markdown("---")
    st.write("hire me ples")

    # Using st.form
    with st.form(key="contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Your Name")
        with col2:
            email = st.text_input("Your Email")

        message = st.text_area("Your Message")

        submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        if not name or not email or not message:
            st.warning("Please fill out all fields before sending.", icon="⚠️")
        elif "@" not in email:
            st.warning("Please enter a valid email address.", icon="📧")
        else:
            # In a real app, you'd email this or save it to a DB
            st.success(
                f"Thank you, {name}! Your message has been sent. char langs", icon="✅"
            )
            st.balloons()
            st.info("I'll get back to you as soon as possible.")
