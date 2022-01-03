"""directory monitoring"""

import logging
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from ._event import EventBase

__all__ = ["DirModifiedEvent"]

WAITING_TIME = 2 * 60  # wait for 2 minutes after last modified


class DirWatchDog(FileSystemEventHandler):
    """put event Logs all the events captured."""

    def __init__(self, logger=None):
        super().__init__()
        self.logger = logger or logging.root
        self.last_modified = None

    def tick(self):
        """record event time"""
        self.last_modified = time.time()

    def on_moved(self, event):
        super().on_moved(event)

        what = "Moved directory" if event.is_directory else "file"
        self.logger.info("%s: from %s to %s", what, event.src_path, event.dest_path)
        self.tick()

    def on_created(self, event):
        super().on_created(event)

        what = "Created directory" if event.is_directory else "file"
        self.logger.info("%s: %s", what, event.src_path)
        self.tick()

    def on_deleted(self, event):
        super().on_deleted(event)

        what = "Deleted directory" if event.is_directory else "file"
        self.logger.info("%s: %s", what, event.src_path)
        self.tick()

    def on_modified(self, event):
        super().on_modified(event)

        what = "Modified directory" if event.is_directory else "file"
        self.logger.info("%s: %s", what, event.src_path)
        self.tick()


class DirModifiedEvent(EventBase):
    """directory/files monitoring"""

    def __init__(self, path) -> None:
        self.event_handler = DirWatchDog()
        self.observer = Observer()
        self.observer.schedule(self.event_handler, path, recursive=True)
        self.observer.start()

    def stop(self) -> None:
        """stop the event"""
        self.observer.stop()
        self.observer.join()

    def is_triggered(self):

        if (
            self.event_handler.last_modified is not None
            and time.time() - self.event_handler.last_modified >= WAITING_TIME
        ):
            return True

        return False

    def clear(self):
        self.event_handler.last_modified = None
