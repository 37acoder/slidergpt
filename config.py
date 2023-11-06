import os

deployment_name = os.environ["AZURE_DEPLOYMENT_NAME"] or "gpt35-16k"
openai_api_type = "azure"
openai_api_key = os.environ["AZURE_API_KEY"]
openai_api_base = os.environ["AZURE_API_BASE"]
openai_api_version = os.environ["AZURE_API_VERSION"]
