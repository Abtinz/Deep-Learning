# LangChain vs Handmade Tool Calling

This folder shows the same agent pattern in two styles:

1. `tool_calling/` using LangChain abstractions  
2. `raw_tool_calling/` using direct provider SDK calls (Ollama-style)

The core loop is the same in both:

1. Send messages to the model  
2. Check for tool calls  
3. Execute a tool  
4. Append the tool result  
5. Repeat until final answer

The main difference is how much boilerplate you write.

## Quick Comparison

| Area | LangChain | Handmade (Raw SDK) |
|---|---|---|
| Tool schema | `@tool` auto-generates JSON schema from function name, type hints, and docstring | You manually write and maintain JSON schema dictionaries |
| Message format | Standardized message classes (`SystemMessage`, `HumanMessage`, `ToolMessage`) | Provider-specific dict format (changes across SDKs/providers) |
| Tool execution | `tool.invoke(args)` with validation/tracing/error-handling patterns | Direct call like `tool(**tool_args)` with fewer safeguards |
| Tool-call structure | Consistent dictionary-style structure across integrations | SDK-specific typed objects (for Ollama: nested attribute access) |
| Tool result correlation | Framework handles provider differences (for example `tool_call_id` needs) | You must handle provider behavior and compatibility yourself |
| Tracing | Framework + decorators make tracing straightforward | More manual tracing setup and maintenance |

## Why This Matters

LangChain reduces repetitive plumbing so you can focus on agent logic.  
Raw SDK code gives full control, but you must handle schema, formatting, provider quirks, and robustness details yourself.

In short:

- Use LangChain for speed, portability, and maintainability.
- Use raw SDK code when you need low-level control and are comfortable managing provider-specific details.

