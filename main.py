import streamlit as st
st.write ("Hello world")

def mainFunc():
	#If pressed the state would be True
	if (st.button("Input Data")) :

		st.write("Will Input Data Here")

	if (st.button("Go to Dashboard")) :
		st.write("Will Go to Dashboard page")


st.title("Daily Update Form - Workout")

duf_data_input = {
	"date" : None,
	"weight" : None,
	"fat%" : None,
	"water%" : None,
	"muscle%" : None
}

with st.form(key="duf_workout") :
	duf_input_Date = st.date_input("What's today's date?")
	duf_input_weight = st.number_input("Enter your morning weight :")
	duf_input_fat = st.number_input("Enter your morning fat % :")
	duf_input_water = st.number_input("Enter your morning water % :")
	duf_input_muscle = st.number_input("Enter your morning muscle % :")
	

	submit_button = st.form_submit_button("Submit")
