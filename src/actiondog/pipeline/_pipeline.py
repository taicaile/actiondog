"""Pipeline"""
import logging
import time
from typing import List, Optional

logger = logging.getLogger()


class Pipeline:
    """Pipeline"""

    def __init__(self, conditions, actions) -> None:
        self.conditions = conditions
        self.actions = actions

    def run(self):
        while True:
            if all(e.is_triggered() for e in self.conditions):
                for e in self.conditions:
                    e.clear()
                for action in self.actions:
                    action.run()

            time.sleep(1)

    def stop(self):
        for e in self.conditions:
            e.stop()

    # Context Manager -----------------------------------------------
    def __enter__(self):
        PipelineContext.push_context_managed_dag(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        PipelineContext.pop_context_managed_dag()


class PipelineContext:
    """
    Pipeline context is used to keep the current Pipeline when Pipeline is
    used as ContextManager.
    """

    _context_managed_dag: Optional[Pipeline] = None
    _previous_context_managed_dags: List[Pipeline] = []

    @classmethod
    def push_context_managed_dag(cls, dag: Pipeline):
        """push"""
        if cls._context_managed_dag:
            cls._previous_context_managed_dags.append(cls._context_managed_dag)
        cls._context_managed_dag = dag

    @classmethod
    def pop_context_managed_dag(cls) -> Optional[Pipeline]:
        """pop"""
        old_dag = cls._context_managed_dag
        if cls._previous_context_managed_dags:
            cls._context_managed_dag = cls._previous_context_managed_dags.pop()
        else:
            cls._context_managed_dag = None
        return old_dag

    @classmethod
    def get_current_dag(cls) -> Optional[Pipeline]:
        """get current"""
        return cls._context_managed_dag
