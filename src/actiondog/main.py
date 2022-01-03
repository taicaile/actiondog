"""main entry"""
import logging
import time

import helper
from events import DirModifiedEvent
from measures import CPULoadMeasure

helper.logging_init()

logger = logging.getLogger()

if __name__ == "__main__":

    events = [DirModifiedEvent("src")]
    measures = [CPULoadMeasure(20)]

    try:
        while True:
            if all(e.is_triggered() for e in events) and all(
                e.is_triggered() for e in measures
            ):
                logger.info("is_triggered.")
                for e in events:
                    e.clear()
            time.sleep(1)
    except KeyboardInterrupt:
        for e in events:
            e.stop()
