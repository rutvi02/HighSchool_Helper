from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class SympyStep(BaseModel):
    description: str = Field(
        description="A plain language explanation of the step (e.g., 'Represent the quadratic equation')."
    )
    sympy_hint: str = Field(
        description="The Sympy construct or function that could be used for this step (e.g., 'Eq(x**2 + 5*x + 6, 0)', 'solve', 'integrate')."
    )

class MathPlan(BaseModel):
    problem_understanding: str = Field(
        description="Restate the problem clearly in your own words."
    )
    variables: Dict[str, str] = Field(
        description="A dictionary of known and unknown variables, with short descriptions. Example: {'x': 'unknown root of equation', 'a': 'coefficient of x^2'}"
    )
    formula: str = Field(
        description="The relevant formula, theorem, or concept to use. Example: 'Quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / 2a'."
    )
    step_by_step_plan: List[str] = Field(
        description="A list of step-by-step reasoning steps in natural language (without actual computation)."
    )
    sympy_mapping: List[SympyStep] = Field(
        description="A list of steps showing how the reasoning maps to Sympy constructs, e.g., define symbols, set up equations, apply solve."
    )
    next_step: str = Field(
        description="Instruction that another agent should now generate Sympy code and execute it to compute the final answer."
    )
