from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from phi.model.anthropic import Claude
from phi.model.openai import OpenAIChat
from phi.agent import Agent
import openai
import phi.api
import os
import phi
from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app 
load_dotenv()
phi.api=os.getenv("PHI_DATA")

llm = OpenAIChat(id="gpt-4o",api_key="OPEN_API_KEY")
web_search_agent=Agent(
    name="web search agent",
    role="Search the web",
    model=llm,
    tools=[DuckDuckGo()],
    instructions=["Always include source"],
    show_tools_calls=True,
    markdown=True,
)
Finance_agent=Agent(
    name="Finance Agent",
    model=llm,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)
#Multi_Ai_Agent=Agent(
 #   team=[web_search_agent,Finance_agent],
  #  instructions=["Always include source and Use tables to display the data"],
   # show_tools_calls=True,
    #markdown=True,
#model=llm,
#)

#Multi_Ai_Agent.print_response("Summarize analyst recommendation and share the latest news for NVDia",stream=True,markdown=True)

app=Playground(agents=[Finance_agent,web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)