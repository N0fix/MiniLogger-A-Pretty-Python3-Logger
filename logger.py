#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author : N0fix
# PEP8 compliant, python 3 only


class logger:
    HEADER = '\033[95m'  # Brown
    INFO = '\033[94m'  # Blue
    SUCCESS = '\033[92m'  # Greem
    WARNING = '\033[93m'  # Yellow
    FAIL = '\033[91m'  # Red
    NORMAL = '\033[0m'  # Default color
    BOLD = '\033[1m'  # Bold
    UNDERLINE = '\033[4m'  # Underline
    RESET = "\033[0m"  # White

    FLAG_SHORT_LOGS = False  # If enabled, logs wont exceed 80 chars
    MAX_LEN_LOGS = 80

    @staticmethod
    def log(str, color=RESET, endChr='\n'):
        if logger.FLAG_SHORT_LOGS:
            str = logger._shortenString(str)
        print(color + str + logger.RESET, end=endChr)

    @staticmethod
    def _shortenString(str):
        halfLine = int(logger.MAX_LEN_LOGS/2)
        return str[:halfLine - 2] + "..." + str[-halfLine + 1:]


if __name__ == "__main__":

    # ############# EXAMPLES ################# #

    #  Writing bold green
    logger.log("This is a test", logger.BOLD + logger.SUCCESS)

    # Process something
    for i in range(1, 100):
        logger.log("{}/{} files processed...".format(i, 100),
                   logger.INFO, '\r')

    # Enable max 80 char logs
    logger.FLAG_SHORT_LOGS = True

    # Change max len logs
    logger.MAX_LEN_LOGS = 40

    # ######################################## #
