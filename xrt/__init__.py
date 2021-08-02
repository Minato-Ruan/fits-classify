#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/28
#  This software is released under the MIT License.
import os

from xrt.xrt_cutter import *
import numpy as np
import pandas as pd
import logging

from xrt.log_decorator import *


@log("Image cut begin.")
def cut_xrt_list(list_path, image_path, new_path):
    try:
        log_file("Import XRT-Finder's Log.")
        target_list = get_xrt_list(list_path, image_path)
    except FileNotFoundError:
        log_file("File path" + list_path + "or" + image_path + "NOT Found.", logging.error)

    try:
        log("Rename filename by Base32.")
        renamed_list, old_name_list, new_name_list = rename_target_list(target_list)
    except:
        log("Rename Failed.", logging.error)

    c = ImageCutter()
    failed = 0
    finished = 0

    finished_new = []
    finished_old = []
    for item, old, new in zip(list(renamed_list), old_name_list, new_name_list):
        try:
            new_image = c.cut(item)
            new_image.path = os.path.join(new_path, item.name)
            new_image.save()
        except FileNotFoundError:
            log_file("Input Image(" + new + ")Failed.(path:" + item.path + ")", logging.warning)
            failed += 1
            continue

        finished += 1
        finished_new.append(new)
        finished_old.append(old)
        log_file("Input Image(" + new + ")completed.(path:" + item.path + ")")

    log_file(f"Converted {finished + failed} images. \n {finished} images complete, and {failed} images failed.")

    result = pd.DataFrame(
        {
            "old_name": finished_old,
            "new_name": finished_new
        }
    )
    log("Image Cut Finished.")
    return result


if __name__ == '__main__':
    pass
