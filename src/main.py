import streamlit as st
import pickle
from configparser import ConfigParser
import utils
import base64
import json

#-----Reading Config File---------#

config_object=ConfigParser()
config_object.read('./config.ini')
#---------------------------------#

#-----Loading Image Addresses------#
favicon=config_object["PAGE"]["favicon"]
logo=config_object["IMAGES"]["logo"]
header_image=config_object["IMAGES"]["header_image"]
#----------------------------------#

#-----Loading Model----------------#
model_path_logreg=config_object["MODEL"]["model_path_logreg"]
model_path_rf=config_object["MODEL"]["model_path_rfc"]
model_path_xgb=config_object["MODEL"]["model_path_xgb"]
model_path_bc=config_object["MODEL"]["model_path_bc"]

with open("./Data/metrics_logreg.json","r") as file:
    metrics_logreg=json.load(file)



#----------------------Setting Page Config------------------------#
st.set_page_config(page_title="Titanic Survival", page_icon=favicon, layout="wide")
#-----------------------------------------------------------------#

#------Loading CSS File----------#
css_file=config_object["CSS"]["css_file"]
utils.load_css_file(css_file)
#--------------------------------#

#------------SideBar Design--------------#
#------Top of SideBar has the Logo-------#
#------Rest of the SideBar has the content options----#
#-----------------------------------------------------#
with st.sidebar.container():
    #-------Dividing in three columns gives some padding to the content----#
    #----The left and right columns are narrow and we'll keep them blank---#
    #-------This can also be done using the CSS file-----------------------#
    col1,col2,col3=st.columns([1,7,1])
    with col2:
        #----Placing Logo-----#
        #st.sidebar.image(logo)
        st.sidebar.image('./Assets/HeaderImage.png')





    





linkedin_link=config_object["Contact"]["linkedin_link"]
linkedin_icon=config_object["Contact"]["linkedin_icon"]

twitter_link=config_object["Contact"]["twitter_link"]
twitter_icon=config_object["Contact"]["twitter_icon"]

email_link=config_object["Contact"]["email_link"]
email_icon=config_object["Contact"]["email_icon"]


#----Header has link to code repository----#
github_repo=config_object["Contact"]["github_repo"]
github_icon=config_object["Contact"]["github_icon"]

with st.sidebar.container():
    st.divider()
    model_selection=st.radio("Select Model",("Logistic Regression","Random Forest","XGBoost","Bagging Classifier"))
    if model_selection=="Logistic Regression":
        model_path=model_path_logreg
        with st.expander("View Model Metrics"):
            with open("./Data/metrics_logreg.json","r") as file:
                metrics=json.load(file)
            st.write("Training Accuracy:"+str(metrics["model"][0]["accuracy_score_train"])+"%")
            st.write("Validation Accuracy:"+str(metrics["model"][0]["accuracy_score_test"])+"%")
            st.write("Validation Precision:"+str(metrics["model"][0]["precision_score_test"])+"%")
            st.write("Validation Recall:"+str(metrics["model"][0]["recall_score_test"])+"%")
            st.write("Validation F1 Score:"+str(metrics["model"][0]["f1_score_test"])+"%")
            st.write("Confusion Matrix")
            st.image("./Assets/cm_logreg_best.png")
            st.write("ROC Curve")
            st.image("./Assets/roc_logreg_best.png")
            st.write("ROC AUC Score:"+str(metrics["model"][0]["roc_auc_score_test"])+"%")
    elif model_selection=="Random Forest":
        model_path=model_path_rf
        with st.expander("View Model Metrics"):
            with open("./Data/metrics_rfc.json","r") as file:
                metrics=json.load(file)
            st.write("Training Accuracy:"+str(metrics["model"][0]["accuracy_score_train"])+"%")
            st.write("Validation Accuracy:"+str(metrics["model"][0]["accuracy_score_test"])+"%")
            st.write("Validation Precision:"+str(metrics["model"][0]["precision_score_test"])+"%")
            st.write("Validation Recall:"+str(metrics["model"][0]["recall_score_test"])+"%")
            st.write("Validation F1 Score:"+str(metrics["model"][0]["f1_score_test"])+"%")
            st.write("Confusion Matrix")
            st.image("./Assets/cm_rfc_best.png")
            st.write("ROC Curve")
            st.image("./Assets/roc_rfc_best.png")
            st.write("ROC AUC Score:"+str(metrics["model"][0]["roc_auc_score_test"])+"%")

    elif model_selection=="XGBoost":
        model_path=model_path_xgb
        with st.expander("View Model Metrics"):
            with open("./Data/metrics_xgb.json","r") as file:
                metrics=json.load(file)
            st.write("Training Accuracy:"+str(metrics["model"][0]["accuracy_score_train"])+"%")
            st.write("Validation Accuracy:"+str(metrics["model"][0]["accuracy_score_test"])+"%")
            st.write("Validation Precision:"+str(metrics["model"][0]["precision_score_test"])+"%")
            st.write("Validation Recall:"+str(metrics["model"][0]["recall_score_test"])+"%")
            st.write("Validation F1 Score:"+str(metrics["model"][0]["f1_score_test"])+"%")
            st.write("Confusion Matrix")
            st.image("./Assets/cm_xgb_best.png")
            st.write("ROC Curve")
            st.image("./Assets/roc_xgb_best.png")
            st.write("ROC AUC Score:"+str(metrics["model"][0]["roc_auc_score_test"])+"%")

    elif model_selection=="Bagging Classifier":
        model_path=model_path_bc
        with st.expander("View Model Metrics"):
            with open("./Data/metrics_bc.json","r") as file:
                metrics=json.load(file)
            st.write("Training Accuracy:"+str(metrics["model"][0]["accuracy_score_train"])+"%")
            st.write("Validation Accuracy:"+str(metrics["model"][0]["accuracy_score_test"])+"%")
            st.write("Validation Precision:"+str(metrics["model"][0]["precision_score_test"])+"%")
            st.write("Validation Recall:"+str(metrics["model"][0]["recall_score_test"])+"%")
            st.write("Validation F1 Score:"+str(metrics["model"][0]["f1_score_test"])+"%")
            st.write("Confusion Matrix")
            st.image("./Assets/cm_bc_best.png")
            st.write("ROC Curve")
            st.image("./Assets/roc_bc_best.png")
            st.write("ROC AUC Score:"+str(metrics["model"][0]["roc_auc_score_test"])+"%")


#with st.container():
    #col1,col2,col3=st.columns([1,10,1])
    #with col2:
        #----Header Image-----#
        #st.image(header_image)
        #----Social Links-----#
        #st.markdown(f"<h6 style='text-align:right;'><a href={github_repo}><img src={github_icon} alt='github' style='width:42px;height:42px;'></a>&emsp;&emsp;<a href={linkedin_link}><img src={linkedin_icon} alt='linkedin' style='width:42px;height:42px;'></a>&emsp;&emsp;<a href={twitter_link}><img src={twitter_icon} alt='twitter' style='width:42px;height:42px;'></a>&emsp;&emsp;<a href={email_link}><img src={email_icon} alt='email' style='width:42px;height:42px;'></a></h6>",unsafe_allow_html=True)

with st.container():
    col1,col2=st.columns([1,1])
    with col1:
            title,name,p_class,embarkment,gender,age,fare,family_size,siblings,submit=utils.input_form()
    with col2:
        if submit==True:
            prediction,probability=utils.predict_survival(p_class,embarkment,gender,age,fare,family_size,siblings,model_path)
            if prediction=="Survived":
                st.markdown(f" #### <span style='color:#FE633D;'>💜 The passenger {title} {name} is predicted to have survived with a survival probability of "+str(probability)+"%</span>",unsafe_allow_html=True)
                st.image("./Assets/alive.png")
            else:
                st.markdown(f" #### <span style='color:#FE633D;'>🧟‍♂️ The passenger {title} {name} is predicted to have not survived with a survival probability of only "+str(probability)+"%</span>",unsafe_allow_html=True)
                st.image("./Assets/dead.png")
            
        else:
            st.markdown(" #### <span style='color:#FE633D;'>👈🏼 Please enter the passenger details and click on the submit button to get the prediction</span>",unsafe_allow_html=True)


st.sidebar.divider()
st.sidebar.markdown("*Get In Touch!*")
with st.sidebar.container():
     utils.sidebar_footer()