#search
from . import state
from . import frontier
import random

random.seed(1)

max_search = 15000

def search(n):
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    popped=0
    pushed=0
    while not frontier.is_empty(f) and pushed<max_search:
        s=frontier.remove(f)
        popped+=1
        if state.is_target(s):
            return [s,pushed,popped,state.path_len(s),True]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
            pushed+=1
    return [s,max_search,max_search,100,False]

output = []
runs = 100
for i in range(runs):
    output.append(search(4))
    if(i%10==0):
        print(i)
    if(not output[-1][-1]):
        print("failed")

av_pushed = 0
av_checked = 0
av_cost = 0
av_cost_suc = 0
max_pushed = 0
max_checked = 0
max_cost = 0
sucsess = 0.0

for i in output:
    av_pushed += i[1]
    av_checked += i[2]
    av_cost += i[3]
    sucsess += 1 if i[4] else 0
    av_cost_suc += i[3] if i[4] else 0

    max_pushed = max(max_pushed, i[1])
    max_checked = max(max_checked, i[2])
    max_cost = max(max_cost, i[3])

av_cost_suc/=sucsess
av_pushed /= runs
av_checked /= runs
av_cost /= runs
sucsess /= runs

with open("./id/output.txt","w") as f:
    f.write("Total runs: " + str(runs) + "\n")
    f.write("Average pushed: " + str(av_pushed) + "\n")
    f.write("Average checked: " + str(av_checked) + "\n")
    f.write("Average cost: " + str(av_cost) + "\n")
    f.write("Average cost of successful runs: " + str(av_cost_suc) + "\n")
    f.write("Success rate: " + str(sucsess) + "\n")
    f.write("Max pushed: " + str(max_pushed) + "\n")
    f.write("Max checked: " + str(max_checked) + "\n")
    f.write("Max cost: " + str(max_cost) + "\n")