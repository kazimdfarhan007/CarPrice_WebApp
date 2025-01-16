import streamlit as st
import pandas as pd
import datetime
#import xgboost as xgb

def main():
   # model=xgb.XGBRegressor()
    #model.load_model('xgb_final.json')
    
    html_temp="""
    <div style = "background-color:lightblue;padding:16px">
    <h2 style="color:black;text-align:center;"> Car Price Prediction Using ML
    <p style="font-size:1vw;">          Developed by Kazi Md Farhan.</p>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown("#### Are you planning to sell your car?\n#### so Let's find best price")
    p1=st.number_input("What is the current ex-showroom price (in lakhs)",2.5,25.0,step=1.0)
    p2=st.number_input("What is the distance completed by the car in kilometers?",100,5000000,step=100)
    s1=st.selectbox("What is the fuel type of the car?",('Petrol','Diesel','CNG'))
    if s1=="Petrol":
        p3=2
    elif s1=="Diesel":
        p3=1
    elif s1=="CNG":
        p3=0
    s2=st.selectbox("Are you dealer or individual?",('Dealer','Individual'))
    if s2=="Dealer":
        p4=0
    elif s2=="Individual":
        p4=1    
        
    s3=st.selectbox("What is the fuel type of the car?",('Manual','Automatic'))
    if s3=="Manual":
        p5=1
    elif s3=="Automatic":
        p5=0 
    p6=st.slider("Number of the owner the car previously has?",0,6)    
    
    date_time=datetime.datetime.now()
    years=st.number_input("In which year can car was purchased?",1990,date_time.year)
    p7=date_time.year-years
    
    dataset_new = pd.DataFrame({
    'Present_Price':p1,
    'Driven_kms':p2,
    'Fuel_Type':p3,
    'Selling_type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    try:
        if st.button('Predict'):
            pred=model.predict(dataset_new)
            if pred>0:
                st.success("You can sell your car for{:.2f} Lakhs".format(pred[0]))
            else:
                st.Warning("You can't able to sell this car")
    except:
        st.warning("Something went wrong please try y")            
    st.write('')
    st.write('                                                       ')
    
if __name__ == '__main__':
        main()
