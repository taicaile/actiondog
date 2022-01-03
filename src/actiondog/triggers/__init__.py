"""trigger module"""
from ._trigger import TriggerBase
from .events import DirModifiedEvent
from .sensors import CPUSensor

__all__ = ["CPUSensor", "DirModifiedEvent"]
