# Mengimpor library
import pandas as pd
import streamlit as st
import pickle

# Menghilangkan warning
import warnings
warnings.filterwarnings("ignore")

# Menulis judul
st.markdown("<h1 style='text-align: center; '> Churn Customer Prediction (Exited/No) </h1>", unsafe_allow_html=True)
st.markdown('---'*10)


# Fungsi untuk prediksi
def final_prediction(values, model):
    global prediction
    prediction = model.predict(values)
    return prediction

# Ini merupakan fungsi utama
def main():
    
    # Nilai awal
    Age = 39
    CreditScore = 850
    Balance	= 83807
    
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            Age = st.number_input('Age', value=Age)
        with col2:
            Balance = st.number_input('Balance', value=Balance)
        with col3:
            CreditScore = st.number_input('Credit Score', value=CreditScore)
    
    data = {
        'Age': Age,
        'Balance':Balance,
        'CreditScore': CreditScore
        }
    
    kolom = list(data.keys())
    
    df_final = pd.DataFrame([data.values()],columns=kolom)
    
    # load model
    my_model = pickle.load(open('churn_customer_prediction.pkl', 'rb'))
    
    # Predict
    result = int(final_prediction(df_final, my_model))
    
    hasil = []
    if result==0:
        hasil='No'
    else:
        hasil='Exited'
    
    st.markdown('---'*10)
    
    st.write('<center><b><h3>Predicted Exited/No= ', hasil,'</b></h3>', unsafe_allow_html=True)
           
if __name__ == '__main__':
	main() 


