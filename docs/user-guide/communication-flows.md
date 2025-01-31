# Communication Flows

Communication flows define how agents interact within an agency. This guide explains how to design and implement effective communication patterns in Multi-Swarm.

## Basic Concepts

### 1. Directional Communication

Communication in Multi-Swarm is directional:

```python
agency = Agency([
    manager,  # Entry point
    [manager, worker],  # manager -> worker
    [worker, helper],   # worker -> helper
])
```

- Left agent can initiate communication with right agent
- Communication is one-way unless explicitly bidirectional
- Entry point agent handles external communication

### 2. Message Types

```python
# Direct message
response = await agency.process_message(
    "Analyze this data",
    from_agent="manager",
    to_agent="analyst"
)

# Broadcast message
response = await agency.broadcast_message(
    "System update required",
    from_agent="admin"
)

# Chain message
response = await agency.chain_message(
    "Process this document",
    chain=["intake", "processor", "reviewer"]
)
```

## Communication Patterns

### 1. Hierarchical (Tree)

```python
def create_hierarchical_agency():
    """
    CEO
    ├── Manager1
    │   ├── Worker1
    │   └── Worker2
    └── Manager2
        ├── Worker3
        └── Worker4
    """
    agency = Agency([
        ceo,
        [ceo, manager1],
        [ceo, manager2],
        [manager1, worker1],
        [manager1, worker2],
        [manager2, worker3],
        [manager2, worker4],
    ])
    return agency
```

### 2. Pipeline (Chain)

```python
def create_pipeline_agency():
    """
    Intake -> Processor -> Validator -> Publisher
    """
    agency = Agency([
        intake,
        [intake, processor],
        [processor, validator],
        [validator, publisher],
    ])
    return agency
```

### 3. Hub and Spoke

```python
def create_hub_agency():
    """
    Coordinator (Hub)
    ├── Specialist1
    ├── Specialist2
    ├── Specialist3
    └── Specialist4
    """
    agency = Agency([
        coordinator,
        [coordinator, specialist1],
        [coordinator, specialist2],
        [coordinator, specialist3],
        [coordinator, specialist4],
    ])
    return agency
```

### 4. Mesh Network

```python
def create_mesh_agency():
    """
    Fully connected network of peers
    """
    agency = Agency([
        coordinator,
        [peer1, peer2],
        [peer2, peer1],
        [peer2, peer3],
        [peer3, peer1],
        [peer3, peer2],
    ])
    return agency
```

## Message Handling

### 1. Basic Message Processing

```python
class CustomAgent(BaseAgent):
    async def process_message(self, message: str) -> str:
        # Preprocess
        context = self._build_context(message)
        
        # Generate response
        response = await self._generate_response(context)
        
        # Postprocess
        return self._format_response(response)
```

### 2. Message Routing

```python
class CustomAgency(Agency):
    async def route_message(
        self,
        message: str,
        from_agent: str,
        to_agent: str
    ) -> str:
        # Validate route
        if not self._is_valid_route(from_agent, to_agent):
            raise ValueError("Invalid route")
        
        # Process message
        return await self._process_route(message, from_agent, to_agent)
```

### 3. Message Broadcasting

```python
class BroadcastAgency(Agency):
    async def broadcast(self, message: str, from_agent: str) -> List[str]:
        responses = []
        for agent in self.agents:
            if agent.name != from_agent:
                response = await self.route_message(
                    message,
                    from_agent,
                    agent.name
                )
                responses.append(response)
        return responses
```

## Advanced Features

### 1. Context Sharing

```python
class ContextAwareAgency(Agency):
    def __init__(self):
        super().__init__()
        self.shared_context = {}
    
    async def process_with_context(
        self,
        message: str,
        context: Dict
    ) -> str:
        self.shared_context.update(context)
        response = await self.process_message(message)
        return response
```

### 2. Priority Routing

```python
class PriorityAgency(Agency):
    async def route_message(
        self,
        message: str,
        from_agent: str,
        to_agent: str,
        priority: int = 0
    ) -> str:
        if priority > 0:
            return await self._handle_priority_message(
                message,
                from_agent,
                to_agent,
                priority
            )
        return await super().route_message(message, from_agent, to_agent)
```

### 3. Message Filtering

```python
class FilteredAgency(Agency):
    def __init__(self):
        super().__init__()
        self.filters = []
    
    async def process_message(self, message: str) -> str:
        for filter_fn in self.filters:
            message = filter_fn(message)
        return await super().process_message(message)
```

## Best Practices

1. **Clear Communication Paths**
   - Define explicit routes
   - Avoid circular dependencies
   - Document flow patterns

2. **Error Handling**
   ```python
   try:
       response = await agency.process_message(message)
   except CommunicationError as e:
       # Handle communication errors
       await agency.handle_error(e)
   except AgentError as e:
       # Handle agent-specific errors
       await agency.retry_with_backup(message)
   ```

3. **Message Validation**
   ```python
   class ValidatedAgency(Agency):
       def validate_message(self, message: str) -> bool:
           if not message:
               return False
           if len(message) > self.max_length:
               return False
           return True
   ```

4. **Performance Optimization**
   ```python
   class OptimizedAgency(Agency):
       def __init__(self):
           super().__init__()
           self.message_cache = {}
       
       async def process_message(self, message: str) -> str:
           cache_key = self._compute_cache_key(message)
           if cache_key in self.message_cache:
               return self.message_cache[cache_key]
           
           response = await super().process_message(message)
           self.message_cache[cache_key] = response
           return response
   ```

## Common Patterns

### 1. Request-Response

```python
async def request_response(agency, request: str) -> str:
    """Basic request-response pattern."""
    return await agency.process_message(request)
```

### 2. Chain of Responsibility

```python
async def process_chain(agency, message: str, chain: List[str]) -> str:
    """Process message through a chain of agents."""
    result = message
    for agent in chain:
        result = await agency.process_message(
            result,
            to_agent=agent
        )
    return result
```

### 3. Publish-Subscribe

```python
class PubSubAgency(Agency):
    def __init__(self):
        super().__init__()
        self.subscribers = defaultdict(list)
    
    async def publish(self, topic: str, message: str):
        """Publish message to topic subscribers."""
        for subscriber in self.subscribers[topic]:
            await self.route_message(message, "publisher", subscriber)
```

## Testing Communication

```python
async def test_communication():
    agency = create_test_agency()
    
    # Test direct communication
    response = await agency.process_message(
        "Test message",
        from_agent="sender",
        to_agent="receiver"
    )
    assert response is not None
    
    # Test broadcast
    responses = await agency.broadcast_message(
        "Broadcast test",
        from_agent="broadcaster"
    )
    assert len(responses) == len(agency.agents) - 1
    
    # Test chain
    chain_response = await agency.chain_message(
        "Chain test",
        chain=["first", "second", "third"]
    )
    assert chain_response is not None
```

## Learn More

- [Agency Creation](creating-agencies.md)
- [Message Patterns](../api/messages.md)
- [Error Handling](../user-guide/error-handling.md)
- [Performance Tips](../user-guide/performance.md) 