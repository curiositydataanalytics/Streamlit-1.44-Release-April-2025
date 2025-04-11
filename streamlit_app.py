# Data manipulation
import numpy as np
import datetime as dt
import pandas as pd
import geopandas as gpd

# Database and file handling
import os

# Data visualization
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

path_cda = 'C:\\CuriosityDataAnalytics'
path_wd = path_cda + '\\24_streamlit_1_44'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.44?")
st.divider()

with st.sidebar:
    st.logo(path_cda + '\\logo_large.png', size='large')
    st.empty()
#
#

def page1():
    st.header(':one: Custom themes')

    with st.expander('config.toml'):
        cols = st.columns(2)
        cols[0].subheader('Streamlit 1.43')
        cols[0].code('''
            [theme]
            base = "dark"
            primaryColor = "#C9A840"
            backgroundColor = "#123458"
            secondaryBackgroundColor = "#272731"
            font = "serif"
        ''')
        cols[1].subheader('Streamlit 1.44')
        cols[1].code('''
            [theme]
            base = "dark"
            primaryColor = "#C9A840"
            backgroundColor = "#123458"
            secondaryBackgroundColor = "#272731"
            font = "Bebas Neue"

            textColor = "#e1e2e8"
            linkColor = "#1E90FF"
            codeBackgroundColor = "#272731"
            codeFont = "monospace"
            headingFont = "Bebas Neue"
            baseRadius = "0.8rem"
            borderColor = "#DDDDDD"
            showWidgetBorder = true
            baseFontSize = 16
            showSidebarBorder = false

            [[theme.fontFaces]]
            family = "Bebas Neue"
            url = "https://fonts.gstatic.com/s/bebasneue/v14/JTUSjIg69CK48gW7PXoo9Wlhyw.woff2"
            weight = 400
            style = "normal"
        ''')

    
    st.code('''
    df = pd.DataFrame({'a': [1, 2, 3],
                   'b': [4, 5, 6],
                   'c': [7, 8, 9]})
    st.button('Click me!')
    st.bar_chart(df)
    st.dataframe(df)
    ''')
    df = pd.DataFrame({'a': [1, 2, 3],
                   'b': [4, 5, 6],
                   'c': [7, 8, 9]})
    st.button('Click me!')
    st.bar_chart(df)
    st.dataframe(df)


def page2():
    st.header(':two: st.badge')

    st.code('''
        st.badge('Recently watched', icon="🕒", color="blue")
        st.write('* The Last of Us - Season 1, Episode 4')
        st.write('* Severance - Season 2, Episode 9')
        st.badge('New Releases', icon="🆕", color="green")
        st.write('* The White Lotus - Season 3, Episode 1')
        st.badge('Free This Week', icon="💰", color="orange")
        st.write("* Hell's Kitchen - Season 22, Episode 1")
    ''')
    st.badge('Recently watched', icon="🕒", color="blue")
    st.write('* The Last of Us - Season 1, Episode 4')
    st.write('* Severance - Season 2, Episode 9')
    st.badge('New Releases', icon="🆕", color="green")
    st.write('* The White Lotus - Season 3, Episode 1')
    st.badge('Free This Week', icon="💰", color="orange")
    st.write("* Hell's Kitchen - Season 22, Episode 1")


def page3():
    st.header(':three: st.exception')
    
    st.code('''
        username = st.text_input("Enter your username")
        try:
            if "$" in username:
                raise ValueError("Usernames cannot contain the '$' character.")
            elif len(username) > 0:
                st.success(f"✅ Username *{username}* is valid!")
        except ValueError as e:
            st.error("❌ Invalid username!")
            st.exception(e)
    ''')

    username = st.text_input("Enter your username")
    try:
        if "$" in username:
            raise ValueError("Usernames cannot contain the '$' character.")
        elif len(username) > 0:
            st.success(f"✅ Username *{username}* is valid!")
    except ValueError as e:
        st.error("❌ Invalid username!")
        st.exception(e)
    



def page4():
    st.header(':four: streamlit init')

    st.code('''
    streamlit init C:\projects\my_app
    ''')


pg = st.navigation([st.Page(page1, title='Custom themes'),
                    st.Page(page2, title='st.badge'),
                    st.Page(page3, title='st.exception'),
                    st.Page(page4, title='streamlit init')])
pg.run()