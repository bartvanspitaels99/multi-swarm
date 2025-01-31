# Creating Tools

Tools are the actions that agents can perform. This guide explains how to create custom tools in Multi-Swarm using Pydantic for type safety and validation.

## Basic Tool Structure

Every tool inherits from the `BaseTool` class:

```python
from multi_swarm.tools import BaseTool
from pydantic import Field
from typing import List, Dict

class CustomTool(BaseTool):
    """
    A clear description of what the tool does.
    This docstring helps agents understand when to use the tool.
    """
    input_data: str = Field(..., description="Description of the input")
    options: Dict = Field(default={}, description="Optional configuration")

    def run(self) -> str:
        """Implement the tool's functionality."""
        result = self._process_data(self.input_data, self.options)
        return result
```

## Tool Components

### 1. Class Definition

```python
class DataAnalysisTool(BaseTool):
    """Tool for analyzing numerical data and generating insights."""
```

- Inherit from `BaseTool`
- Clear docstring explaining purpose
- Descriptive class name

### 2. Input Fields

```python
class DataAnalysisTool(BaseTool):
    data: List[float] = Field(
        ...,  # Required field
        description="List of numerical values to analyze",
        min_items=1,
        example=[1.0, 2.5, 3.7]
    )
    
    method: str = Field(
        default="mean",  # Default value
        description="Analysis method to use",
        choices=["mean", "median", "mode"]
    )
```

- Use Pydantic's `Field` for validation
- Clear descriptions
- Default values when appropriate
- Type hints for better IDE support

### 3. Run Method

```python
def run(self) -> str:
    """
    Execute the tool's main functionality.
    Returns a string describing the result.
    """
    try:
        result = self._analyze_data()
        return f"Analysis complete: {result}"
    except Exception as e:
        return f"Error during analysis: {str(e)}"
```

- Clear return type
- Error handling
- Descriptive return messages

## Advanced Features

### 1. Async Support

```python
class AsyncTool(BaseTool):
    async def run(self) -> str:
        """Asynchronous tool execution."""
        result = await self._async_operation()
        return result
```

### 2. Complex Validation

```python
from pydantic import validator
from datetime import datetime

class DateProcessingTool(BaseTool):
    date_str: str = Field(..., description="Date string to process")
    format: str = Field(default="%Y-%m-%d")

    @validator('date_str')
    def validate_date(cls, v, values):
        try:
            datetime.strptime(v, values['format'])
            return v
        except ValueError:
            raise ValueError(f"Invalid date format. Expected {values['format']}")
```

### 3. Dependent Fields

```python
class APITool(BaseTool):
    endpoint: str = Field(..., description="API endpoint")
    method: str = Field(default="GET")
    body: Dict = Field(default={})

    @validator('body')
    def validate_body(cls, v, values):
        if values['method'] in ['POST', 'PUT'] and not v:
            raise ValueError("Body required for POST/PUT requests")
        return v
```

## Common Tool Types

### 1. API Integration

```python
class APITool(BaseTool):
    """Tool for making API calls."""
    url: str = Field(..., description="API endpoint URL")
    method: str = Field(default="GET")
    headers: Dict = Field(default={})
    body: Dict = Field(default={})

    async def run(self) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.request(
                self.method,
                self.url,
                headers=self.headers,
                json=self.body
            ) as response:
                result = await response.json()
                return str(result)
```

### 2. File Operations

```python
class FileProcessingTool(BaseTool):
    """Tool for file operations."""
    file_path: str = Field(..., description="Path to file")
    operation: str = Field(
        default="read",
        choices=["read", "write", "append"]
    )
    content: str = Field(default="")

    def run(self) -> str:
        if self.operation == "read":
            with open(self.file_path, 'r') as f:
                return f.read()
        elif self.operation == "write":
            with open(self.file_path, 'w') as f:
                f.write(self.content)
            return f"Written {len(self.content)} bytes"
```

### 3. Data Processing

```python
class DataTransformTool(BaseTool):
    """Tool for data transformation."""
    data: List[Dict] = Field(..., description="Data to transform")
    transform_type: str = Field(
        default="filter",
        choices=["filter", "map", "reduce"]
    )
    criteria: Dict = Field(default={})

    def run(self) -> str:
        if self.transform_type == "filter":
            result = self._filter_data()
        elif self.transform_type == "map":
            result = self._map_data()
        else:
            result = self._reduce_data()
        return str(result)
```

## Best Practices

1. **Input Validation**
   ```python
   class ValidatedTool(BaseTool):
       value: int = Field(
           ...,
           ge=0,
           le=100,
           description="Value between 0 and 100"
       )
   ```

2. **Error Handling**
   ```python
   class RobustTool(BaseTool):
       def run(self) -> str:
           try:
               result = self._process()
               return result
           except ValueError as e:
               return f"Validation error: {e}"
           except Exception as e:
               return f"Unexpected error: {e}"
   ```

3. **Documentation**
   ```python
   class WellDocumentedTool(BaseTool):
       """
       Detailed description of the tool's purpose.
       
       Args:
           input_data: Description of input
           options: Description of options
       
       Returns:
           Description of return value
       
       Raises:
           ValueError: When input is invalid
       """
   ```

4. **Resource Management**
   ```python
   class ResourceTool(BaseTool):
       async def run(self) -> str:
           async with self._acquire_resource() as resource:
               result = await self._process(resource)
           return result
   ```

## Testing Tools

```python
import pytest

async def test_custom_tool():
    # Test basic functionality
    tool = CustomTool(input_data="test")
    result = await tool.run()
    assert result is not None

    # Test validation
    with pytest.raises(ValueError):
        tool = CustomTool(input_data=None)

    # Test edge cases
    tool = CustomTool(input_data="", options={"strict": True})
    result = await tool.run()
    assert result == "Empty input handled"
```

## Learn More

- [Tool API Reference](../api/tools.md)
- [Example Tools](../examples/dev-agency.md#tools)
- [Advanced Validation](../user-guide/advanced-tools.md)
- [Tool Best Practices](../user-guide/tool-best-practices.md) 