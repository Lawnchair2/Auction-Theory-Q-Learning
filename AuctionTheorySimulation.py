import numpy as np
import random


class Agent:
    def __init__(self, numagents, value, increment, alpha, beta, gamma):
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.PossibleActionTable = ["Bid", "Pass"]
        self.Qtable = [np.zeros(len(Agent.ActionTable),value/increment) for _ in range(0,numagents)]
        self.numactions = 0

    def updateQtable(reward): # Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        for n in range(0,Agent.numagents):
            for i in range(0,len(Agent.Qtable)):
                Agent.Qtable[n][]
                pass
    
    def action():
            Agent.numactions += Agent.numactions
            ActionTable = []
            for i in range(0,Agent.numagents):
                if np.random.uniform() < Agent.gamma:
                    ActionTable.append(Agent.PossibleActionTable[random.randint(0,1)])
                else:
                    ActionTable.append(Agent.PossibleActionTable[max(Agent.Qtable[Agent.numactions])])
            return(ActionTable)


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