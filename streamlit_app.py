import streamlit as st
import os
st.title('🎈 App Name')

st.write('Hello world!' + os.environ.get("SECRET_111"))
