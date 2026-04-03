# Lang-Graph

This folder focuses on graph-based LLM application design using LangGraph, where workflows are modeled as explicit nodes, edges, and state transitions.

## What LangGraph Means Here

- LangGraph is used to build stateful agent systems as graphs.
- Instead of one linear chain, execution is routed across graph nodes based on rules or model/tool outputs.
- This supports branching logic, tool routing, and memory across turns.

## Core Concepts Implemented

- Graph-state modeling for chatbot flows.
- Conditional routing between nodes.
- Tool-calling inside graph execution.
- Conversation memory in graph applications.

## Projects In This Folder

- `codebasics_tutorial/chatbot.ipynb`
  - Chatbot graph basics.
- `codebasics_tutorial/conditional_graph.ipynb`
  - Conditional branching/routing patterns.
- `codebasics_tutorial/financial_graph.ipynb`
  - Financial analysis graph workflow.
- `codebasics_tutorial/memory_in_langgraph.ipynb`
  - State and memory behavior across turns.
- `codebasics_tutorial/tool_call_stock_price.ipynb`
  - Tool-enabled graph flow for stock-related queries.

## Models and Technologies Referenced

- LangGraph
- LangChain
- `google_genai:gemini-2.0-flash`
- `gpt-3.5-turbo`

