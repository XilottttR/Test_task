import logging

def get_logger(name: str | None = None):
    return logging.getLogger(name or "task_project")
