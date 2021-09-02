#!/usr/bin/env python

# import lxml.etree as ET

from jmx_api.internal.super import BaseElem
from jmx_api.internal.constants import THINK_TIME


class ThinkTime(BaseElem):
    def __init__(self, name='think time'):
        super().__init__(THINK_TIME, name)
