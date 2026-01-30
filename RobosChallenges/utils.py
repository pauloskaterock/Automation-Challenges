import os
import time
from datetime import datetime
from dateutil.parser import parse


def wait_for_file(folder, timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        files = os.listdir(folder)
        for file in files:
            if file.lower().endswith(".pdf"):
                return os.path.join(folder, file)
        time.sleep(1)
    raise TimeoutError("PDF não foi baixado a tempo")


def is_due_or_overdue(date_str):
    due = parse(date_str).date()
    today = datetime.today().date()
    return due <= today
