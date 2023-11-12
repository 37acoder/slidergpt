from datetime import time
import streamlit as st
import uuid

class History:
    def __init__(self,id, messages=None, start_time=None) -> None:
        self.messages = messages or []
        self.start_time = start_time or time.time()


class HistoryManager:
    def __init__(self) -> None:
        self.histories = {}

        
    def add(self, title, messages=[], start_time=None):
        id = uuid.uuid4()
        self.histories[id] = History(messages, start_time)


    def get(self, title,)
