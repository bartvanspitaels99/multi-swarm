# Creating Agents

This guide explains how to create custom agents in Multi-Swarm. Agents are the core building blocks of your AI system, each with specific roles and capabilities.

## Basic Agent Structure

Every agent inherits from the `BaseAgent` class:

```python
from multi_swarm import BaseAgent

class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Custom Agent",
            description="Description of the agent's role",
            instructions="path/to/instructions.md",
            tools_folder="./tools",
            model="claude-3.5-sonnet",
            temperature=0.5
        )
```

## Required Parameters

1. **name** (str)
   - Unique identifier for the agent
   - Should be descriptive of the role
   - Used in logging and debugging

2. **description** (str)
   - Detailed description of the agent's purpose
   - Helps other agents understand its role
   - Used in communication flows

3. **instructions** (str)
   - Path to the markdown file containing agent instructions
   - Defines behavior and responsibilities
   - Can be updated without changing code

4. **tools_folder** (str)
   - Directory containing agent-specific tools
   - Tools are automatically loaded
   - Can be shared between agents

5. **model** (str)
   - LLM model to use (e.g., "claude-3.5-sonnet", "gemini-2.0-pro")
   - Chosen based on task requirements
   - Affects capabilities and costs

6. **temperature** (float)
   - Controls response randomness
   - 0.0 to 1.0 range
   - Lower for technical tasks, higher for creative tasks

## Optional Parameters

```python
class AdvancedAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Advanced Agent",
            model="claude-3.5-opus",
            provider_config={
                "api_version": "2024-03",
                "max_tokens": 4096,
                "top_p": 0.9,
                "top_k": 50
            },
            retry_config={
                "max_retries": 3,
                "backoff_factor": 2,
                "retry_on": ["rate_limit", "server_error"]
            },
            streaming=True
        )
```

1. **provider_config** (dict)
   - Model-specific configuration
   - API versions
   - Token limits
   - Safety settings

2. **retry_config** (dict)
   - Error handling settings
   - Retry attempts
   - Backoff strategy
   - Error types to retry on

3. **streaming** (bool)
   - Enable/disable response streaming
   - Default: False
   - Useful for long responses

## Creating Instructions

Instructions are markdown files that define agent behavior:

```markdown
# Agent Role

Detailed description of the agent's role and purpose.

# Goals

1. Primary objective
2. Secondary objectives
3. Success criteria

# Process Workflow

1. Step-by-step process
2. Decision points
3. Interaction guidelines

# Communication Guidelines

1. How to interact with other agents
2. Message formatting
3. Response expectations
```

## Advanced Features

### 1. Custom Message Processing

```python
class CustomProcessor(BaseAgent):
    async def process_message(self, message: str) -> str:
        """Override default message processing."""
        # Custom preprocessing
        processed = await self._preprocess(message)
        
        # Get model response
        response = await self._generate_response(processed)
        
        # Custom postprocessing
        return await self._postprocess(response)
```

### 2. State Management

```python
class StatefulAgent(BaseAgent):
    def __init__(self):
        super().__init__(name="Stateful Agent")
        self.conversation_history = []
        self.context = {}
    
    async def process_message(self, message: str) -> str:
        # Update state
        self.conversation_history.append(message)
        
        # Process with context
        response = await super().process_message(
            self._build_context(message)
        )
        
        # Update state with response
        self.conversation_history.append(response)
        return response
```

### 3. Event Handlers

```python
class EventAwareAgent(BaseAgent):
    async def on_start(self):
        """Called when agent starts."""
        await self._load_resources()

    async def on_error(self, error: Exception):
        """Called on processing error."""
        await self._log_error(error)

    async def on_shutdown(self):
        """Called when agent stops."""
        await self._cleanup_resources()
```

## Best Practices

1. **Role Clarity**
   - Give agents focused responsibilities
   - Avoid overlapping roles
   - Clear communication patterns

2. **Model Selection**
   - Match model to task requirements
   - Consider cost-performance trade-offs
   - Use appropriate temperature settings

3. **Error Handling**
   - Implement comprehensive error handling
   - Use retry mechanisms
   - Log errors for debugging

4. **Resource Management**
   - Clean up resources properly
   - Monitor token usage
   - Implement rate limiting

## Common Patterns

### 1. Specialist Agent

```python
class SpecialistAgent(BaseAgent):
    """Agent focused on a specific domain."""
    def __init__(self):
        super().__init__(
            name="Security Expert",
            model="claude-3.5-sonnet",
            temperature=0.3  # Low for precise analysis
        )
```

### 2. Coordinator Agent

```python
class CoordinatorAgent(BaseAgent):
    """Agent that manages other agents."""
    def __init__(self):
        super().__init__(
            name="Project Coordinator",
            model="gemini-2.0-pro",
            temperature=0.7  # Higher for creative planning
        )
```

### 3. Pipeline Agent

```python
class PipelineAgent(BaseAgent):
    """Agent that processes data in stages."""
    def __init__(self):
        super().__init__(
            name="Data Pipeline",
            model="claude-3.5-sonnet",
            streaming=True  # Enable for large datasets
        )
```

## Testing Agents

```python
async def test_agent():
    agent = CustomAgent()
    
    # Test basic functionality
    response = await agent.process_message("Test message")
    assert response is not None
    
    # Test error handling
    try:
        await agent.process_message(None)
    except ValueError:
        print("Error handled correctly")
    
    # Test with different inputs
    test_cases = ["case1", "case2", "case3"]
    for case in test_cases:
        response = await agent.process_message(case)
        validate_response(response)
```

## Learn More

- [Creating Tools](creating-tools.md)
- [Communication Flows](communication-flows.md)
- [API Reference](../api/agents.md)
- [Example Projects](../examples/dev-agency.md) 