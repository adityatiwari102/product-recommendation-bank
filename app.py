import streamlit as st
import pandas as pd
import numpy as np
import pickle


classifier = pickle.load(open('churn_pred.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
prod_final = pickle.load(open('prod_final.pkl', 'rb'))
rating_avg = pickle.load(open('rating_avg.pkl', 'rb'))
final_ratings = pickle.load(open('final_ratings.pkl', 'rb'))

def classification(monthly_income, debit_trans_from_s1, debit_trans_from_s3, total_amt_from_s3, target_desc):

   classification = classifier.predict(
      [[monthly_income, debit_trans_from_s1,debit_trans_from_s3, 
      total_amt_from_s3, TAR_Desc]])
   
   print(classification)

   return classification

def status(classification):
   if classification == 0:
      return 'ACTIVE'
   else:
      return 'CHURN'
      
def recommend(status, product):
    
   index = np.where(prod_final.index == (status, product))[0][0]
   similar_products = sorted(list(enumerate(similarity_score[index])), key= lambda x: x[1], reverse=True)[1:6]
    
   data = [] #[[1],[2]]
   for i in similar_products:
      products = []
      products.append(prod_final.index[i[0]])
        
      data.append(products)
             
   return data







st.title('Product Recommendation')

monthly_income = st.number_input('Monthy Income')
debit_trans_from_s1 = st.number_input('Debit Transactions from S1')
debit_trans_from_s3 = st.number_input('Debit Transaction from S3')
total_amt_from_s3 = st.number_input('Total Debit Amount from S3')
TAR_Desc = st.number_input('Customer Class')
st.text('EXECUTIVE : 0, LOW : 1, MIDDLE : 2, PLATINUM : 3')






recommend_product = st.selectbox("Which Product are you using?", 
         rating_avg.index.values)



if st.button('Recommend Products'):
   class_op = classification(monthly_income, debit_trans_from_s1, debit_trans_from_s3, total_amt_from_s3, TAR_Desc)
   a = recommend(status(class_op),recommend_product)
   st.write('The Customer is',status(class_op))
   

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
          

   

    
