class Agent:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.preferences = []

    def __str__(self):
        return self.name + " " + self.surname

    def setPreferences(self, newPreferences):
        self.preferences = newPreferences

    def returnPreferences(self):
        return self.preferences


def sequentialAllocation(agentList, order):
    # sorting the agent list acc to the order provided
    sorted_agent_list = sorted(agentList, key=lambda x: getattr(x, order))

    # creating an empty list per agent to fill it up with items according to the sorted order
    picking_order_of_items_per_agent = {agent: [] for agent in agentList}

    # initializing an empty set to keep the track of all the items picked so far across multiple agents
    total_items = len(agentList[0].returnPreferences())

    if len(agentList) > 0:
        items_picked_so_far = set()
        counter = 0
        #iterating over the items so that all the items are eventually allocated to agents
        while len(items_picked_so_far) < total_items:
            #used modulo operation to circularly keep iterating over the agents
            agent = sorted_agent_list[counter % len(sorted_agent_list)]
            counter = counter + 1
            agent_item_preference = agent.returnPreferences()
            #checking what all items the agent has already picked and giving him a new one which has not been picked so far
            for item in agent_item_preference:
                if item not in items_picked_so_far:
                    picking_order_of_items_per_agent[agent].append(item)
                    items_picked_so_far.add(item)
                    break
        return picking_order_of_items_per_agent

    return {}


# dummy data to test run the program

# agent1 = Agent("Bill", "Bruford")
# agent2 = Agent("Greg", "Lake")
# agent3 = Agent("Robert", "Fripp")
#
# agent1.setPreferences([1, 2, 3, 4])
# agent2.setPreferences([1, 3, 4, 2])
# agent3.setPreferences([2, 3, 1, 4])
#
# agentList = [agent1, agent2, agent3]
#
# abc = sequentialAllocation(agentList, "name")
#
# print(agent1, agent2, agent3)
