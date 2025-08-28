import os
import json
from openai import OpenAI

def add(a: int, b: int) -> int:
    """
    Adds two numbers together.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    print(f"Executing tool: add({a}, {b})")
    return a + b

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")
client = OpenAI(api_key=api_key)
print("Setup complete. Client created.")

tools = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "Adds two numbers together.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "The first number."},
                    "b": {"type": "integer", "description": "The second number."}
                },
                "required": ["a", "b"]
            }
        }
    }
]

user_prompt = "What is 5 plus 7?"
print(f"\nUser prompt: '{user_prompt}'")
print("Sending request to OpenAI to see which tool to use...")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_prompt}],
    tools=tools,
    tool_choice="auto"
)

response_message = response.choices[0].message
if response_message.tool_calls:
    print("\nModel wants to use a tool. Executing...")

    # For this homework, we'll just handle the first tool call
    tool_call = response_message.tool_calls[0]
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)

    # --- Call the appropriate function based on the name ---
    if function_name == "add":
        function_result = add(
            a=function_args.get("a"),
            b=function_args.get("b")
        )
    else:
        # In a real app, you might have many more functions
        raise ValueError(f"Unknown function: {function_name}")

    print(f"Tool '{function_name}' executed. Result: {function_result}")

    # --- Send the tool result back to the model ---
    print("\nSending tool result back to the model for the final answer...")

    # We need to build the history of the conversation
    messages = [
        {"role": "user", "content": user_prompt},  # The original prompt
        response_message,  # The model's first response (the tool call)
        {
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": function_name,
            "content": str(function_result),  # The result of our function
        },
    ]

    second_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,  # We send the full conversation history
    )

    final_answer = second_response.choices[0].message.content
    print(f"\nFinal Answer from AI: {final_answer}")

else:
    # If the model didn't use a tool, just print its response
    final_answer = response_message.content
    print(f"\nFinal Answer from AI: {final_answer}")