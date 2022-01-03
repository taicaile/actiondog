"""DAG"""
from typing import List, Optional


class DAG:
    """DAG"""

    # Context Manager -----------------------------------------------
    def __enter__(self):
        DagContext.push_context_managed_dag(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        DagContext.pop_context_managed_dag()


class DagContext:
    """
    DAG context is used to keep the current DAG when DAG is used as ContextManager.
    """

    _context_managed_dag: Optional[DAG] = None
    _previous_context_managed_dags: List[DAG] = []

    @classmethod
    def push_context_managed_dag(cls, dag: DAG):
        """push"""
        if cls._context_managed_dag:
            cls._previous_context_managed_dags.append(cls._context_managed_dag)
        cls._context_managed_dag = dag

    @classmethod
    def pop_context_managed_dag(cls) -> Optional[DAG]:
        """pop"""
        old_dag = cls._context_managed_dag
        if cls._previous_context_managed_dags:
            cls._context_managed_dag = cls._previous_context_managed_dags.pop()
        else:
            cls._context_managed_dag = None
        return old_dag

    @classmethod
    def get_current_dag(cls) -> Optional[DAG]:
        """get current"""
        return cls._context_managed_dag
