# Contributing to Multi-Swarm

First off, thank you for considering contributing to Multi-Swarm! It's people like you that make Multi-Swarm such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include details about your environment

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* A clear and descriptive title
* A detailed description of the proposed functionality
* Explain why this enhancement would be useful
* List some other tools or applications where this enhancement exists
* Include code examples if applicable

### Pull Requests

* Fill in the required template
* Follow the Python style guide (PEP 8)
* Include type hints and docstrings
* Write or update tests for the changes
* Update documentation as needed
* Ensure all tests pass

## Development Process

1. Fork the repo
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests (`pytest`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/multi-swarm.git
cd multi-swarm

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install development dependencies
pip install -e .[dev]

# Run tests
pytest
```

### Code Style

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use type hints
* Write descriptive docstrings
* Keep functions focused and small
* Comment complex logic

## Documentation

* Write docstrings for all public modules, functions, classes, and methods
* Update the README.md if needed
* Add examples for new features
* Keep the documentation up to date with changes

## Testing

* Write unit tests for new features
* Ensure all tests pass before submitting a PR
* Aim for high test coverage
* Include both positive and negative test cases

## Questions?

Feel free to open an issue with your question or reach out to the maintainers. 