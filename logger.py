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

    @staticmethod
    def log(str, color=RESET, endChr='\n'):
        print(color + str + logger.RESET, end=endChr)


if __name__ == "__main__":
    #  Writing bold green
    logger.log("This is a test", logger.BOLD + logger.SUCCESS)
    for i in range(1, 100):
        logger.log("{}/{} files processed...".format(i, 100),
                   logger.INFO, '\r')
        #Process something
