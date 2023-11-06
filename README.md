# Streamlit UI for Chatting with Azure OpenAI

## Description

This project is about creating a user interface (UI) using Streamlit to chat with an AI model based on Azure OpenAI. Because I can't find any simple implementation to access Azure OpenAI so I decide to write this streamlit app.

## Installation

To use this project, you can just download the source code.
Before run apps, you should set some environments shows below. You can find it from Azure OpenAI deployment page.

```python
deployment_name = os.environ["AZURE_DEPLOYMENT_NAME"] 
openai_api_key = os.environ["AZURE_API_KEY"]
openai_api_base = os.environ["AZURE_API_BASE"]
openai_api_version = os.environ["AZURE_API_VERSION"]
```

## Usage

run `streamlit run ui.py`
