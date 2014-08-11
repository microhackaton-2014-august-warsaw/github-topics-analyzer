import datetime
import threading
import os
import os.path
import microhackaton.settings


def create_log_message(level, correlation_id, message, now):
    return '%(date)s | %(level)-5s | %(correlation_id)s | %(thread)s | default | %(message)s' % {
        "date": now.strftime("%Y-%m-%d %H:%M:%S.%fZ"),
        "level": level,
        "correlation_id": correlation_id,
        "thread": threading.currentThread().ident,
        "message": message
    }


def log(level, correlation_id, message):
    if not os.path.exists(os.path.dirname(microhackaton.settings.LOG_FILE)):
        os.makedirs(os.path.dirname(microhackaton.settings.LOG_FILE))
    with open(microhackaton.settings.LOG_FILE, 'a') as log_file:
        log_file.write(create_log_message(level, correlation_id, message, datetime.datetime.now()))
        log_file.write("\n")

def error(correlation_id, message):
    log("ERROR", correlation_id, message)

def warn(correlation_id, message):
    log("WARN", correlation_id, message)

def info(correlation_id, message):
    log("INFO", correlation_id, message)

def debug(correlation_id, message):
    log("DEBUG", correlation_id, message)