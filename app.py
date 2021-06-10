import streamlit as st 

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Basic Calculator")
#a = st.sidebar.text_input("Enter first number")
#b = st.sidebar.number_input("Enter first number")
a = st.slider("Enter second number",0,100)
b = st.slider("Enter second number",0,100)
select = st.selectbox("How would you like to do?",("Addition", "Subtraction","Multiplication","Division"))
if select == "Addition":
  calc = int(a)+int(b)
elif select == "Subtraction":
    calc = int(a)-int(b)
elif select == "Multiplication":
    calc = int(a)*int(b)
elif select == "Division":
    calc = int(a)/int(b)
if st.button("CALCULATE"):
    st.sidebar.title(f"The {select} of {a} and {b} is {calc}")
