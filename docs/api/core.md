# Core API Reference

This document provides detailed information about the core classes and functions in Multi-Swarm.

## BaseAgent

The foundation class for all agents in Multi-Swarm.

### Constructor

```python
def __init__(
    self,
    name: str,
    description: str,
    instructions: str,
    tools_folder: str,
    model: str,
    temperature: float = 0.7,
    provider_config: Optional[Dict] = None,
    retry_config: Optional[Dict] = None,
    streaming: bool = False
)
```

#### Parameters

- **name** (str): Unique identifier for the agent
- **description** (str): Description of the agent's role
- **instructions** (str): Path to instructions file
- **tools_folder** (str): Path to tools directory
- **model** (str): LLM model identifier
- **temperature** (float, optional): Response randomness (0.0-1.0)
- **provider_config** (Dict, optional): Model-specific settings
- **retry_config** (Dict, optional): Error handling settings
- **streaming** (bool, optional): Enable response streaming

### Methods

#### process_message

```python
async def process_message(
    self,
    message: str,
    **kwargs
) -> str:
    """Process an incoming message and generate a response."""
```

#### load_instructions

```python
def load_instructions(
    self,
    path: str
) -> str:
    """Load agent instructions from file."""
```

#### load_tools

```python
def load_tools(
    self,
    path: str
) -> List[BaseTool]:
    """Load tools from directory."""
```

## Agency

The main class for managing agent interactions.

### Constructor

```python
def __init__(
    self,
    agents: List[Union[BaseAgent, List[BaseAgent]]],
    shared_instructions: str,
    config: Optional[Dict] = None
)
```

#### Parameters

- **agents** (List): Agents and communication flows
- **shared_instructions** (str): Path to shared instructions
- **config** (Dict, optional): Agency configuration

### Methods

#### process_message

```python
async def process_message(
    self,
    message: str,
    from_agent: Optional[str] = None,
    to_agent: Optional[str] = None
) -> str:
    """Process a message through the agency."""
```

#### broadcast_message

```python
async def broadcast_message(
    self,
    message: str,
    from_agent: str
) -> List[str]:
    """Send a message to all agents."""
```

#### chain_message

```python
async def chain_message(
    self,
    message: str,
    chain: List[str]
) -> str:
    """Process a message through a chain of agents."""
```

## BaseTool

Base class for creating agent tools.

### Constructor

```python
class BaseTool(BaseModel):
    """Base class for all tools."""
    pass
```

### Required Methods

#### run

```python
def run(self) -> str:
    """Execute the tool's functionality."""
    raise NotImplementedError
```

## Exceptions

### AgentError

Base exception for agent-related errors.

```python
class AgentError(Exception):
    """Base class for agent exceptions."""
    pass
```

### CommunicationError

Exception for communication failures.

```python
class CommunicationError(Exception):
    """Raised when communication between agents fails."""
    pass
```

### ToolError

Exception for tool execution failures.

```python
class ToolError(Exception):
    """Raised when a tool fails to execute."""
    pass
```

## Utility Functions

### load_dotenv

```python
def load_dotenv(
    path: Optional[str] = None
) -> bool:
    """Load environment variables from .env file."""
```

### setup_logging

```python
def setup_logging(
    level: str = "INFO",
    file: Optional[str] = None
) -> None:
    """Configure logging for Multi-Swarm."""
```

### validate_config

```python
def validate_config(
    config: Dict
) -> Dict:
    """Validate and normalize configuration."""
```

## Constants

```python
# Model identifiers
CLAUDE_MODELS = [
    "claude-3.5-opus",
    "claude-3.5-sonnet",
    "claude-3.5-haiku"
]

GEMINI_MODELS = [
    "gemini-2.0-pro",
    "gemini-2.0-pro-vision"
]

# Default configurations
DEFAULT_TEMPERATURE = 0.7
MAX_RETRIES = 3
TIMEOUT_SECONDS = 300

# Error messages
INVALID_MODEL_ERROR = "Invalid model specified: {}"
INVALID_ROUTE_ERROR = "Invalid communication route: {} -> {}"
TOOL_LOAD_ERROR = "Failed to load tool from {}: {}"
```

## Type Definitions

```python
from typing import TypeVar, Generic, Protocol

AgentType = TypeVar("AgentType", bound=BaseAgent)
ToolType = TypeVar("ToolType", bound=BaseTool)

class MessageProcessor(Protocol):
    async def process_message(self, message: str) -> str:
        ...

class ToolExecutor(Protocol):
    def run(self) -> str:
        ...
```

## Configuration Schema

```python
from pydantic import BaseModel, Field

class AgentConfig(BaseModel):
    name: str
    description: str
    instructions: str
    tools_folder: str
    model: str
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    provider_config: Optional[Dict] = None
    retry_config: Optional[Dict] = None
    streaming: bool = False

class AgencyConfig(BaseModel):
    max_rounds: int = Field(default=10, ge=1)
    timeout: int = Field(default=300, ge=0)
    retry_policy: Dict = Field(default_factory=dict)
```

## Usage Examples

### Creating an Agent

```python
from multi_swarm import BaseAgent

class CustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Custom Agent",
            description="Example agent",
            instructions="instructions.md",
            tools_folder="./tools",
            model="claude-3.5-sonnet"
        )
```

### Creating an Agency

```python
from multi_swarm import Agency

def create_agency():
    agent1 = CustomAgent()
    agent2 = AnotherAgent()
    
    agency = Agency(
        agents=[
            agent1,
            [agent1, agent2]
        ],
        shared_instructions="manifesto.md"
    )
    return agency
```

### Error Handling

```python
try:
    agency = create_agency()
    response = await agency.process_message("Test")
except AgentError as e:
    logger.error(f"Agent error: {e}")
except CommunicationError as e:
    logger.error(f"Communication error: {e}")
except Exception as e:
    logger.error(f"Unexpected error: {e}")
```

## Learn More

- [Agent API](agents.md)
- [Tool API](tools.md)
- [Agency API](agency.md)
- [User Guide](../user-guide/creating-agents.md) 