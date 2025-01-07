import streamlit as st

st.write("Form Input goes here")

if st.button("Home Button") :
	st.write("Goes Home")


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
	"muscle" : None,
	"exercise_status" : None,
	"exercise_type" : None
}

with st.form(key="duf_workout") :
	duf_data_input["date"] = st.date_input("What's today's date?", max_value = "today", format="YYYY-MM-DD")
	duf_data_input["weight"] = st.number_input("Enter your morning weight :")
	duf_data_input["fat"] = st.number_input("Enter your morning fat % :")
	duf_data_input["water"] = st.number_input("Enter your morning water % :")
	duf_data_input["muscle"] = st.number_input("Enter your morning muscle % :")
	duf_data_input["exercise_status"] = st.radio(
	    "Did you Workout today?",
	    [":rainbow[YES!]", "Nope"],
	    index=None,
		)
	duf_data_input["exercise_type"] = st.multiselect(
	    "Choose exercises you've done today",
	    ["Treadmill/Cardio", "Morning Walk", "Body Weight", "Yoga", "Weights exercise"],
	    ["Morning Walk", "Weights exercise"],
		)	



	submit_button = st.form_submit_button("Submit Data")
	st.write("state : ", submit_button)
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
			#st.write("#### multiselect output test :")
			#for i in options :
			#	st.write(i, " ")
			#st.write("#### radio output test : ", exercise)
							
