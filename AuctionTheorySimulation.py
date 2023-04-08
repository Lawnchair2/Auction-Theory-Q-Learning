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
        self.numactions = 0
        self.PrevActionTable = ["Bid" for _ in range(0,numagents)]

        for i in range(0,numagents):
            self.Qtable.append(np.zeros((len(PossibleActionTable),value//increment), dtype = np.double))


    def updateQtable(self, Auction, winningbidder, reward, fee): # Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        AuctionHistoryTable = Auction.AuctionHistory

        for n in range(0,self.numagents):

           # if self.Qtable[n] < self.numactions:
            #    np.resize(self.Qtable[n], np.shape(2,self.numactions+1))

            for i in range(0,self.numactions):
                if n == winningbidder:                  
                    if AuctionHistoryTable[i][n] == "Bid":
                        self.Qtable[n][0,i] = self.Qtable[n][0,i] + self.alpha*(reward + self.gamma * np.max(self.Qtable[n][:,i+1])-self.Qtable[n][0,i])
                    else:
                        self.Qtable[n][1,i] = self.Qtable[n][1,i] + self.alpha*(reward + self.gamma * np.max(self.Qtable[n][:,i+1])-self.Qtable[n][1,i])
                else:
                    if AuctionHistoryTable[i][n] == "Bid":
                        self.Qtable[n][0,i] = self.Qtable[n][0,i] + self.alpha*(fee + self.gamma * np.max(self.Qtable[n][:,i+1])-self.Qtable[n][0,i])
                    else:
                        self.Qtable[n][1,i] = self.Qtable[n][1,i] + self.alpha*(fee + self.gamma * np.max(self.Qtable[n][:,i+1])-self.Qtable[n][1,i])
                    # TODO: FIX Q TABLE, IDK WHAT REWARD SHOULD BE
                    # QTable Rows are "Bid" "Pass", Columns are auction round. 
    
    def action(self):
            self.numactions = self.numactions + 1
            RoundActionTable = []

            for i in range(0,self.numagents):

                if len(self.Qtable[i][0]) < self.numactions+1:
                    self.Qtable[i] = np.resize(self.Qtable[i], np.shape([np.zeros(self.numactions+1),np.zeros(self.numactions+1)]))

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

        if self.AuctionHistory[-1].count("Bid") == 1:
            self.winningbidder = self.AuctionHistory[-1].index("Bid")

        reward = self.value - self.winningbid - self.fee

        print(reward)
        Agent.PrevActionTable = ["Bid" for _ in range(0,Agent.numagents)]
        Agent.numactions = 0
        Agent.updateQtable(self, self.winningbidder, reward, fee)

# Agents: self, numagents, value, increment, alpha, epsilon, gamma
# Auctions: self, numagents, value, increment, fee

numagents = 2
value = 10
increment = 1
alpha = 0.6
epsilon = 0.2
gamma = 0.8
fee = 1
B = Agent(numagents, value, increment, alpha, epsilon, gamma, PossibleActionTable=["Bid", "Pass"])
for i in range(0,1000):
    A = Auction(numagents, value, increment, fee)
    A.run_auction(B)
