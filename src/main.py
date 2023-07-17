import streamlit as st
import pickle
from configparser import ConfigParser
import utils
import base64

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
model_path=config_object["MODEL"]["model_path"]


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
        st.sidebar.image(logo)
        st.sidebar.image('./Assets/sidebanner.png')




    

st.sidebar.markdown("*Get In Touch!*")
with st.sidebar.container():
     utils.sidebar_footer()



linkedin_link=config_object["Contact"]["linkedin_link"]
linkedin_icon=config_object["Contact"]["linkedin_icon"]

twitter_link=config_object["Contact"]["twitter_link"]
twitter_icon=config_object["Contact"]["twitter_icon"]

email_link=config_object["Contact"]["email_link"]
email_icon=config_object["Contact"]["email_icon"]


#----Header has link to code repository----#
github_repo=config_object["Contact"]["github_repo"]
github_icon=config_object["Contact"]["github_icon"]


with st.container():
    col1,col2,col3=st.columns([1,10,1])
    with col2:
        #----Header Image-----#
        st.image(header_image)
        #----Social Links-----#
        st.markdown(f"<h6 style='text-align:right;'><a href={github_repo}><img src={github_icon} alt='github' style='width:42px;height:42px;'></a>&emsp;&emsp;<a href={linkedin_link}><img src={linkedin_icon} alt='linkedin' style='width:42px;height:42px;'></a>&emsp;&emsp;<a href={twitter_link}><img src={twitter_icon} alt='twitter' style='width:42px;height:42px;'></a>&emsp;&emsp;<a href={email_link}><img src={email_icon} alt='email' style='width:42px;height:42px;'></a></h6>",unsafe_allow_html=True)

with st.container():
    col1,col2=st.columns(2)
    with col1:
        with st.container():
            p_class,embarkment,gender,age,fare,family_size,siblings,submit=utils.input_form()

    with col2:
        with st.container():
            prediction=utils.predict_survival(p_class,embarkment,gender,age,fare,family_size,siblings,model_path)
            st.write(prediction)



