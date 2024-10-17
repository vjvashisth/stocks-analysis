import os
import warnings
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from pydantic import BaseModel
from flask import Flask, request, jsonify

app = Flask(__name__)

# Warning control
warnings.filterwarnings('ignore')

# Initialize the search tool
search_tool = SerperDevTool()

# Define the stock search agent
stock_search_agent = Agent(
    role="Senior Stock Researcher",
    goal="find top 10 performing stocks",
    backstory="Specializing in financial markets, this agent searches for Top 10 stocks.",
    verbose=True,
    allow_delegation=True,
    tools=[search_tool]
)

# Define a Pydantic model for stock details
class StockDetails(BaseModel):
    ticker: list

# Define the task for the agent
search_task = Task(
    description="find top 10 performing stocks.",
    expected_output="current top 10 performing stocks",
    output_json=StockDetails,
    output_file="stock_details.json",
    agent=stock_search_agent
)

# Define the crew with agents and tasks
stock_search_crew = Crew(
    agents=[stock_search_agent],
    tasks=[search_task],
    verbose=True
)

@app.route('/invocations', methods=['POST'])
def invoke_endpoint():
    # Execute the task
    result = stock_search_crew.kickoff()
    return jsonify({"result": result})

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "Healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)