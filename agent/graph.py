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

from agent.states import *
from agent.prompts import *
from agent.tools import sympy_code_generator_and_executor
tools = [sympy_code_generator_and_executor]

llm_with_tool = llm.bind_tools(tools)

## Stategraph
from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
# System message
sys_msg = SystemMessage(content=agent_promt())

# Node
def assistant(state: MessagesState):
   return {"messages": [llm_with_tool.invoke([sys_msg] + state["messages"])]}

from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Graph
builder = StateGraph(MessagesState)

# Define nodes: these do the work
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# Define edges: these determine the control flow
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
    "assistant",
    # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
    # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
    tools_condition,
)
builder.add_edge("tools", "assistant")
graph = builder.compile()
