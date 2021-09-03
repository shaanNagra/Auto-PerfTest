#!/usr/bin/env python

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////


from jmx_api.internal.base_element import BaseElem
from jmx_api.internal.constants import TEST_FRAGMENT


# ------------------------------------------
#
# ------------------------------------------
class TestFragment(BaseElem):

    def __init__(self, name):
        super().__init__(TEST_FRAGMENT, name)

    def configTestFragment(self, comments):
        pass
