#!/usr/bin/python

# import lxml.etree as ET

from internal.super import BaseElem
from internal.constants import TEST_PLAN


class testPlanBuilder(BaseElem):
    def __init__(self, name='Test Plan'):
        super().__init__(TEST_PLAN, name)

    def configTestPlan(
            self,
            comments,
            func_mode=False, teardown=False, s_tg=False):

        self.Element.find(
            './/stringProp[@name="TestPlan.comments"]').text = comments

        self.Element.find(
            './/boolProp[@name="TestPlan.functional_mode"]'
            ).text = self.Bool2Bool(func_mode)

        self.Element.find(
            './/boolProp[@name="TestPlan.tearDown_on_shutdown"]'
            ).text = self.Bool2Bool(teardown)

        self.Element.find(
            './/boolProp[@name="TestPlan.serialize_threadgroups"]'
            ).text = self.Bool2Bool(s_tg)
        return

# tp = testPlanBuilder()
# tpp = testPlanBuilder('dfafasdfdfsfdskljfdlisjaflkjfdlkdfdjlksdfjldkfj')
# tp.append(tpp.getElem())
# tp.print()
