# Gemini Integration

Multi-Swarm integrates Google's Gemini models, which excel at creative tasks, strategic planning, and natural communication.

## Available Models

1. **Gemini Pro**
   - Versatile model for most tasks
   - Best for: Strategic planning, creative writing
   - Balanced performance and cost
   
2. **Gemini Pro Vision**
   - Multimodal capabilities
   - Best for: Image analysis, visual tasks
   - Supports image inputs

## Configuration

### Basic Setup

```python
from multi_swarm import BaseAgent

class StrategicAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Strategic Planner",
            description="Expert in project planning and coordination",
            instructions="planner_instructions.md",
            tools_folder="./tools",
            model="gemini-2.0-pro",  # Specify Gemini model
            temperature=0.7  # Higher temperature for creative tasks
        )
```

### Advanced Configuration

```python
class VisionAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Vision Analyst",
            model="gemini-2.0-pro-vision",
            provider_config={
                "api_version": "2024-01",
                "max_tokens": 2048,
                "top_p": 0.95,
                "top_k": 40,
                "safety_settings": {
                    "harassment": "block_none",
                    "hate_speech": "block_medium",
                    "sexually_explicit": "block_high",
                    "dangerous_content": "block_medium"
                }
            }
        )
```

## Best Practices

1. **Model Selection**
   - Use Pro for general tasks and planning
   - Use Pro Vision for image-related tasks
   - Consider cost-performance trade-offs

2. **Temperature Settings**
   - 0.7: Creative and strategic tasks
   - 0.5: Balanced tasks
   - 0.9: Highly creative tasks

3. **Content Safety**
   - Configure safety settings appropriately
   - Handle blocked content gracefully
   - Monitor safety filter triggers

4. **Error Handling**

```python
try:
    response = await agent.process_message(prompt)
except GoogleGenerativeAIError as e:
    if "rate_limit" in str(e):
        # Handle rate limiting
        await asyncio.sleep(30)
        response = await agent.process_message(prompt)
    else:
        # Handle other API errors
        raise
```

## Common Use Cases

1. **Strategic Planning**
   ```python
   # Gemini excels at high-level planning
   response = await agent.process_message("""
   Create a project plan for developing a mobile app:
   1. Define key features
   2. Estimate timeline
   3. Identify potential risks
   """)
   ```

2. **Image Analysis**
   ```python
   # Using Gemini Pro Vision for image tasks
   response = await vision_agent.process_message(
       text="Analyze this UI design and suggest improvements",
       images=["design.png"]
   )
   ```

3. **Creative Writing**
   ```python
   # Gemini is great for creative content
   response = await agent.process_message("""
   Write a compelling product description for:
   - Smart home security system
   - Focus on benefits and features
   - Include call to action
   """)
   ```

## Performance Optimization

1. **Token Management**
   - Monitor token usage
   - Use concise prompts
   - Implement response caching

2. **Cost Tracking**
   ```python
   # Track API usage
   class UsageTracker(BaseAgent):
       async def process_message(self, message):
           response = await super().process_message(message)
           self.log_api_usage(response.usage)
           return response
   ```

3. **Streaming Support**
   ```python
   async for chunk in agent.stream_message(prompt):
       print(chunk, end="", flush=True)
   ```

## Multimodal Features

1. **Image Input**
   ```python
   # Process images with text
   response = await vision_agent.process_message(
       text="What's in this image?",
       images=["image.jpg"],
       image_descriptions=["A product photo"]
   )
   ```

2. **Image Analysis**
   ```python
   # Detailed image analysis
   response = await vision_agent.process_message(
       text="Analyze this chart and extract key trends",
       images=["chart.png"]
   )
   ```

## Troubleshooting

1. **Rate Limits**
   - Implement backoff strategies
   - Queue requests when needed
   - Monitor API quotas

2. **Safety Filters**
   - Handle blocked content
   - Adjust safety settings
   - Log filter triggers

3. **API Errors**
   ```python
   from multi_swarm.exceptions import GoogleGenerativeAIError
   
   try:
       response = await agent.process_message(prompt)
   except GoogleGenerativeAIError as e:
       if "safety" in str(e):
           # Handle safety filter trigger
           modified_prompt = adjust_prompt_safety(prompt)
           response = await agent.process_message(modified_prompt)
   ```

## Learn More

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Multi-Swarm Examples](../examples/trends-agency.md)
- [Safety Settings Guide](../user-guide/safety-settings.md) 