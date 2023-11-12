from datetime import datetime
import streamlit as st
import uuid

class History:
    def __init__(self, id=None, title="Untitled", messages=None, start_time=None) -> None:
        self.messages = messages or []
        self.start_time = start_time or datetime.now()
        self.title = title

class HistoryManager:
    def __init__(self) -> None:
        self.histories = {}

        
    def add(self, title, messages=[], start_time=None):
        id = uuid.uuid4()
        self.histories[id] = History(id, title, messages, start_time)
        return id

    def get(self, id):
        return self.histories[id]


class HistoryUIComponent:
    def __init__(self) -> None:
        self.history_manager = st.session_state.get("history_manager")or HistoryManager()
        st.session_state["history_manager"] = self.history_manager
        def on_history_select_change():
            st.session_state.messages = st.session_state.history_selected.messages
        st.selectbox("History", self.history_manager.histories.values(), format_func=lambda x: x.title, key="history_selected", on_change=on_history_select_change)
        