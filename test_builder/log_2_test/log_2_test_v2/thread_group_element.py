#!/usr/bin/python

import lxml.etree as ET

from internal.super import BaseElem
from internal.constants import THREAD_GROUP


class threadGroup(BaseElem):
    def __init__(self, name='Thread Group'):
        super().__init__(self, THREAD_GROUP, name)

    def configTG_loopCount(self, count, infinite=False):

        if infinite is False:
            newElem = ET.Element('stringProp', name='LoopController.loops')
            newElem.text = str(count)
        else:
            newElem = ET.Element('intProp', name='LoopController.loops')
            newElem.text = str(-1)

        if self.Element.find(
             './/intProp[@name="LoopController.loops"]'
             ) is None:
            elem = self.Element.find(
                './/stringProp[@name="LoopController.loops"]'
                )

        else:
            elem = self.Element.find(
                './/intProp[@name="LoopController.loops"]'
                )

        elem.addnext(newElem)
        parent = elem.getparent()
        parent.remove(elem)
        return

    def configTG_onSampleError(self):

        return

    def configTG_Lifetime(self, toggle=False, Duration="", StartupDelay=""):
        schedElem = self.Element.find(
            './/boolProp[@name="ThreadGroup.scheduler"]'
            )
        duratElem = schedElem.getnext()
        delayElem = duratElem.getnext()
        if toggle is False:
            schedElem.text = self.Bool2Bool(toggle)
            duratElem.text = ''
            delayElem.text = ''
        else:
            schedElem.text = self.Bool2Bool(toggle)
            duratElem.text = str(Duration)
            delayElem.text = str(StartupDelay)
        return

    def configTG_other(self, sameUserOnIter=False, numThreads=1, rampTime=1):
        numThreadsElem = self.Element.find(
            './/stringProp[@name="ThreadGroup.num_threads"]'
            )
        rampTimeElem = numThreadsElem.getnext()
        sameUserElem = self.Element.find(
            './/boolProp[@name="ThreadGroup.same_user_on_next_iteration"]'
            )
        numThreadsElem.text = str(numThreads)
        rampTimeElem.text = str(rampTime)
        sameUserElem.text = self.Bool2Bool(sameUserOnIter)
        return
