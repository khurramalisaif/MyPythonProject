import streamlit as st

st.set_page_config(
    page_title="Quantum Calc",
    page_icon="🧮",
    layout="centered"
)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

st.markdown("<h1 style='text-align:center; color:#2563eb;'>🧮 Quantum Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#6b7280;'>Perform basic arithmetic operations</p>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    first_value = st.number_input("Enter first number", value=0.0, step=1.0)
with col2:
    second_value = st.number_input("Enter second number", value=0.0, step=1.0)

operation = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = add_numbers(first_value, second_value)
    elif operation == "Subtraction":
        result = subtract_numbers(first_value, second_value)
    elif operation == "Multiplication":
        result = multiply_numbers(first_value, second_value)
    elif operation == "Division":
        result = divide_numbers(first_value, second_value)

if result is not None:
    st.markdown(f"<h2 style='text-align:center; color:#16a34a;'>Result: {result}</h2>", unsafe_allow_html=True)
