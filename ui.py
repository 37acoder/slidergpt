# First
import streamlit as st
from azure import AzureGPT
import config
from langchain.schema import HumanMessage, SystemMessage, AIMessage

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key", key="chatbot_api_key", type="password"
    )

chater = AzureGPT(
    config.deployment_name,
    config.openai_api_type,
    config.openai_api_key,
    config.openai_api_base,
    config.openai_api_version,
)


st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello, I'm a chatbot. How can I help you?"}
    ]


def transform_dict_to_msg(data):
    if data["role"] == "user":
        return HumanMessage(content=data["content"])
    elif data["role"] == "assistant":
        return AIMessage(content=data["content"])
    elif data["role"] == "system":
        return SystemMessage(content=data["content"])
    return None


def transform_sesssion_state_to_messages(messages):
    return [transform_dict_to_msg(msg) for msg in messages]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = chater.chat(
        transform_sesssion_state_to_messages(st.session_state.messages)
    )
    st.session_state.messages.append({"role": "assistant", "content": response.content})
    st.chat_message("assistant").write(response.content)
