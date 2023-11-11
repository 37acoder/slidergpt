import os

deployment_name = os.environ.get("AZURE_DEPLOYMENT_NAME", "gpt35-16k")
openai_api_type = "azure"
openai_api_key = os.environ.get("AZURE_API_KEY")
openai_api_base = os.environ.get("AZURE_API_BASE")
openai_api_version = os.environ.get("AZURE_API_VERSION")
