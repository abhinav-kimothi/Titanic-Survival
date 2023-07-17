import streamlit as st
import pickle
from configparser import ConfigParser

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
        p_class=st.selectbox("Passenger Class",["First","Second","Third"])
        embarkment=st.selectbox("Port of Embarkment",["Cherbourg","Queenstown","Southampton"])
        gender=st.radio("Gender",["Male","Female"],horizontal=True)

        age=st.slider("Age",min_value=0,max_value=100,value=0,step=1)
        fare=st.slider("Fare",min_value=0.0,max_value=600.0,value=0.0,step=0.1)

        family_size=st.number_input("Parents/Children",min_value=0,max_value=10,value=0,step=1)
        siblings=st.number_input("Siblings/Spouses",min_value=0,max_value=10,value=0,step=1)    

        submit=st.form_submit_button("Submit",use_container_width=True)

    return p_class,embarkment,gender,age,fare,family_size,siblings,submit

def predict_survival(p_class,embarkment,gender,age,fare,family_size,siblings,model):
    if p_class=="First":
        class1=1
        class2=0
        class3=0
    elif p_class=="Second":
        class1=0
        class2=1
        class3=0
    else:
        class1=0
        class2=0
        class3=1
    if embarkment=="Cherbourg":
        emb_c=1
        em_q=0
        em_s=0
    elif embarkment=="Queenstown":
        emb_c=0
        em_q=1
        em_s=0
    else:
        emb_c=0
        em_q=0
        em_s=1
    if gender=="Male":
        male=1
        female=0
    else:
        female=1
        male=0
    
    if family_size==0: 
        parch_0=1
        parch_1=0
        parch_2=0
        parch_3=0
        parch_4=0
        parch_5=0
        parch_6=0
    elif family_size==1: 
        parch_1=1
        parch_0=0
        parch_2=0
        parch_3=0
        parch_4=0
        parch_5=0
        parch_6=0
    elif family_size==2: 
        parch_2=1
        parch_0=0
        parch_1=0
        parch_3=0
        parch_4=0
        parch_5=0
        parch_6=0
    elif family_size==3: 
        parch_3=1
        parch_0=0
        parch_1=0
        parch_2=0
        parch_4=0
        parch_5=0
        parch_6=0
    elif family_size==4: 
        parch_4=1
        parch_0=0
        parch_1=0
        parch_2=0
        parch_3=0
        parch_5=0
        parch_6=0
    elif family_size==5: 
        parch_5=1
        parch_0=0
        parch_1=0
        parch_2=0
        parch_3=0
        parch_4=0
        parch_6=0
    elif family_size==6: 
        parch_6=1
        parch_0=0
        parch_1=0
        parch_2=0
        parch_3=0
        parch_4=0
        parch_5=0
    else: 
        parch_6=1
        parch_0=0
        parch_1=0
        parch_2=0
        parch_3=0
        parch_4=0
        parch_5=0
    if siblings==0: 
        sib_0=1
        sib_1=0
        sib_2=0
        sib_3=0
        sib_4=0
        sib_5=0
        sib_8=0
    elif siblings==1: 
        sib_1=1
        sib_0=0
        sib_2=0
        sib_3=0
        sib_4=0
        sib_5=0
        sib_8=0
    elif siblings==2: 
        sib_2=1
        sib_0=0
        sib_1=0
        sib_3=0
        sib_4=0
        sib_5=0
        sib_8=0
    elif siblings==3: 
        sib_3=1
        sib_0=0
        sib_1=0
        sib_2=0
        sib_4=0
        sib_5=0
        sib_8=0
    elif siblings==4:   
        sib_4=1
        sib_0=0
        sib_1=0
        sib_2=0
        sib_3=0
        sib_5=0
        sib_8=0
    elif siblings==5:
        sib_5=1
        sib_0=0
        sib_1=0
        sib_2=0
        sib_3=0
        sib_4=0
        sib_8=0
    else: 
        sib_8=1
        sib_0=0
        sib_1=0
        sib_2=0
        sib_3=0
        sib_4=0
        sib_5=0

    pickle_model=pickle.load(open(model,'rb'))



    prediction=pickle_model.predict([[age, fare, parch_0, parch_1, parch_2, parch_3, parch_4,parch_5, parch_6, emb_c, em_q, em_s, female, male,class1, class2, class3, sib_0, sib_1, sib_2, sib_3,sib_4, sib_5, sib_8]])

    return prediction

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
