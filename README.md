# Email Processing Agent

This project is an intelligent email processing system that can analyze and classify emails, with a focus on spam detection and response generation. It uses LangGraph for workflow orchestration and Langfuse for observability.

## Features

- Email classification (spam detection)
- Email categorization
- Automated response generation
- Observability and tracing with Langfuse
- Integration with LangGraph for workflow management

## Prerequisites

- Python 3.8+
- Ollama (for local LLM support)
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with the following variables:
```
LANGFUSE_PUBLIC_KEY=your_public_key
LANGFUSE_SECRET_KEY=your_secret_key
```

## Project Structure

```
.
├── agent/           # Core agent implementation
├── models/          # Data models and schemas
├── src/            # Source code and utilities
├── main.py         # Main application entry point
└── requirements.txt # Project dependencies
```

## Usage

Run the main application:
```bash
python main.py
```

The application will process example emails (both legitimate and spam) and demonstrate the classification and response generation capabilities.

## Development

The project uses:
- LangGraph for workflow orchestration
- Langfuse for observability and tracing
- Pydantic for data validation
- Python-dotenv for environment management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Here]
