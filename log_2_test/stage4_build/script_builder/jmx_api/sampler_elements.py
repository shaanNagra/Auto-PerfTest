#!/usr/bin/env python

# INTERNAL IMPORTS
from jmx_api.internal.base_element import BaseElem
from internal.constants import JSR223_SAMPLER

# ////////////////FILE DESCRIPTION/////////////////
#
# /////////////////////////////////////////////////


# ------------------------------------------
#
# ------------------------------------------
class Jsr223Sampler(BaseElem):
    def __init__(self, name='JSR223 Sampler'):
        super().__init__(JSR223_SAMPLER, name)

    def configJSR223_Script(self, script):
        self.Element.find('.//stringProp[@name="script"]').text = script
        return
