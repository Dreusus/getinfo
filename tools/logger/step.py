from colorama import Fore

from app.utils.logger.base import BaseLogger
from config import LoggerEnv


class StepLogger(BaseLogger):
    _NAME: str = 'step'
    _LEVEL: int = LoggerEnv.LOG_LEVEL_STEP
    _FORCED_COLOR: str = Fore.GREEN
