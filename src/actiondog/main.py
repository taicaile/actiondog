"""main entry"""
import logging

import utils
from operators import BashOperator
from pipeline import Pipeline
from triggers.events import DirModifiedEvent
from triggers.sensors import CPUSensor

utils.logging_init()

logger = logging.getLogger()

if __name__ == "__main__":

    conditions = (DirModifiedEvent("src"), CPUSensor(20))
    actions = [BashOperator(shell_command="echo $(date)")]

    with Pipeline(conditions=conditions, actions=actions) as pipe:
        try:
            pipe.run()
        except KeyboardInterrupt:
            pipe.stop()
