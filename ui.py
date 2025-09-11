import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.messages import HumanMessage
from agent.graph import graph

# ---- Page config ----
st.set_page_config(
    page_title="HighSchool Helper",
    page_icon="🎓",
    layout="centered",
)

# ---- Custom CSS for aesthetics ----
st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(to bottom right, #fdfbfb, #ebedee);
    }
    .stTextArea textarea {
        border-radius: 12px;
        font-size: 1.1rem;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-size: 1.1rem;
        padding: 0.5rem 1.2rem;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .result-box {
        background: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 6px rgba(0,0,0,0.1);
        font-size: 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- App title ----
st.title("🎓 HighSchool Helper")
st.subheader("Solve Math & Physics Problems Instantly")

# ---- Input box ----
problem = st.text_area(
    "Enter your problem:",
    placeholder="e.g., Find the roots of x^2 - 5x + 6 = 0 or Calculate the velocity of a 2kg mass sliding down an incline...",
    height=120,
)

# ---- Submit button ----
if st.button("Solve"):
    if problem.strip():
        with st.spinner("Thinking..."):
            try:
                # Pass message to your agent
                response = graph.invoke({"messages": [HumanMessage(content=problem)]})
                answer = response["messages"][-1].content
                st.markdown(f"<div class='result-box'>{answer}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a problem to solve.")
