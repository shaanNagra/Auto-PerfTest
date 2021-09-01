#!/usr/bin/env python

from elemBuilder import elemBuilder
import lxml.etree as ET
from constants import *


class BuildElement(elemBuilder):
    def __init__(self, name='think time'):
        super().__init__(THINK_TIME, name)
