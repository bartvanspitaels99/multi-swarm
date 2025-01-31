# Multi-Swarm Framework

[![PyPI version](https://badge.fury.io/py/multi-swarm.svg)](https://badge.fury.io/py/multi-swarm)
[![CI](https://github.com/bartvanspitaels99/multi-swarm/actions/workflows/ci.yml/badge.svg)](https://github.com/bartvanspitaels99/multi-swarm/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/bartvanspitaels99/multi-swarm/branch/main/graph/badge.svg)](https://codecov.io/gh/bartvanspitaels99/multi-swarm)
[![Python Versions](https://img.shields.io/pypi/pyversions/multi-swarm.svg)](https://pypi.org/project/multi-swarm/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A powerful framework for creating collaborative AI agent swarms, leveraging multiple LLM providers including Claude and Gemini.

## Features

- Create collaborative agent swarms with distinct roles and capabilities
- Support for multiple LLM providers (Claude and Gemini)
- Easy-to-use agent template creation
- Flexible agency configuration
- Built-in tools system
- Asynchronous communication between agents

## Installation

```bash
pip install multi-swarm
```

For development installation with testing tools:

```bash
pip install multi-swarm[dev]
```

## Quick Start

1. Set up your environment variables:

```bash
# .env
ANTHROPIC_API_KEY=your_claude_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

2. Create a simple agency:

```python
from multi_swarm import Agency, CEO, TrendsAnalyst

def create_agency():
    # Initialize agents
    ceo = CEO()
    analyst = TrendsAnalyst()

    # Create agency with communication flows
    agency = Agency(
        agents=[
            ceo,  # Entry point for user communication
            [ceo, analyst],  # CEO can communicate with analyst
        ],
        shared_instructions="agency_manifesto.md"
    )
    
    return agency

if __name__ == "__main__":
    # Create and run the agency
    agency = create_agency()
    agency.run_demo()
```

## Advanced Usage Examples

### 1. Creating a Custom Agent with Tools

```python
import os
from typing import Dict, Any
from multi_swarm.core.base_agent import BaseAgent
from pydantic import BaseModel

# Define a custom tool
class MarketAnalysisTool(BaseModel):
    """Tool for analyzing market data."""
    market: str
    timeframe: str
    metrics: list[str]

    def run(self) -> Dict[str, Any]:
        # Implement your market analysis logic here
        return {
            "market": self.market,
            "analysis": {
                "trend": "bullish",
                "confidence": 0.85
            }
        }

class MarketAnalyst(BaseAgent):
    """An agent specialized in market analysis."""
    
    def __init__(self):
        super().__init__(
            name="MarketAnalyst",
            description="Specialized in analyzing market trends and patterns",
            instructions=os.path.join(os.path.dirname(__file__), "instructions.md"),
            tools_folder=os.path.join(os.path.dirname(__file__), "tools"),
            model="claude-3-sonnet",
            temperature=0.7
        )
        self.register_tool("market_analysis", MarketAnalysisTool)
```

### 2. Complex Agency with Multiple Communication Flows

```python
from multi_swarm import Agency, CEO, TrendsAnalyst
from custom_agents import MarketAnalyst, DataScientist, Strategist

def create_complex_agency():
    # Initialize agents
    ceo = CEO()
    analyst = TrendsAnalyst()
    market_analyst = MarketAnalyst()
    data_scientist = DataScientist()
    strategist = Strategist()

    # Create agency with complex communication flows
    agency = Agency(
        agents=[
            ceo,  # Entry point
            [ceo, analyst],  # CEO -> Analyst
            [ceo, strategist],  # CEO -> Strategist
            [analyst, market_analyst],  # Analyst -> Market Analyst
            [analyst, data_scientist],  # Analyst -> Data Scientist
            [strategist, market_analyst],  # Strategist -> Market Analyst
            [strategist, data_scientist],  # Strategist -> Data Scientist
        ],
        shared_instructions="agency_manifesto.md"
    )
    
    return agency
```

### 3. Asynchronous Agency Operation

```python
import asyncio
from multi_swarm import Agency, CEO, TrendsAnalyst

async def process_tasks(agency: Agency, tasks: list[str]):
    """Process multiple tasks concurrently through the agency."""
    async def process_task(task: str):
        response = await agency.process_message(task)
        return {"task": task, "response": response}
    
    # Process all tasks concurrently
    results = await asyncio.gather(
        *[process_task(task) for task in tasks]
    )
    return results

# Usage
async def main():
    agency = create_agency()
    tasks = [
        "Analyze market trends for AI sector",
        "Predict emerging technologies in 2024",
        "Evaluate competitor strategies"
    ]
    
    results = await process_tasks(agency, tasks)
    for result in results:
        print(f"Task: {result['task']}")
        print(f"Response: {result['response']}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

### 4. Custom Instructions and Tools Loading

```python
from multi_swarm import Agency, BaseAgent
import yaml

def load_agent_config(config_path: str) -> dict:
    """Load agent configuration from YAML file."""
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

class ConfigurableAgent(BaseAgent):
    """An agent that can be configured via YAML files."""
    
    def __init__(self, config_path: str):
        config = load_agent_config(config_path)
        super().__init__(
            name=config["name"],
            description=config["description"],
            instructions=config["instructions_path"],
            tools_folder=config["tools_folder"],
            model=config["model"],
            temperature=config["temperature"]
        )
        
        # Load custom tools
        for tool in config.get("tools", []):
            self.load_tool(tool["name"], tool["path"])

# Example config.yaml:
"""
name: CustomAgent
description: A configurable agent
instructions_path: ./instructions.md
tools_folder: ./tools
model: claude-3-sonnet
temperature: 0.7
tools:
  - name: market_analysis
    path: ./tools/market_analysis.py
  - name: data_processing
    path: ./tools/data_processing.py
"""
```

## Creating Custom Agents

1. Create a new agent template:

```python
from multi_swarm.agency import create_agent_template

create_agent_template(
    name="CustomAgent",
    description="A custom agent for specific tasks",
    path="./custom_agent"
)
```

2. Implement the agent class:

```python
import os
from multi_swarm.core.base_agent import BaseAgent

class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CustomAgent",
            description="A custom agent for specific tasks",
            instructions=os.path.join(os.path.dirname(__file__), "instructions.md"),
            tools_folder=os.path.join(os.path.dirname(__file__), "tools"),
            model="claude-3-sonnet",  # or "gemini-2.0-pro"
            temperature=0.7
        )
```

## Documentation

For detailed documentation, please visit our [GitHub repository](https://github.com/bartvanspitaels99/multi-swarm).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Here are some ways you can contribute:

- Add new agent types
- Implement useful tools
- Improve documentation
- Add tests
- Report bugs
- Suggest features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 