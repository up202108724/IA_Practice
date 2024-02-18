class BucketState:
    c1 = 4   # capacity for bucket 1
    c2 = 3   # capacity for bucket 2
    
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    '''needed for the visited list'''
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash((self.b1, self.b2)) 
    ''' - '''

    def __str__(self):
        return "(" + str(self.b1) + ", " + str(self.b2) + ")"

def child_bucket_states(state):
    new_states = []
    if(empty1(state)):
        new_states.append(empty1(state))
    if(empty2(state)):
        new_states.append(empty2(state))
    if(fill1(state)):
        new_states.append(fill1(state))
    if(fill2(state)):
        new_states.append(fill2(state))
    if(pour12_fill2(state)):
        new_states.append(pour12_fill2(state))
    if(pour12_empty1(state)):
        new_states.append(pour12_empty1(state))
    if(pour21_fill1(state)):
        new_states.append(pour21_fill1(state))
    if(pour21_empty2(state)):
        new_states.append(pour21_empty2(state))
    return new_states

# emptying the first bucket
def empty1(state):
    if state.b1 > 0:
        return BucketState(0, state.b2)
    return None

# emptying the second bucket
def empty2(state):
    if state.b2 > 0:
        return BucketState(state.b1, 0)
    return None
def fill1(state):
    if state.b1 < BucketState.c1:
        return BucketState(BucketState.c1, state.b2)
    return None
def fill2(state):
    if state.b2 < BucketState.c2:
        return BucketState(state.b1, BucketState.c2)
    return None
def pour12_fill2(state):
    if state.b1 > 0 and state.b2 < state.c2:
        if state.b1 + state.b2 <= state.c2:
            return BucketState(0, state.b1 + state.b2)
        else:
            return BucketState(state.b1 - (BucketState.c2 - state.b2), BucketState.c2)
    return None
def pour21_fill1(state):
    if state.b2 > 0 and state.b1 < BucketState.c1:
        if state.b1 + state.b2 > BucketState.c1:
            return BucketState(BucketState.c1, state.b2 - (BucketState.c1 - state.b1))
    return None
def pour12_empty1(state):
      if state.b1 + state.b2 <= BucketState.c2:
            return BucketState(0, state.b1 + state.b2)
        else:
            return None
def pour21_empty2(state):
    if state.b1 + state.b2 <= BucketState.c1:
        return BucketState(state.b1 + state.b2, 0)
    else:
        return None
def goal_bucket_state(state):
    return state.b1 == 2