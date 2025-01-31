# Quick Start Guide

This guide will help you create your first Multi-Swarm agency in minutes. We'll create a simple agency with two agents that collaborate to analyze data.

## 1. Basic Setup

First, make sure you have Multi-Swarm installed and your API keys configured:

```bash
pip install multi_swarm
```

Create a `.env` file with your API keys:
```env
ANTHROPIC_API_KEY=your_claude_api_key
GOOGLE_API_KEY=your_gemini_api_key
```

## 2. Create Your First Agency

Create a new file `my_agency.py`:

```python
from multi_swarm import Agency, BaseAgent
from dotenv import load_dotenv

load_dotenv()  # Load API keys

# Create the analyst agent
class DataAnalyst(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Data Analyst",
            description="Expert in data analysis and visualization",
            instructions="analyst_instructions.md",
            tools_folder="./tools",
            model="claude-3.5-sonnet",  # Using Claude for technical analysis
            temperature=0.5
        )

# Create the reporter agent
class Reporter(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Reporter",
            description="Specializes in clear communication of findings",
            instructions="reporter_instructions.md",
            tools_folder="./tools",
            model="gemini-2.0-pro",  # Using Gemini for communication
            temperature=0.7
        )

# Create and configure the agency
def create_agency():
    analyst = DataAnalyst()
    reporter = Reporter()
    
    agency = Agency(
        agents=[
            analyst,  # Analyst is the entry point
            [analyst, reporter],  # Analyst can delegate to reporter
        ],
        shared_instructions="agency_manifesto.md"
    )
    
    return agency

if __name__ == "__main__":
    agency = create_agency()
    agency.run_demo()
```

## 3. Create Agent Instructions

Create `analyst_instructions.md`:
```markdown
# Data Analyst Role

Your role is to analyze data and extract insights.

# Goals
1. Process and analyze data accurately
2. Identify key patterns and trends
3. Communicate findings to the reporter

# Process
1. Receive data analysis requests
2. Apply appropriate analytical methods
3. Document findings clearly
4. Delegate report creation to reporter
```

Create `reporter_instructions.md`:
```markdown
# Reporter Role

Your role is to communicate findings clearly.

# Goals
1. Create clear, engaging reports
2. Adapt technical content for the audience
3. Highlight key insights effectively

# Process
1. Receive analysis from analyst
2. Structure information logically
3. Create clear visualizations
4. Present findings in accessible language
```

## 4. Run Your Agency

Run your agency:
```bash
python my_agency.py
```

Example interaction:
```python
response = await agency.process_message("""
Analyze the following sales data and create a report:
2023 Q1: $1.2M
2023 Q2: $1.5M
2023 Q3: $1.8M
2023 Q4: $2.1M
""")
```

## 5. Next Steps

1. **Add Custom Tools**
   - Create tools in the `tools` folder
   - Tools are automatically loaded by agents

2. **Customize Communication**
   - Modify agent instructions
   - Adjust communication flows

3. **Enhance Capabilities**
   - Add more agents
   - Implement specialized tools
   - Fine-tune model parameters

## Common Patterns

1. **Model Selection**
   - Use Claude for technical tasks
   - Use Gemini for creative/communication tasks

2. **Temperature Settings**
   - Lower (0.5) for analytical tasks
   - Higher (0.7) for creative tasks

3. **Communication Flows**
   - Define clear hierarchies
   - Enable necessary collaboration
   - Avoid circular dependencies

## Learn More

- [Creating Agents](../user-guide/creating-agents.md)
- [Creating Tools](../user-guide/creating-tools.md)
- [Communication Flows](../user-guide/communication-flows.md)
- [Example Projects](../examples/dev-agency.md) 