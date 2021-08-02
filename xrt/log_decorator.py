#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/29
#  This software is released under the MIT License.
import logging
import time

from config import *


def log(msg: str, msg_type=logging.info, is_to_file: bool = False):
    def decorator(func):
        def wrapper(*args, **kw):
            msg_type(msg)
            if is_to_file:
                with open(LOG_PATH, "a") as f:
                    f.writelines(msg_type.__name__
                                 + "[" + time.asctime(time.localtime(time.time())) + "]"
                                 + ":" + msg + ";\n")
            return func(*args, **kw)

        return wrapper

    return decorator


def log_file(msg, msg_type=logging.info):
    msg_type(msg)
    with open(LOG_PATH, "a") as f:
        f.writelines(msg_type.__name__
                     + "[" + time.asctime(time.localtime(time.time())) + "]"
                     + ":" + msg + ";\n")


if __name__ == '__main__':
    @log("test new2", logging.warning, is_to_file=True)
    def func():
        return "Hello World"

    print(func())
    print(func())
    print(func())
