#!/usr/bin/python
# import xml.etree.ElementTree as ET
import lxml.etree as ET
from constants import *
from elemBuilder import elemBuilder

class jsr223SamplerBuilder(elemBuilder):
    def __init__(self, name='JSR223 Sampler'):
        super().__init__(JSR223_SAMPLER, name)

    def configJSR223_Script(self,script):
        self.Element.find('.//stringProp[@name="script"]').text = script
        return