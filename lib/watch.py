import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from lib.build import ASSETS
from lib.launch import run_launch

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        super().on_modified(event)
        if event.is_directory:
            print('dir modified')
            run_launch(object())

def run_watch(args):
    observer = Observer()
    observer.schedule(MyEventHandler(), ASSETS, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
