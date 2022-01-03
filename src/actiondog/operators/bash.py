"""execute shell command"""
import logging
import subprocess

from .baseoperator import BaseOperator

logger = logging.getLogger()


class BashOperator(BaseOperator):
    """Executes shell commands in response to matched events."""

    def __init__(self, shell_command=None):
        self.shell_command = shell_command

    def run(self):
        """run the command"""
        try:
            proc = subprocess.run(
                self.shell_command,
                shell=True,
                capture_output=True,
                text=True,
                check=True,
            )
            if proc.returncode != 0:
                logger.error(proc.stdout.rstrip())
            else:
                logger.info(proc.stdout.rstrip())
            return proc.returncode

        except subprocess.CalledProcessError as e:
            logger.exception(e)
            logger.error("execute %s failed", self.shell_command)

        return -1
