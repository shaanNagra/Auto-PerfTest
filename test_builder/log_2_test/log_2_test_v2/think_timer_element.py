#!/usr/bin/env python

# import lxml.etree as ET

from internal.super import BaseElem
from internal.constants import THINK_TIME


class BuildElement(BaseElem):
    def __init__(self, name='think time'):
        super().__init__(THINK_TIME, name)
