from typing import TypedDict


class AgentState(TypedDict):
    task: str
    code: str
    error: str
    iterations: int
