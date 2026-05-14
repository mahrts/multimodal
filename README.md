# 🛡️ Multimodal AI for content Moderation System
This is a multi-modal content moderation system that makes customer service interactions remain more professional, more secure, and high-quality by auditing contents before sending them to users.

# 🚀 Overview
The system acts as a gatekeeper. It moderates text, image, audio, and video content to detect PII, unprofessional tone, and low-quality media, providing instant feedback and blocking harmful interactions.

## Tech Stack and Architecture

- Gradio: An interactive chat UI for real-time training and file uploads.
- FastAPI: RESTful API endpoints providing access to the moderation services.
- Google Gemini: Specialized prompts for domain-specific content auditing.
- Arize Phoenix: Tracing and monitoring of LLM spans and agent behavior.

```bash

├── evals #Code and sample data for evaluation
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── src
│   ├── agents #Agent for each mode (text, video, image, audio)
│   │   ├── audio_agent.py
│   │   ├── customer_agent.py
│   │   ├── image_agent.py
│   │   ├── __init__.py
│   │   ├── text_agent.py
│   │   └── video_agent.py
│   ├── APP #API calls
│   │   ├── app.py
│   │   ├── fastapi_app.py
│   │   ├── gradio_app.py
│   │   ├── __init__.py
│   ├── COMMON_EVAL #Codes for evaluation
│   │   ├── common_evaluators.py
│   │   ├── config.py
│   │   ├── __init__.py
│   ├── gradio_app
│   │   ├── gradio_app.py
│   │   ├── __init__.py
│   ├── loadenv #loads local environment
│   │   ├── env.py
│   │   ├── __init__.py
│   ├── types_moderation #codes for content moderation
│   │   ├── __init__.py
│   │   ├── model_choice.py
│   │   ├── moderation_result.py
│   └── UTILS
│       ├── __init__.py
│       ├── tracing.py
│       └── utils.py
├── tests
│   ├── test_data #sample data for testing
│   ├── test_gradio_app.py
│   ├── test_image_agent.py
│   ├── test_moderation_result.py
│   ├── test_text_agent.py
│   └── test_video_agent.py
└── uv.lock
```

## Usage
This app can be run locally as follow.
### 1- Build

```bash
git clone <THIS_REPO>
cd multimodal
pip install -r requirements.txt && pip install -e .
```

### 2- Set up .env
Create .env file with the following

```bash
USER_API_KEY=<user_api_key> #Can be your gemini_api_key for running locally.

GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>

# FOLLOWING are default value, can be changed
GOOGLE_GEMINI_BASE_URL=https://gemini.vocareum.com
DEFAULT_GOOGLE_MODEL="gemini-2.5-flash-lite"
# Model used as judge in evaluations (can be same or different from DEFAULT_GOOGLE_MODEL)
# You might want to use a more powerful model as judge, e.g., "gemini-2.0-flash-exp"
EVAL_JUDGE_MODEL="gemini-2.5-flash-lite"
# Number of times to repeat each test case (for measuring LLM consistency)
# Set to 1 for quick runs, 5-10 for statistical confidence
EVAL_NUM_REPEATS=5
```

### 3- Run the Application

One can access the web app with the following:

```bash
uv run multimodal-moderation
```

## Acknowledgement

This project was developed as part of the Udacity Generative AI Nanodegree program.
