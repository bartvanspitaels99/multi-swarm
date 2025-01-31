# Creating Agencies

Agencies are collections of agents working together to achieve complex goals. This guide explains how to create and configure agencies in Multi-Swarm.

## Basic Agency Structure

```python
from multi_swarm import Agency
from multi_swarm.agents import ManagerAgent, WorkerAgent

def create_agency():
    # Initialize agents
    manager = ManagerAgent()
    worker1 = WorkerAgent()
    worker2 = WorkerAgent()
    
    # Create agency with communication flows
    agency = Agency(
        agents=[
            manager,  # Entry point
            [manager, worker1],  # Manager can talk to worker1
            [manager, worker2],  # Manager can talk to worker2
        ],
        shared_instructions="agency_manifesto.md"
    )
    
    return agency
```

## Agency Components

### 1. Agent List

The first argument to `Agency` is a list defining agents and their communication flows:

```python
agents=[
    entry_point,  # First agent is the entry point
    [agent1, agent2],  # agent1 can communicate with agent2
    [agent2, agent3],  # agent2 can communicate with agent3
]
```

- First agent is the entry point for external communication
- Each sublist defines a one-way communication channel
- Order matters: left agent can initiate communication with right agent

### 2. Shared Instructions

```markdown
# Agency Manifesto

## Agency Description
Description of the agency's purpose and capabilities.

## Mission Statement
Clear statement of the agency's goals and objectives.

## Operating Environment
Description of the context in which the agency operates.

## Shared Guidelines
1. Code quality standards
2. Communication protocols
3. Error handling procedures
4. Performance requirements
```

### 3. Configuration

```python
agency = Agency(
    agents=agent_list,
    shared_instructions="agency_manifesto.md",
    config={
        "max_rounds": 10,  # Maximum conversation rounds
        "timeout": 300,    # Timeout in seconds
        "retry_policy": {
            "max_retries": 3,
            "backoff_factor": 2
        }
    }
)
```

## Communication Patterns

### 1. Hierarchical

```python
# Manager delegates to specialists
agency = Agency([
    manager,
    [manager, specialist1],
    [manager, specialist2],
    [manager, specialist3],
])
```

### 2. Pipeline

```python
# Sequential processing
agency = Agency([
    intake,
    [intake, processor],
    [processor, validator],
    [validator, publisher],
])
```

### 3. Peer-to-Peer

```python
# Agents can communicate freely
agency = Agency([
    coordinator,
    [peer1, peer2],
    [peer2, peer1],
    [peer2, peer3],
    [peer3, peer1],
])
```

## Advanced Features

### 1. Message Routing

```python
class CustomAgency(Agency):
    async def route_message(self, message: str, from_agent: str, to_agent: str):
        """Custom message routing logic."""
        # Preprocess message
        processed = await self._preprocess(message)
        
        # Route message
        response = await self._route(processed, from_agent, to_agent)
        
        # Postprocess response
        return await self._postprocess(response)
```

### 2. State Management

```python
class StatefulAgency(Agency):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.conversation_history = []
        self.metrics = {}
    
    async def process_message(self, message: str):
        # Track conversation
        self.conversation_history.append(message)
        
        # Process message
        response = await super().process_message(message)
        
        # Update metrics
        self._update_metrics(message, response)
        return response
```

### 3. Event Handlers

```python
class EventDrivenAgency(Agency):
    async def on_start(self):
        """Called when agency starts."""
        await self._initialize_resources()

    async def on_message(self, message: str):
        """Called for each message."""
        await self._log_message(message)

    async def on_error(self, error: Exception):
        """Called when an error occurs."""
        await self._handle_error(error)

    async def on_shutdown(self):
        """Called when agency stops."""
        await self._cleanup_resources()
```

## Running Agencies

### 1. Interactive Mode

```python
# Run in interactive mode
agency = create_agency()
agency.run_demo()
```

### 2. Programmatic Usage

```python
async def process_tasks(agency, tasks):
    results = []
    for task in tasks:
        response = await agency.process_message(task)
        results.append(response)
    return results
```

### 3. Background Processing

```python
async def run_background_tasks(agency):
    agency.start_background_processing()
    try:
        while True:
            task = await get_next_task()
            await agency.queue_task(task)
    finally:
        await agency.stop_background_processing()
```

## Best Practices

1. **Agency Design**
   - Clear communication flows
   - Appropriate agent roles
   - Efficient task distribution
   - Error handling strategy

2. **Performance**
   - Monitor response times
   - Track token usage
   - Implement caching
   - Handle rate limits

3. **Reliability**
   - Implement retries
   - Handle failures gracefully
   - Monitor agent health
   - Log important events

4. **Scalability**
   - Design for growth
   - Monitor resource usage
   - Implement load balancing
   - Consider cost optimization

## Common Patterns

### 1. Development Agency

```python
def create_dev_agency():
    manager = ProjectManager()
    backend = BackendDev()
    frontend = FrontendDev()
    
    return Agency([
        manager,
        [manager, backend],
        [manager, frontend],
        [backend, frontend],
    ])
```

### 2. Analysis Agency

```python
def create_analysis_agency():
    coordinator = AnalysisCoordinator()
    collector = DataCollector()
    analyst = DataAnalyst()
    reporter = Reporter()
    
    return Agency([
        coordinator,
        [coordinator, collector],
        [collector, analyst],
        [analyst, reporter],
    ])
```

### 3. Support Agency

```python
def create_support_agency():
    support = SupportAgent()
    technical = TechnicalExpert()
    docs = DocumentationAgent()
    
    return Agency([
        support,
        [support, technical],
        [support, docs],
        [technical, docs],
    ])
```

## Testing

```python
async def test_agency():
    agency = create_test_agency()
    
    # Test basic functionality
    response = await agency.process_message("Test message")
    assert response is not None
    
    # Test communication flows
    response = await agency.process_message(
        "Task for worker",
        from_agent="manager",
        to_agent="worker"
    )
    assert response is not None
    
    # Test error handling
    try:
        await agency.process_message(None)
    except ValueError:
        print("Error handled correctly")
```

## Learn More

- [Agency API Reference](../api/agency.md)
- [Communication Flows](communication-flows.md)
- [Example Projects](../examples/dev-agency.md)
- [Advanced Patterns](advanced-patterns.md) 