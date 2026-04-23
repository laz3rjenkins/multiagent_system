from langgraph.graph import StateGraph, END

from state import AgentState

# 4. Логика графа
def should_continue(state: AgentState):
    if not state['error'] or state['iterations'] >= 3:
        return "end"
    return "continue"


# Сборка
workflow = StateGraph(AgentState)
workflow.add_node("coder", coder_node)
workflow.add_node("tester", tester_node)
workflow.set_entry_point("coder")
workflow.add_edge("coder", "tester")
workflow.add_conditional_edges("tester", should_continue, {"continue": "coder", "end": END})

if __name__ == "__main__":
    app = workflow.compile()

    # ЗАПУСК
    task = "Проанализируй все логи в ./logs и выпиши ошибки в summary.md"
    result = app.invoke({"task": task, "code": "", "error": "", "iterations": 0})

    print("\n=== ИТОГОВЫЙ КОД ===")
    print(result['code'])
