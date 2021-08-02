#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/28
#  This software is released under the MIT License.

from xrt.image.image import *
from xrt.image.converter import *


def convert_fits_png(ori: str, target: str):
    ori_obj = XImage(ori)
    c = Converter()
    return c.convert(ori_obj, target)


if __name__ == '__main__':
    pass
