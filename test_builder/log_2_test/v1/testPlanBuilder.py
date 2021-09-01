#!/usr/bin/python
# import xml.etree.ElementTree as ET
import lxml.etree as ET
from constants import *
from elemBuilder import elemBuilder
import functions as funcs
import threadGroupBuilder


class testPlanBuilder(elemBuilder):
    def __init__(self, name='Test Plan'):
        super().__init__(TEST_PLAN, name)

    def configTestPlan(self, comments, func_mode=False, tearDown_on_SD=False, s_tg=False):
        self.Element.find('.//stringProp[@name="TestPlan.comments"]').text = comments
        self.Element.find('.//boolProp[@name="TestPlan.functional_mode"]').text = self.Bool2Bool(func_mode)
        self.Element.find('.//boolProp[@name="TestPlan.tearDown_on_shutdown"]').text = self.Bool2Bool(tearDown_on_SD)
        self.Element.find('.//boolProp[@name="TestPlan.serialize_threadgroups"]').text = self.Bool2Bool(s_tg)
        return

# tp = testPlanBuilder()
# tpp = testPlanBuilder('dfafasdfdfsfdskljfdlisjaflkjfdlkdfdjlksdfjldkfj')
# tp.append(tpp.getElem())
# tp.print()