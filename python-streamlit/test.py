import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.subheader('Hallo wave!')  # Let's create a title for our app

# These are two parameters we want to modify interactively, by means of a slider
phi = st.slider(label='phase', min_value=-2*np.pi, max_value=2*np.pi, value=0.0, step=0.1)
freq = st.slider(label='frequency', min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Use the parameters above for some computation
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(freq * (x + phi))

# Let's plot the results of the above computations
fig, ax = plt.subplots()
fig.set_size_inches(9, 4)
ax.plot(x, y)

# Display the result!
st.pyplot(fig)