"""Trigger Base"""


class TriggerBase:
    def is_triggered(self):
        """check if this event/sensor is triggered"""

    def stop(self):
        """stop this trigger"""

    def clear(self):
        """clear after reading trigger"""
