#!/usr/bin/python

import lxml.etree as ET
from constants import *
from elemBuilder import elemBuilder


class OnceOnlyController(elemBuilder):
    def __init__(self, name='Once Only Controller'):
        super().__init__(ONCE_ONLY_CONTROLLER, name)
