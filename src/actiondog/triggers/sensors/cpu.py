"""cpu usuage"""
import os

import psutil

from ._sensor import SensorBase


class CPUSensor(SensorBase):
    """read cpu average load"""

    def read(self):
        # Getting loadover15 minutes
        load1, load5, load15 = psutil.getloadavg()
        del load1, load5
        cpu_usage = (load15 / os.cpu_count()) * 100

        return self.cmp(cpu_usage, self.threshold)
