from browser_use import Agent, ChatGoogle, ChatOpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    llm = ChatGoogle(model ="gemini-flash-latest")
    task = "Find the software engineer related jobs at oklo official website"
    agent = Agent(task=task, llm=llm)
    await agent.run()

if __name__ == "__main__":
    history = asyncio.run(main())
    print(history.structured_output)
