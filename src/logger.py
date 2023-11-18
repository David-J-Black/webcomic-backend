import datetime
import logging
import sys
import config

log: logging.Logger = logging.getLogger('webcomicLogger')

# Define ANSI escape codes for text colors
COLORS = {
    'RED': '\033[91m',
    'ORANGE': '\033[93m',
    'BLUE': '\033[94m',
    'PURPLE': '\033[95m',
    'ENDC': '\033[0m'  # Reset to default color
}


# Define custom log formatter
class _ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_level = record.levelname
        log_message = super(_ColoredFormatter, self).format(record)
        time = datetime.datetime.now()
        if log_level == 'WARNING':
            return f"{time}{COLORS['ORANGE']} [WARN] {log_message}{COLORS['ENDC']}"
        elif log_level == 'INFO':
            return f"{time}{COLORS['BLUE']} [INFO] {COLORS['ENDC']}{log_message}{COLORS['ENDC']}"
        elif log_level == 'DEBUG':
            return f"{time}{COLORS['PURPLE']} [DEBUG] {COLORS['ENDC']}{log_message}{COLORS['ENDC']}"
        elif log_level == 'ERROR':
            return f"{time}{COLORS['RED']} [ERROR!] {log_message}{COLORS['ENDC']}"
        else:
            return log_message


def setup_logger():
    global log
    logging.basicConfig(level=logging.DEBUG,
                        filename=config.log_location,
                        filemode='a')
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(_ColoredFormatter())
    log.addHandler(stream_handler)
