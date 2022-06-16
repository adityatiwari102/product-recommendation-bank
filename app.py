import streamlit as st
import pandas as pd
import numpy as np
import pickle

similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
prod_final = pickle.load(open('prod_final.pkl', 'rb'))
rating_avg = pickle.load(open('rating_avg.pkl', 'rb'))
final_ratings = pickle.load(open('final_ratings.pkl', 'rb'))

def recommend(status, product):
    
    index = np.where(prod_final.index == (status, product))[0][0]
    similar_products = sorted(list(enumerate(similarity_score[index])), key= lambda x: x[1], reverse=True)[1:6]
    
    data = []
    for i in similar_products:
        products = []
        products.append(prod_final.index[i[0]])
        
        data.append(products)
             
    return data





st.title('Product Recommendation')

status = st.selectbox('Status of Customer',final_ratings['Status'].unique())


recommend_product = st.selectbox("Which Product are you using?", 
         rating_avg.index.values)



if st.button('Recommend Products'):
   a = recommend(status,recommend_product)

   recommendation = []
   for i in a:
      recommendation.append(i[0][1])
      
   col1, col2, col3, col4, col5 = st.columns(5)

   with col1:
      st.subheader((recommendation[0]))
          
   with col2:
      st.subheader((recommendation[1]))
          

   with col3:
      st.subheader((recommendation[2]))
          

   with col4:
      st.subheader((recommendation[3]))
          

   with col5:
      st.subheader((recommendation[4]))
          

   

    
