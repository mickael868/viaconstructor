import sys

ERROR = 0
WARNING = 1
INFO = 2
DBG = 3

log_level = WARNING


def eprint(message, *args, **kwargs):  # pylint: disable=W0613
    sys.stderr.write(f"{message}\n")


def log(level, *args, **kwargs):
    if level <= log_level:
        print(*args, **kwargs)


def log_error(*args, **kwargs):
    log(ERROR, "ERROR:", *args, **kwargs)


def log_warn(*args, **kwargs):
    log(WARNING, "WARNING:", *args, **kwargs)


def log_info(*args, **kwargs):
    log(INFO, "INFO:", *args, **kwargs)


def log_dbg(*args, **kwargs):
    log(DBG, "DEBUG:", *args, **kwargs)
