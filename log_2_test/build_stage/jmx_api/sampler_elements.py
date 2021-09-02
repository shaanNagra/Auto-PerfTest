#!/usr/bin/python

# import lxml.etree as ET

from jmx_api.internal.super import BaseElem
from jmx_api.internal.constants import JSR223_SAMPLER


class Jsr223Sampler(BaseElem):
    def __init__(self, name='JSR223 Sampler'):
        super().__init__(JSR223_SAMPLER, name)

    def configJSR223_Script(self, script):
        self.Element.find('.//stringProp[@name="script"]').text = script
        return