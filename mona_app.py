import streamlit as st
import pandas as pd
import numpy as np

st.title('MONA application - Get your dataset')
st.header('MONA application - Get your dataset')

st.image("data:image/png;base64,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")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

if option == 'Email':
    st.write('Email is dope !')
else:
    st.write('Nice choice.')
