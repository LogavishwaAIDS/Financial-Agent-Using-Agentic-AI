from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from phi.model.anthropic import Claude
from phi.agent import Agent
llm = Claude(id="claude-3-5-sonnet-20240620",api_key="OPEN_API_KEY")

web_search_agent=Agent(
    name="web search agent",
    role="Search the web",
    model=llm,
    tools=[DuckDuckGo()],
    instructions=["Always include source"],
    show_tools_calls=True,
    markdown=True,
)
print("A1")
Finance_agent=Agent(
    name="Finance Agent",
    model=llm,
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)
print("A2")
Multi_Ai_Agent=Agent(
    team=[web_search_agent,Finance_agent],
    instructions=["Always include source and Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
model=llm,
)
print("A3")

Multi_Ai_Agent.print_response("Summarize analyst recommendation and share the latest news for NVDia",
stream=True,
markdown=True)
#
# response = Multi_Ai_Agent.run('Share a quick healthy breakfast recipe.', stream=False)
# print(response)