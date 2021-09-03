
import script_builder.naming_function as naming_func
import script_builder.jmx_api as jmx
import script_tansitions


def create_root(state, testplan_name):

    thread_group = jmx.thread_group_element.threadGroup()

    wsc = script_tansitions.create_basic_transitions(
        state.getNextGroup(),
        testplan_name
        )

    thread_group.append(wsc.get_elem())
    return thread_group.get_elem()


def create_node(state, index, testplan_name):
    state_name = naming_func.getStateName(index)

    n_state = jmx.test_fragment.TestFragment(state_name)

    wsc = script_tansitions.create_basic_transitions(
        state.getNextGroup(),
        testplan_name
        )

    n_state.append(wsc.get_elem())
    return n_state.get_elem()


def create_end_node(state, index, testplan_name):
    state_name = naming_func.getStateName(index)

    end_state = jmx.test_fragment.TestFragment(state_name)

    wsc = script_tansitions.create_basic_transitions(
        state.getNextGroup(),
        testplan_name
        )

    end_state.append(wsc.get_elem())
    return end_state.get_elem()
