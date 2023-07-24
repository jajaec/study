import pandas as pd
import numpy as np
import streamlit as st

# df = pd.read_csv("tips.csv")

# SYNTAX
# streamlit.dataframe(data=None, width=None, height=None) # height and width in pixels
# st.dataframe(df,500,500)

# Create a dictionary for the dataframe
dict = {
  'Name': ['Sukritin', 'Sumit Tyagi', 
           'Akriti Goel', 'Sanskriti',
           'Abhishek Jain'],
   'Age': [22, 20, 45, 21, 22],
  'Marks': [90, 84, -33, -87, 82]
}
  
# Converting Dictionary to
# Pandas Dataframe
df = pd.DataFrame(dict)

# Define a function for colouring
# negative values red and
# positive values black
def highlight_max(s):
	if s.dtype == np.object:
		is_neg = [False for _ in range(s.shape[0])]
	else:
		is_neg = s < 0
	return ['color: red;' if cell else 'color:' for cell in is_neg]

# Using apply method of style
# attribute of Pandas DataFrame
# st.dataframe(df.style.apply(highlight_max))

def color_cell(x, color):
    color = f'background-color:{color}'
    return color

# st.dataframe(df.style.applymap(color_cell, color='#ff9090', subset=pd.IndexSlice[1, ['Age']]))
st.dataframe(df.style.applymap(color_cell, color='#ff9090', subset=([1,2], 'Age')))

# st.table(df)

# st.write(df.head())

# c = """for i in range(2,11,2):   
#            print(i)"""
# st.code(c)