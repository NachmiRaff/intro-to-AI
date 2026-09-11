#search
from . import state
from . import frontier

max_search = 15000

def search(s):
    print(s)
    f = frontier.create(s)
    popped = 0
    while not frontier.is_empty(f) and f[1]<max_search:
        s = frontier.remove(f)
        popped+=1
        if state.is_target(s):
            return [s, f[1], popped, state.path_len(s), True]
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return [s, max_search, max_search, 100, False]
