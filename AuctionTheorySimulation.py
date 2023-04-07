import numpy as np
import random


class Agent:
    def __init__(self, numagents, value, increment, alpha, epsilon, gamma, PossibleActionTable):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.PossibleActionTable = PossibleActionTable
        self.numagents = numagents
        self.Qtable = []
        for i in range(0,numagents):
            self.Qtable.append(np.zeros((len(PossibleActionTable),value//increment), dtype = np.double))
        self.numactions = 0
        self.PrevActionTable = ["Bid" for _ in range(0,numagents)]

    def updateQtable(self, reward): # Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        for n in range(0,self.numagents):
            for i in range(0,value//increment):
                for k in range(0,1):
                    # new_state = 
                    self.Qtable[n][k,i] = self.Qtable[n][k,i] + self.alpha*(reward + self.gamma * np.max(self.Qtable[n][reward,:])-self.Qtable[n][k,i]) 
                    # TODO: FIX Q TABLE, IDK WHAT REWARD SHOULD BE
    
    def action(self):
            self.numactions += self.numactions
            RoundActionTable = []
            for i in range(0,self.numagents):
                if self.PrevActionTable[i] == "Pass":
                    self.currentaction = "Pass"
                    RoundActionTable.append(self.currentaction)
                elif np.random.uniform() < self.epsilon:
                    self.currentaction = self.PossibleActionTable[random.randint(0,1)]
                    RoundActionTable.append(self.currentaction)
                else:
                    self.currentaction = self.PossibleActionTable[int(max(self.Qtable[i][:,self.numactions]))]
                    RoundActionTable.append(self.currentaction)
            self.PrevActionTable = RoundActionTable
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
        self.winningbid = 0

    def step(self, Agent):
        CurrentActions = Agent.action()
        self.AuctionHistory.append(CurrentActions)
        if CurrentActions.count("Bid") > 1:
            self.winningbid = self.winningbid + self.increment
        else:
            self.isactive = False
        return(self.winningbid)
        
    def run_auction(self, Agent):
        while self.isactive == True:
            self.step(Agent)
        self.winningbidder = self.AuctionHistory[-1].index("Bid")
        if self.winningbidder == -1:
            reward = self.fee*-1
        else:
            reward = self.value - self.winningbid - self.fee
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
A.run_auction(B)