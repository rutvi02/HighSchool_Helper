# def main():
#     print("Hello from highschool-helper!")


# if __name__ == "__main__":
#     main()

from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages

from typing import Optional

from pydantic import BaseModel, Field, ConfigDict
import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model

llm=init_chat_model("groq:openai/gpt-oss-120b")

from agent.prompts import *
from agent.tools import sympy_code_generator_and_executor
tools = [sympy_code_generator_and_executor]

llm_with_tool = llm.bind_tools(tools)


from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# System message

from agent.graph import graph


messages = [HumanMessage(content="Find the roots of x^2 - 5x + 6 = 0")]
messages = graph.invoke({"messages": messages})

print(messages['messages'][-1].content)