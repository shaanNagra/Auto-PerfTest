#!/usr/bin/env python

# import lxml.etree as ET

from jmx_api.internal.super import BaseElem
from jmx_api.internal.constants import TEST_FRAGMENT


class testFragmentBuilder(BaseElem):

    def __init__(self, name):
        super().__init__(TEST_FRAGMENT, name)

    def configTestFragment(self, comments):
        pass
