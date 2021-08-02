#  xrt_denoiser - $file.filename
#  Copyright (c) 2021. Minato Ryan
#  Last Edit:2021/7/28
#  This software is released under the MIT License.

from abc import ABCMeta, abstractmethod
from xrt.image.image import *


class Convert(metaclass=ABCMeta):
    @abstractmethod
    def convert(self, ori: Image, target=None):
        """
        Convert Image File.
        :param ori: Original Image
        :param target: (None)Target Image
        :return: path
        """
        pass


class Converter(Convert):
    def __init__(self):
        self.target_type = "png"

    def convert(self, ori: Image, target=None):
        if target is None:
            target = ori.path + "." + self.target_type

        if isinstance(target, str):
            target = PNG(target)

        target.data = ori.read()
        return target.save()


if __name__ == '__main__':
    pass
