#!/usr/bin/env python

# import lxml.etree as ET

from jmx_api.internal.super import BaseElem
from jmx_api.internal.constants import UNIFORM_RANDOM_TIMER


class UniformRandom(BaseElem):
    def __init__(self, name='think time'):
        super().__init__(UNIFORM_RANDOM_TIMER, name)

    def set_offset(self, delay):
        elem = self.Element.find('.//stringProp[@name="ConstantTimer.delay"]')
        elem.text = delay

    def set_range(self, range):
        elem = self.Element.find('.//stringProp[@name="RandomTimer.range"]')
        elem.text = range
