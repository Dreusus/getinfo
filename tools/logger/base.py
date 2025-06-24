import logging
import sys
from datetime import datetime

from colorama import Fore
from colorama import Style




class CustomFormatter(logging.Formatter):
    EMOJI = {
        'DEBUG': '🐞',
        'INFO': 'ℹ️',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '🔥',
    }

    def __init__(self, fmt=None, date_fmt=None, style='%', use_colors=False, forced_color=None):
        super().__init__(fmt=fmt, datefmt=date_fmt, style=style)
        self.use_colors = use_colors
        self.forced_color = forced_color

    def formatTime(self, record, date_fmt=None):
        dt = datetime.fromtimestamp(record.created, pytz.timezone('Europe/Moscow'))
        return dt.strftime('%H:%M:%S.%f')[:-4]

    def format(self, record: logging.LogRecord) -> str:
        record.name = record.name.upper()
        emoji = self.EMOJI.get(record.levelname, '')
        record.name_level = f' {emoji}{record.name}'
        msg = super().format(record)

        message_body = record.getMessage()
        start_index = msg.find(message_body)
        indent = ' ' * start_index if start_index != -1 else ''

        lines = msg.splitlines()
        if len(lines) > 1:
            msg = '\n'.join([lines[0]] + [indent + line.lstrip() for line in lines[1:]])

        if self.use_colors:
            if record.levelno in [logging.CRITICAL, logging.ERROR, logging.WARNING]:
                log_color = Fore.RED
            else:
                log_color = self.forced_color
            return f'{log_color}{msg}{Style.RESET_ALL}'

        return msg


class BaseLogger:
    _NAME: str = ''
    _LEVEL: int = logging.INFO
    _FORCED_COLOR: str | None = None
    _FORMAT_STR: str = '%(asctime)s |%(name_level)-8s| %(message)s'
    _DATE_FMT: str = 'H:%M:%S'

    def __init__(self):
        self.logger = logging.getLogger(self._NAME)
        self.logger.setLevel(self._LEVEL)

        _handler = logging.StreamHandler(sys.stdout)
        self._formatter = CustomFormatter(
            fmt=self._FORMAT_STR,
            date_fmt=self._DATE_FMT,
            use_colors=True,
            forced_color=self._FORCED_COLOR
        )
        _handler.setFormatter(self._formatter)
        self.logger.addHandler(_handler)