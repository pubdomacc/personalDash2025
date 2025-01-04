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
	"fat" : None,
	"water" : None,
	"muscle" : None
}

with st.form(key="duf_workout") :
	duf_data_input["date"] = st.date_input("What's today's date?", max_value = "today", format="YYYY-MM-DD")
	duf_data_input["weight"] = st.number_input("Enter your morning weight :")
	duf_data_input["fat"] = st.number_input("Enter your morning fat % :")
	duf_data_input["water"] = st.number_input("Enter your morning water % :")
	duf_data_input["muscle"] = st.number_input("Enter your morning muscle % :")
	

	submit_button = st.form_submit_button("Submit Data")
	if submit_button :
		if not all(duf_data_input.values()):
		#if (duf_data_input.values()).contains(None):
			st.warning("Please fill in all the fields")
		else : 
			st.success ("Thank you for today's input!")
			st.balloons()
			st.write("#### Info :")
			for (key,value) in duf_data_input.items() :
				st.write(key, " : ", value)
