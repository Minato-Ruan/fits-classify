#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/29
#  This software is released under the MIT License.

import os
from xrt.cutter.cutter import TargetList, ImageTarget, ImageCutter
import base64 as b64

import numpy as np
import pandas as pd


def get_xrt_list(path: str, img_path):
    data = pd.read_table(path, sep=" ", header=None)
    data.columns = ["name", "fkx", "fky", "level", "x", "y"]

    result = TargetList()

    for row in data.iterrows():
        row_data = row[1]

        new_target = ImageTarget(
            pos=(int(row_data.x), int(row_data.y)),
            size=(32, 32),
            name=row_data["name"],
            path=os.path.join(img_path, row_data["name"].split("_")[0] + "xpcw3po_cl.evt")
        )
        result.append(new_target)

    return result


def target_base32_name(target: ImageTarget):
    """
    Encode Image's Name by Base32
    :param target: Target Obj
    :return: New Target obj, Old Name, New Name
    """
    old_name = target.name
    target.name = b64.b32encode((target.name
                                 + "_" + str(target.pos[0])
                                 + "_" + str(target.pos[1])).encode()).decode("utf-8")

    return target, old_name, target.name


def rename_target_list(target_list):
    rename_list = TargetList()
    old_name_list = []
    new_name_list = []
    for item in target_list:
        new_target, old_name, new_name = target_base32_name(item)
        rename_list.append(new_target)
        old_name_list.append(old_name)
        new_name_list.append(new_name)

    return rename_list, old_name_list, new_name_list


if __name__ == '__main__':
    pass
