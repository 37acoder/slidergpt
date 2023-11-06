from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate


class AzureGPT:
    def __init__(
        self, deployment_name, api_type, api_key, api_base, api_verion
    ) -> None:
        chat = AzureChatOpenAI(
            deployment_name=deployment_name,
            # model_name=model_name,
            openai_api_type=api_type,
            openai_api_key=api_key,
            openai_api_base=api_base,
            openai_api_version=api_verion,
        )
        self.chat = chat

    def llm_call(self, messages):
        return self.chat(messages)
