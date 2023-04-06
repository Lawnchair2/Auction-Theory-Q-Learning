import numpy as np
import random


class Agent:
    def __init__(self, numagents, value, increment, alpha, epsilon, gamma, PossibleActionTable):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.PossibleActionTable = PossibleActionTable
        self.Qtable = []
        for i in range(0,numagents):
            self.Qtable.append(np.zeros((len(PossibleActionTable),value//increment), dtype = np.double))
        self.numactions = 0

    def updateQtable(reward): # Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        for n in range(0,Agent.numagents):
            for i in range(0,len(Agent.Qtable)):
                for k in range(0,1):
                    Agent.Qtable[n][k,i] = Agent.Qtable[n][k,i] + Agent.alpha*(reward + Agent.gamma * np.max(Agent.Qtable[n][reward,:]-Agent.Qtable[n][k,i]))
    
    def action():
            Agent.numactions += Agent.numactions
            RoundActionTable = []
            for i in range(0,Agent.numagents):
                if np.random.uniform() < Agent.epsilon:
                    RoundActionTable.append(Agent.PossibleActionTable[random.randint(0,1)])
                else:
                    RoundActionTable.append(Agent.PossibleActionTable[max(Agent.Qtable[Agent.numactions])])
            return(RoundActionTable)


class Auction:
    def __init__(self, numagents, value, increment, fee):
        self.value = value
        self.increment = increment
        self.fee = fee
        self.isactive = True
        self.AuctionHistory = []
        self.numagents = numagents
        self.winningbidder = -1

    def step():
        CurrentActions = Agent.action()
        Auction.AuctionHistory.append(CurrentActions)
        if Auction.CurrentAction.count("Bid") > 1:
            currentvalue = currentvalue + Auction.increment
        else:
            Auction.winningbid = currentvalue
            Auction.isactive == False
            return(Auction.winningbid)
        


    def run_auction():
        while Auction.isactive == True:
            Auction.step()
        Auction.winningbidder = Auction.AuctionHistory.index("Bid")
        if Auction.winningbidder == -1:
            reward = Auction.fee*-1
        else:
            reward = Auction.value - Auction.winningbid - Auction.fee
        Agent.updateQtable(reward)

# Agents: self, numagents, value, increment, alpha, epsilon, gamma
# Auctions: self, numagents, value, increment, fee

numagents = 3
value = 10
increment = 1
alpha = 0.6
epsilon = 0.1
gamma = 0.8
fee = 1
B = Agent(numagents, value, increment, alpha, epsilon, gamma, PossibleActionTable=["Bid", "Pass"])
A = Auction(numagents, value, increment, fee)
Auction.run_auction()