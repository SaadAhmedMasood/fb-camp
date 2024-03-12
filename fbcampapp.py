import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import streamlit as st
import pandas as pd
#import joblib
import random
st.title('Live Prediction Of Expected Conversion test3')

df = pd.read_excel('Social_FB.xlsx')

df
