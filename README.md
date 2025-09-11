# HighSchool Helper

An AI agent that helps solve maths and physics problems using LangChain, LangGraph, and custom tools.
It takes a math/physics problem written in plain English, asks a Large Language Model (LLM) to reason about it, uses a SymPy-based tool to run calculations, and returns the final answer.


**Features**
- Uses an LLM (groq:openai/gpt-oss-120b) for reasoning.
- The tool used generated and executes SymPy code to compute exact solutions.
- This is built on ReAct agent architecture
- Easy to extend with more tools or prompts.

  **Architecture**

  <img width="214" height="250" alt="Screenshot 2025-09-11 at 7 50 47 PM" src="https://github.com/user-attachments/assets/917802ea-a341-4e9b-9ef5-02729bfa5a56" />
