import streamlit as st
import time

st.set_page_config(page_title="Portfolio", page_icon=":page_with_curl:", layout="wide")


def set_bg_hack_url():

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/free-vector/gradient-black-technology-background_23-2149209060.jpg?w=900&t=st=1699107482~exp=1699108082~hmac=acc977cbfc5238091b70c7f01c30d0452a772801ff9f81046e77627bd7fe7d73");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


set_bg_hack_url()

option = st.sidebar.selectbox('Select options to explore more', ('About Me', 'Education and Technical skills', 'Experience and Project', 'Hobbies and Future Plan'))

if option == 'About Me':
    st.subheader('PORTFOLIO')
    st.markdown("<h1 style='text-align: left; font-size: 120px; color: white;'>PRATIK</h1>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Personal Info", "Summary"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.image('rename.jpeg', width=300)
        with col2:
            multi = ['Phone number = +91 7597252357', 'EmailID = pratikjhajharia2152@gmail.com',
                     'LinkedinID =  www.linkedin.com/in/pratik-637512944/',
                     'Github id = https://github.com/Pratik5566', 'Location = Jhunjhunu, Rajasthan']

            for i in multi:
                st.subheader(i)
    with tab2:
        st.title("Summary")
        st.subheader('I am a second-year BTech student with a passion for Web Dovelopment and Computers.'
                      ' Proficient in Java and C++, I am eager to learn & understand new things and collaborate with professionals to contribute in real-world projects.')


if option == 'Education and Technical skills':
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    with st.container():
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image('gifpage0.gif', use_column_width=True)

    with st.container():
        st.title('Education')
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            st.image('education.jpg', width=300)
        with col2:
            st.header('B.Tech, Computer Science and Engineering (Graduating 2026)')
            st.text('')
            st.text('')
            st.subheader('SRM Institute of Science and Technology, Chennai, India')
            st.subheader('Specialization in Software Engineering')
            st.subheader('Relevant coursework: Data Structures and Algorithm,OODP,Operating System,System Design,Programming,etc.')
            for i in range(5):
                st.text('')

    with st.container():
        st.markdown('<h1 style="text-align: right;">Technical skills</h1>', unsafe_allow_html=True)
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.7, 0.3])
        with col2:
            st.image('technical.jpg', width=350)
        with col1:
            st.header('Languages:')
            st.subheader(' C, C++, Java, Python.')
            st.text('')
            st.text('')
            st.header('Machine Learning:')
            st.subheader('NumPy, Pandas, Scikit-learn, TensorFlow.')
            st.text('')
            st.text('')
            st.header('Developer Tools:')
            st.subheader('Git, VScode, Pycharm.')


if option == 'Experience and Project':
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    with st.container():
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image('gifpage1.gif', use_column_width=True)

    with st.container():
        st.title('Experience')
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            st.text('')
            st.text('')
            st.image('experience.jpg', width=300)
        with col2:
            st.header('SRM Quantum Computing Club, Chennai, IN: Technical Associate (Oct 2022 – Present)')
            st.subheader('Tried to contribute in some projects in Ai/ML domain')
            st.text('')
            st.text('')
            st.header('SRM Swift Coding Club, Chennai, IN: Member (Mar 2023 – Present)')
            st.subheader('Tried to contribute in some projects in Ai/ML domain')
            for i in range(5):
                st.text('')

    with st.container():
        st.markdown('<h1 style="text-align: right;">Projects</h1>', unsafe_allow_html=True)
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.7, 0.3])
        with col2:
            for i in range(15):
                st.text('')
            st.image('project.jpg', width=350)
        with col1:
            st.header('Hospital Management System:')
            st.subheader('Helps to identify the availability of medicines.')
            st.text('')
            st.text('')
            st.header('Tic Tac Toe:')
            st.subheader('Game')
            st.text('')
            st.text('')
            st.header('Solar System planet identifier using CNN:')
            st.subheader('An educational purpose project to identify planets of solar system')
            st.text('')
            st.text('')
            st.header('Basic Greetings Chat-bot')
            st.subheader('A personal learning project to understand the implementation of NLP')
            st.text('')
            st.text('')


if option == 'Hobbies and Future Plan':
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    st.balloons()

    with st.container():
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image('gifpage2.gif', use_column_width=True)

    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.title('Hobbies & Interest')
        st.subheader('', divider='rainbow')
        st.subheader('Badminton')
        st.subheader('Cricket')
        st.subheader('Music')
        st.subheader('Gaming')
    with col2:
        st.title('Future plans')
        st.subheader('', divider='rainbow')
        st.subheader('Learning DSA in Java')
        st.subheader('Learning mySQL and PowerBI for data analytics')