#!/usr/bin/env python

from jmx_api import *
from stateName import getStateName, getCaseName


def create_case(name, tt_offset, tt_range, path):
    simple_ctrl = logic_elements.SimpleController(name)

    simple_ctrl.append(_create_think_time(tt_offset, tt_range))
    simple_ctrl.append(_create_module(path))
    return simple_ctrl.get_elem()


def _create_think_time(tt_offset, tt_range):

    tt = think_timer_element.ThinkTime()

    timer = timer_elements.UniformRandom()
    timer.set_offset(str(tt_offset))
    timer.set_range(str(tt_range))

    tt.append(timer.get_elem())

    return tt.get_elem()


def _create_module(path):

    module = logic_elements.ModuleController()
    module.add_path(path)

    return module.get_elem()


def buildWSC(next_states, test_plan_name):

    wsc = logic_elements.WeightedSwitchController()

    for ns in next_states:
        case_name = getCaseName(ns)
        state_name = getStateName(ns)
        wsc.addCase(case_name, next_states[ns]["prob"])
        wsc.append(
            create_case(
                case_name,
                next_states[ns]["offset"],
                next_states[ns]["range"],
                ['Test Plan', test_plan_name, state_name]
                )
            )
    return wsc


testinput = {
        0: {'prob': 5, 'offset': 100, 'range': 50},
        8: {'prob': 20, 'offset': 1000, 'range': 300},
        3: {'prob': 17, 'offset': 10, 'range': 100}
    }
testwsc = buildWSC(testinput, 'this is thename of my test plan')
testwsc.print()
# test = create_case('go to x', '100', '3485', ['the', 'path', 'to'])
# test.print()
# testinput = {
#         0: {'prob': 5, 'offset': 100, 'range': 50},
#         8: {'prob': 20, 'offset': 1000, 'range': 300},
#         3: {'prob': 17, 'offset': 10, 'range': 100}
#     }
