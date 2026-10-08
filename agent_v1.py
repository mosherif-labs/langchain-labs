from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()  # finds mosherif-labs/.env by searching up from this folder


def get_weather(city: str) -> str:
    """Get the weather for a city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="claude-sonnet-4-6",
    tools=[get_weather],
    system_prompt="You are a helpful assistant.",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What is the weather in SF and in Paris?"}]}
)
print(result["messages"][-1].content_blocks)
