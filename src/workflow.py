from langgraph.graph import StateGraph
from typing import TypedDict
from src.retriever import get_results
from src.llm import generate_answer
from src.hitl import check_escalation

class GraphState(TypedDict):
    query: str
    answer: str

def build_graph(db):

    def process_node(state: GraphState):
        query = state["query"]

        results = get_results(db, query)
        answer, context = generate_answer(results, query)

        final_answer = check_escalation(answer, context, results, query)

        return {
            "query": query,
            "answer": final_answer
        }

    def output_node(state: GraphState):
        return state

    workflow = StateGraph(GraphState)

    workflow.add_node("process", process_node)
    workflow.add_node("output", output_node)

    workflow.set_entry_point("process")
    workflow.add_edge("process", "output")

    return workflow.compile()