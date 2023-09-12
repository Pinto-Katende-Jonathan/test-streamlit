import streamlit as st
import pandas
from PIL import Image

st.write("""
# Simple Stock Price App
***

Shown are the stock closing price and volume of Google!


""")

df = pandas.read_excel("data.xlsx", index_col='ntest'
)

st.dataframe(df, use_container_width=True)

st.write('Evolution du pH')
st.line_chart(df.ph, color='#CD1818')


image = Image.open('good.jpg')
if st.button('Ajout', type='primary'):

    new_image = image.resize((500, 500))

    st.image(new_image)

else:
    st.write('non click')
    
    
#with open("good.jpg", "rb") as file:
#    btn = st.download_button(
#            label="Download image",
#            data=file,
#            file_name="flower.png",
#            mime="image/png"
#          )
          

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)