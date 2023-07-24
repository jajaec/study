import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris

## Title
st.title('Streamlit Tutorial')
## Header/Subheader
st.header('This is header')
st.subheader('This is subheader')
## Text
st.text('Hello Streamlit! 이 글은 튜토리얼 입니다.')

## Load data
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris['target']
iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))

## Return table/dataframe
# table
st.table(iris_df.head())

# dataframe
st.dataframe(iris_df)
st.write(iris_df)