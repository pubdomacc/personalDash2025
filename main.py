import streamlit as st

#global varibles

page_State = None

if "page_State" not in st.session_state:
	st.session_state.page_State = None

#st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")


#Functions
def mainFunc():
	return 0;

#To format and control main page

st.header ("WELCOME")


#st.Page
#(page, *, title=None, icon=None, url_path=None, default=False)
inputForm = st.Page("DataInput/InputForm.py",title="Daily Input Form") 
Dashboard = st.Page("DataDisplay/Dashboard.py",title="Daily Dashboard")

#If pressed the state would be True
if (st.button("Input Data")) :
	st.session_state.page_State = "InputForm"
	st.write("Will Input Data Here")
	#will call input data form page here
	pg = st.navigation ([inputForm])
	pg.run()

if (st.button("Go to Dashboard")) :
	st.session_state.page_State = "Dashboard"
	st.write("Will Go to Dashboard page")
	#will call dashboard data here
	pg = st.navigation([Dashboard])
	pg.run()
