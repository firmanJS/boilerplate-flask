import logging
import logging.handlers
import os
from datetime import datetime


class Logger:
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

    def __init__(self, base_path, log_name, to_stdout=True, max_bytes=10485760, backup_count=1):
        log_file = os.path.join(base_path, '{}.log'.format(log_name))
        self.to_stdout = to_stdout

        # logging.basicConfig(format='%(message)s')
        self.logger = logging.getLogger('{}_logger'.format(log_name))
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(message)s')
        handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def print_log(self, message, to_file=True, log_type=INFO, to_stdout=True):
        if not self.to_stdout:
            to_stdout = self.to_stdout

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if to_stdout:
            print("{0} [{1}] {2}".format(now, log_type, message))

        if to_file:
            if log_type == self.ERROR:
                self.logger.error("{0} [{1}] {2}".format(now, log_type, message))
            elif log_type == self.WARNING:
                self.logger.warning("{0} [{1}] {2}".format(now, log_type, message))
            else:
                self.logger.info("{0} [{1}] {2}".format(now, log_type, message))
