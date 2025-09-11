from agent.prompts import *
import sympy
import re
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model

def sympy_code_generator_and_executor(query: str) -> dict:
    """
    Solve a mathematical query by generating and executing Sympy code.

    - Use this tool only for **numerical problem solving** (e.g., arithmetic, algebra, calculus, roots, equations).
    - Do NOT use this tool for conceptual/theoretical explanations.
    - The input is a math problem in natural language (string).
    - The tool will:
        1. Generate Sympy code relevant to the query.
        2. Execute the code safely.
        3. Return the result.
    - The output is always a dictionary with a key "Final_Result" containing a strictly **numerical value**.
      Example: {"Final_Result": 42.5}
    """
    # math_plan = math_agent(query)

    # # math_plan = state['math_plan']

    code_generation_prompt = sympy_executor_prompt(query)

    import re
    llm=init_chat_model("groq:openai/gpt-oss-120b")

    # Step 1: Generate Sympy code
    sympy_code = llm.invoke(code_generation_prompt).content

    import json 

    sympy_code = json.loads(sympy_code)

    sympy_code = sympy_code.get('generated_code', "no code found")

    # Step 2: Clean the code (remove markdown fencing if present)
    sympy_code_cleaned = re.sub(r"^```python\n|```$", "", sympy_code, flags=re.MULTILINE).strip()

    # print("Generated Sympy Code:\n", sympy_code_cleaned)

    # Step 3: Execute the generated Sympy code safely
    global_vars = {"sympy": sympy}
    local_vars = {}

    try:
        exec(sympy_code_cleaned, local_vars)
        FINAL_RESULT = local_vars.get("final_answer", "No result found.")
    except Exception as e:
        FINAL_RESULT = f"Execution Error: {e}"

    print("Final Result:", FINAL_RESULT)

    return {"Final_Result": FINAL_RESULT}
