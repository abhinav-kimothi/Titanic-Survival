import streamlit as st
import joblib
from configparser import ConfigParser
import pandas as pd
import numpy as np

#-----Reading Config File---------#

config_object=ConfigParser()
config_object.read('./config.ini')
#---------------------------------#

linkedin_link=config_object["Contact"]["linkedin_link"]
linkedin_icon=config_object["Contact"]["linkedin_icon"]
twitter_link=config_object["Contact"]["twitter_link"]
twitter_icon=config_object["Contact"]["twitter_icon"]
email_link=config_object["Contact"]["email_link"]
email_icon=config_object["Contact"]["email_icon"]
github_repo=config_object["Contact"]["github_repo"]
github_icon=config_object["Contact"]["github_icon"]
source_code_link=config_object["Contact"]["source_code_link"]
source_code_icon=config_object["Contact"]["source_code_icon"]
coffee_link=config_object["Contact"]["coffee_link"]
coffee_icon=config_object["Contact"]["coffee_icon"]
feedback_link=config_object["Contact"]["feedback_link"]
feedback_icon=config_object["Contact"]["feedback_icon"]
youtube_link=config_object["Contact"]["youtube_link"]
youtube_icon=config_object["Contact"]["youtube_icon"]


def load_css_file(css_file_path):
     with open(css_file_path) as f:
          return st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def input_form():
    with st.form("Input",clear_on_submit=False):
        title=st.selectbox("Title",["Mr","Mrs","Miss","Master","Other"],index=2,help="Title of the passenger")
        name=st.text_input("Name",help="Name of the passenger",max_chars=50,placeholder="Enter Name",value="Jane Doe")
        p_class=st.selectbox("Passenger Class",["First","Second","Third"])
        embarkment=st.selectbox("Port of Embarkment",["Cherbourg","Queenstown","Southampton"])
        gender=st.radio("Gender",["Male","Female"],horizontal=True)

        age=st.slider("Age",min_value=0,max_value=100,value=40,step=1)
        fare=st.slider("Fare",min_value=0.0,max_value=50.0,value=10.0,step=0.1,format="%.2f",help="Fare paid by the passenger")

        family_size=st.number_input("Parents/Children",min_value=0,max_value=10,value=0,step=1)
        siblings=st.number_input("Siblings/Spouses",min_value=0,max_value=10,value=0,step=1)    

        submit=st.form_submit_button("Submit",use_container_width=True)

    return title,name,p_class,embarkment,gender,age,fare,family_size,siblings,submit

def predict_survival(p_class="First",embarkment="S",gender="Male",age=40,fare=10,family_size=1,siblings=1,model='./Models/model_logreg_best.joblib',title="Miss"):
    example_df=pd.DataFrame(columns=['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'log_Fare', 'FamilySize',
       'Sex_female', 'Sex_male', 'Embarked_C', 'Embarked_Q', 'Embarked_S',
       'Title_Master', 'Title_Miss', 'Title_Mr', 'Title_Mrs', 'Title_Other',
       'AgeGroup_Child', 'AgeGroup_Teenager', 'AgeGroup_Adult',
       'AgeGroup_MiddleAge', 'AgeGroup_Senior', 'FareBin_0-8', 'FareBin_8-10',
       'FareBin_10-20', 'FareBin_20-40', 'FareBin_40+'],index=[0])
    

    if p_class=="First":
        example_df.Pclass=1
    elif p_class=="Second":
        example_df.Pclass=2
    else:
        example_df.Pclass=3
    if gender=='Male':
        example_df.Sex_male=1
        example_df.Sex_female=0
    else:
        example_df.Sex_male=0
        example_df.Sex_female=1

    if embarkment=='S':
        example_df.Embarked_S=1
        example_df.Embarked_C=0
        example_df.Embarked_Q=0
    elif embarkment=='C':
        example_df.Embarked_S=0
        example_df.Embarked_C=1
        example_df.Embarked_Q=0
    else:
        example_df.Embarked_S=0
        example_df.Embarked_C=0
        example_df.Embarked_Q=1

    if title=='Mr':
        example_df.Title_Mr=1
        example_df.Title_Mrs=0
        example_df.Title_Miss=0
        example_df.Title_Master=0
        example_df.Title_Other=0
    elif title=='Mrs':
        example_df.Title_Mr=0
        example_df.Title_Mrs=1
        example_df.Title_Miss=0
        example_df.Title_Master=0
        example_df.Title_Other=0
    elif title=='Miss':
        example_df.Title_Mr=0
        example_df.Title_Mrs=0
        example_df.Title_Miss=1
        example_df.Title_Master=0
        example_df.Title_Other=0
    elif title=='Master':
        example_df.Title_Mr=0
        example_df.Title_Mrs=0
        example_df.Title_Miss=0
        example_df.Title_Master=1
        example_df.Title_Other=0
    else:
        example_df.Title_Mr=0
        example_df.Title_Mrs=0
        example_df.Title_Miss=0
        example_df.Title_Master=0
        example_df.Title_Other=1

    if age<12:
        example_df.AgeGroup_Child=1
        example_df.AgeGroup_Teenager=0
        example_df.AgeGroup_Adult=0
        example_df.AgeGroup_MiddleAge=0
        example_df.AgeGroup_Senior=0
    elif age<20:
        example_df.AgeGroup_Child=0
        example_df.AgeGroup_Teenager=1
        example_df.AgeGroup_Adult=0
        example_df.AgeGroup_MiddleAge=0
        example_df.AgeGroup_Senior=0
    elif age<40:
        example_df.AgeGroup_Child=0
        example_df.AgeGroup_Teenager=0
        example_df.AgeGroup_Adult=1
        example_df.AgeGroup_MiddleAge=0
        example_df.AgeGroup_Senior=0
    elif age<60:
        example_df.AgeGroup_Child=0
        example_df.AgeGroup_Teenager=0
        example_df.AgeGroup_Adult=0
        example_df.AgeGroup_MiddleAge=1
        example_df.AgeGroup_Senior=0
    else:
        example_df.AgeGroup_Child=0
        example_df.AgeGroup_Teenager=0
        example_df.AgeGroup_Adult=0
        example_df.AgeGroup_MiddleAge=0
        example_df.AgeGroup_Senior=1

    if fare<8:
        example_df['FareBin_0-8']=1
        example_df['FareBin_8-10']=0
        example_df['FareBin_10-20']=0
        example_df['FareBin_20-40']=0
        example_df['FareBin_40+']=0
    elif fare<10:
        example_df['FareBin_0-8']=0
        example_df['FareBin_8-10']=1
        example_df['FareBin_10-20']=0
        example_df['FareBin_20-40']=0
        example_df['FareBin_40+']=0
    elif fare<20:
        example_df['FareBin_0-8']=0
        example_df['FareBin_8-10']=0
        example_df['FareBin_10-20']=1
        example_df['FareBin_20-40']=0
        example_df['FareBin_40+']=0
    elif fare<40:
        example_df['FareBin_0-8']=0
        example_df['FareBin_8-10']=0
        example_df['FareBin_10-20']=0
        example_df['FareBin_20-40']=1
        example_df['FareBin_40+']=0
    else:
        example_df['FareBin_0-8']=0
        example_df['FareBin_8-10']=0
        example_df['FareBin_10-20']=0
        example_df['FareBin_20-40']=0
        example_df['FareBin_40+']=1

    example_df.Age = age
    example_df.SibSp = siblings
    example_df.Parch = family_size
    example_df.Fare = fare
    example_df.log_Fare = np.log(fare) if fare > 0 else 0
    example_df.FamilySize = siblings + family_size + 1


    selected_model=joblib.load(open(model,'rb'))



    prediction = selected_model.predict(example_df)

    # Get the survival probability
    survival_probability = selected_model.predict_proba(example_df)[:, 1]

    # Map the prediction to the corresponding class label
    prediction = 'Survived' if prediction == 1 else 'Did not survive'

    return prediction, round(survival_probability[0]*100, 2)



def sidebar_footer():
    col1,col2,col3=st.columns(3)
    with col1:
        st.markdown(f"<span style='text-align:right;'><a href={source_code_link}><img src={source_code_icon} alt='source' style='width:40px;height:40px;' title='View Source Code'></a></span>",unsafe_allow_html=True)
        #st.markdown("<p style='font-size:12px;text-align:left;'>Source</p>",unsafe_allow_html=True)
    with col2:
        st.markdown(f"<span style='text-align:center;'><a href={coffee_link}><img src={coffee_icon} alt='coffee' style='width:40px;height:40px;' title='Buy Me A Coffee'></a></span>",unsafe_allow_html=True)
        #st.markdown("<p style='font-size:12px;text-align:left;'>$$upport!!</p>",unsafe_allow_html=True)
    with col3:
        st.markdown(f"<span style='text-align:center;'><a href={feedback_link}><img src={feedback_icon} alt='coffee' style='width:40px;height:40px;' title='Share Feedback'></a></span>",unsafe_allow_html=True)
        #st.markdown("<p style='font-size:12px;text-align:left;'>Feedback</p>",unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align:left;'><a href={github_repo}><img src={github_icon} alt='github' style='width:42px;height:42px;'></a>&emsp;<a href={linkedin_link}><img src={linkedin_icon} alt='linkedin' style='width:42px;height:42px;'></a>&emsp;<a href={twitter_link}><img src={twitter_icon} alt='twitter' style='width:42px;height:42px;'></a>&emsp;<a href={email_link}><img src={email_icon} alt='email' style='width:42px;height:42px;'></a>&emsp;<a href={youtube_link}><img src={youtube_icon} alt='email' style='width:42px;height:42px;'></a></h6>",unsafe_allow_html=True)
    st.divider()
    st.image('./Assets/AKAIlogoblacknobg.jpg')