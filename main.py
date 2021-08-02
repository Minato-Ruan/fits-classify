#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/29
#  This software is released under the MIT License.

import os

from config import FOLDER_LIST
from xrt import cut_xrt_list


def classify_image():
    for conf in FOLDER_LIST:
        log = cut_xrt_list(list_path=conf["log_path"],
                           image_path=conf["ori_path"],
                           new_path=conf["new_path"])

        if os.path.isdir(conf["new_path"]) is False:
            os.mkdir(conf["new_path"])
        log.to_csv(os.path.join(conf["new_path"], "database_" + conf["log_path"].split("/")[-1].split(".")[0] + ".csv"),
                   index=False)


if __name__ == '__main__':
    classify_image()
