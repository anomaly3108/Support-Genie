import json
import random

with open('data.json') as f: # open data of agents in json file format
    agents = json.load(f)

modes = ['all_available', 'least_busy', 'random'] # modes


def listagent(issue):  # returns the list of agents available with same roles
    names = []
    for user in agents:
        if agents[user]['is_available'] == 'True': # select only available agents
            a = agents[user]['roles']
            b = issue['role']
            if all(x in a for x in b):
                names.append(user) # appends all those agents with similar roles as of the issue
    return names


def selection(mode, issue):  # selects the agents based on the mode
    print('the mode you have selected is', modes[mode])
    return_list = []
    agent = listagent(issue)
    if len(agent) == 0:

        print('No agents, please try again later') # if no agents is available
    else:
        if modes[mode] == 'all_available':
            return_list = agent
        elif modes[mode] == 'least_busy':
            return_list, time = least(agent)
        else:
            choice = random.randint(0, len(agent) - 1) # choosing agents randomly
            return_list.append(agent[choice])
    return return_list


def least(agent):  # returns least busy agents
    time = []
    uset = []
    for i in agent:
        time.append(agents[i]['available_since'])
    maxx = max(time) # select maximum idle time of agent
    for i in agent:
        if agents[i]['available_since'] == maxx:
            uset.append(i) # append all those agents with maximum idle time
    return uset, maxx
