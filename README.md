# Mini logger
A simple python logger. Easy to use.

## Installation

`pip install minilogger`

## Usage

```Python
from minilogger import *

if __name__ == "__main__":
  logger.log("This is an important warning!", logger.BOLD + logger.WARNING);
  
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
```
![Example](example.gif)
![Ex2](example.png)
