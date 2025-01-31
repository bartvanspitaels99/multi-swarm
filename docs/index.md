# Multi-Swarm Framework

Multi-Swarm is a powerful framework for creating collaborative AI agents using multiple LLM providers. It allows you to leverage the unique strengths of different language models like Claude and Gemini in a coordinated system.

## Key Features

- **Multi-LLM Support**: Seamlessly integrate multiple LLM providers (Claude and Gemini) in your agent swarms
- **Flexible Agent Architecture**: Create custom agents with specific roles and capabilities
- **Structured Communication**: Define clear communication flows between agents
- **Easy Integration**: Simple API for creating and running agent swarms
- **Built-in Monitoring**: Track performance, costs, and usage across different providers

## Quick Example

```python
from multi_swarm import Agency, CEOAgent, TrendsAnalyst

# Initialize agents
ceo = CEOAgent()  # Uses Gemini 2.0 Pro
analyst = TrendsAnalyst()  # Uses Claude 3.5 Sonnet

# Create agency with communication flows
agency = Agency(
    agents=[
        ceo,  # CEO is the entry point
        [ceo, analyst],  # CEO can delegate to analyst
    ],
    shared_instructions="agency_manifesto.md"
)

# Run the agency
agency.run_demo()
```

## Installation

```bash
pip install multi_swarm
```

## Environment Setup

Create a `.env` file in your project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
ANTHROPIC_API_KEY=your_claude_api_key
```

## Why Multi-Swarm?

1. **Leverage Model Strengths**: Different LLMs excel at different tasks. Multi-Swarm lets you use each model where it performs best.

2. **Structured Collaboration**: Define clear roles and communication paths between agents, ensuring efficient coordination.

3. **Production Ready**: Built with monitoring, error handling, and scalability in mind.

4. **Easy to Extend**: Create custom agents and tools to fit your specific needs.

## Getting Started

Check out our [Quick Start Guide](getting-started/quickstart.md) to create your first agent swarm, or dive into the [Examples](examples/dev-agency.md) to see Multi-Swarm in action.

## Contributing

We welcome contributions! See our [Contributing Guide](contributing.md) for details on how to get involved. 