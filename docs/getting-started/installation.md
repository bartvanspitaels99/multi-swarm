# Installation Guide

Multi-Swarm can be installed directly via pip:

```bash
pip install multi_swarm
```

## Prerequisites

1. **Python Version**
   - Python 3.8 or higher is required
   - Virtual environment recommended

2. **API Keys**
   You'll need API keys for the LLM providers you plan to use:
   
   - For Claude (Anthropic):
     - Get your API key from [Anthropic's Console](https://console.anthropic.com/)
     - Set it as an environment variable:
       ```bash
       export ANTHROPIC_API_KEY=your_api_key
       ```

   - For Gemini (Google):
     - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
     - Set it as an environment variable:
       ```bash
       export GOOGLE_API_KEY=your_api_key
       ```

## Environment Setup

1. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Multi-Swarm**
   ```bash
   pip install multi_swarm
   ```

3. **Create a .env File**
   Create a `.env` file in your project root:
   ```env
   ANTHROPIC_API_KEY=your_claude_api_key
   GOOGLE_API_KEY=your_gemini_api_key
   ```

4. **Verify Installation**
   ```python
   from multi_swarm import Agency, BaseAgent
   print("Multi-Swarm installed successfully!")
   ```

## Optional Dependencies

For enhanced functionality, you can install additional packages:

```bash
# For monitoring and visualization
pip install multi_swarm[monitoring]

# For development and testing
pip install multi_swarm[dev]

# For all optional dependencies
pip install multi_swarm[all]
```

## Troubleshooting

### Common Issues

1. **API Key Not Found**
   ```python
   ImportError: API key not found. Please set the ANTHROPIC_API_KEY environment variable.
   ```
   Solution: Ensure you've set up your API keys in the `.env` file or environment variables.

2. **Python Version Error**
   ```python
   ImportError: This package requires Python 3.8+
   ```
   Solution: Upgrade your Python installation or use a compatible version.

3. **Package Conflicts**
   If you encounter package conflicts, try creating a fresh virtual environment:
   ```bash
   python -m venv fresh_venv
   source fresh_venv/bin/activate
   pip install multi_swarm
   ```

For more help, check our [GitHub Issues](https://github.com/yourusername/multi_swarm/issues) or [Documentation](https://multi-swarm.readthedocs.io/). 