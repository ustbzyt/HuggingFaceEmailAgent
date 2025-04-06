import os
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from agent.nodes import classify_email, draft_response, handle_spam, notify_mr_hugg, read_email, route_email
from models.email_state import EmailState  # Import EmailState

# Instantiate ChatOllama
model = ChatOllama(model="deepseek-r1:7B")  # Replace with your model if needed

# Create the graph
email_graph = StateGraph(EmailState)

# Add nodes, passing the model where needed
email_graph.add_node("read_email", read_email)
email_graph.add_node("classify_email", lambda state: classify_email(state, model))
email_graph.add_node("handle_spam", handle_spam)
email_graph.add_node("generate_draft", lambda state: draft_response(state, model))  # Renamed the node
email_graph.add_node("notify_mr_hugg", notify_mr_hugg)

# Start the edges
email_graph.add_edge(START, "read_email")
# Add edges - defining the flow
email_graph.add_edge("read_email", "classify_email")

# Add conditional branching from classify_email
email_graph.add_conditional_edges(
    "classify_email",
    route_email,
    {
        "spam": "handle_spam",
        "legitimate": "generate_draft"  # Updated the edge target
    }
)

# Add the final edges
email_graph.add_edge("handle_spam", END)
email_graph.add_edge("generate_draft", "notify_mr_hugg")  # Updated the edge source
email_graph.add_edge("notify_mr_hugg", END)

# Compile the graph
compiled_graph = email_graph.compile()
