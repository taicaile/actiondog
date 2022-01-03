"""Measure base module"""
import logging
import operator

from triggers import TriggerBase


class SensorBase(TriggerBase):
    """base class of all measures"""

    def __init__(self, threshold, cmp=operator.le, logger=None) -> None:
        self.logger = logger or logging.root
        self.threshold = threshold
        self.cmp = cmp

    def read(self):
        """read value"""
        raise NotImplementedError

    def is_triggered(self):
        """is triggered"""
        return self.cmp(self.read(), self.threshold)
