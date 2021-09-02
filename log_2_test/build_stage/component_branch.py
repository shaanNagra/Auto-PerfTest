#!/usr/bin/env python

import jmx_api as jmx
from indx_2_name import getStateName, getCaseName


# ------------------------------------------
#
# ------------------------------------------
def create_case(name, tt_offset, tt_range, path):
    simple_ctrl = jmx.logic_elements.SimpleController(name)

    simple_ctrl.append(create_think_time(tt_offset, tt_range).get_elem())
    simple_ctrl.append(create_module(path).get_elem())
    return simple_ctrl

def create_basic_case(name, path):
    simple_ctrl = jmx.logic_elements.SimpleController(name)
    simple_ctrl.append(create_module(path).get_elem())
    return simple_ctrl

# ------------------------------------------
#
# ------------------------------------------
def create_think_time(tt_offset, tt_range):

    tt = jmx.think_timer_element.ThinkTime()

    timer = jmx.timer_elements.UniformRandom()
    timer.set_offset(str(tt_offset))
    timer.set_range(str(tt_range))

    tt.append(timer.get_elem())

    return tt


# ------------------------------------------
#
# ------------------------------------------
def create_module(path):

    module = jmx.logic_elements.ModuleController()
    module.add_path(path)

    return module


# ------------------------------------------
#
# ------------------------------------------
def create_switch(next_states, test_plan_name):

    wsc = jmx.logic_elements.WeightedSwitchController()

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
                ).get_elem()
            )
    return wsc


# ------------------------------------------
#
# ------------------------------------------
def create_basic_switch(next_states, test_plan_name):

    wsc = jmx.logic_elements.WeightedSwitchController()

    for ns in next_states:
        case_name = getCaseName(ns)
        state_name = getStateName(ns)
        wsc.addCase(case_name, next_states[ns])
        wsc.append(
            create_basic_case(
                case_name,
                ['Test Plan', test_plan_name, state_name]
                ).get_elem()
            )
    return wsc

# testinput = {
#         0: {'prob': 5, 'offset': 100, 'range': 50},
#         8: {'prob': 20, 'offset': 1000, 'range': 300},
#         3: {'prob': 17, 'offset': 10, 'range': 100}
#     }
# testwsc = create_switch(testinput, 'this is thename of my test plan')
# testwsc.print()
# test = create_case('go to x', '100', '3485', ['the', 'path', 'to'])
# test.print()
# testinput = {
#         0: {'prob': 5, 'offset': 100, 'range': 50},
#         8: {'prob': 20, 'offset': 1000, 'range': 300},
#         3: {'prob': 17, 'offset': 10, 'range': 100}
#     }
