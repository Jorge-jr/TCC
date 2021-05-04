from statemachine import State, StateMachine


class StationState(StateMachine):


    initial = State('Initial', initial=True)
    potential_in = State('Potential_in')
    present = State('Present')
    potential_out = State('Potential_out')
    absent = State('Absent')

    accept = initial.to(potential_in)
    confirm_in = potential_in.to(present)
    detach =  present.to(potential_out)
    back_in = potential_out.to(present)
    confirm_out = potential_out.to(absent)
    restart_in = potential_in.to(initial)
    restart_out = absent.to(initial)
