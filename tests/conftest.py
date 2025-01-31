import os
import pytest
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock environment variables for testing."""
    env_vars = {
        "ANTHROPIC_API_KEY": "mock-claude-key",
        "GOOGLE_API_KEY": "mock-gemini-key",
    }
    for key, value in env_vars.items():
        monkeypatch.setenv(key, value)
    return env_vars

@pytest.fixture
def mock_provider_config() -> Dict[str, Any]:
    """Mock provider configuration for testing."""
    return {
        "claude": {
            "model": "claude-3-sonnet",
            "api_version": "2024-03",
            "max_tokens": 4096
        },
        "gemini": {
            "model": "gemini-2.0-pro",
            "api_version": "2024-01",
            "max_tokens": 4096
        }
    }

@pytest.fixture
def mock_agent_config() -> Dict[str, Any]:
    """Mock agent configuration for testing."""
    return {
        "name": "TestAgent",
        "description": "Test agent for unit testing",
        "instructions": "Test instructions",
        "tools_folder": "./tools",
        "temperature": 0.7
    }

@pytest.fixture
def mock_agency_config() -> Dict[str, Any]:
    """Mock agency configuration for testing."""
    return {
        "shared_instructions": "Test shared instructions",
        "temperature": 0.5,
        "max_prompt_tokens": 25000
    }

@pytest.fixture
def mock_tool_config() -> Dict[str, Any]:
    """Mock tool configuration for testing."""
    return {
        "name": "TestTool",
        "description": "Test tool for unit testing",
        "example_field": "test value"
    } 