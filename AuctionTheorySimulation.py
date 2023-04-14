import matplotlib.pyplot as plt
import numpy as np
import random

class Agent:
    def __init__(self, numagents, value, increment, alpha, epsilon, gamma, PossibleActionTable):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.PossibleActionTable = PossibleActionTable
        self.numagents = numagents
        self.Qtable = self.initQtable(value, increment, numagents)
        self.numactions = 0
        self.PrevActionTable = ["Bid" for _ in range(0,numagents)]

        # for i in range(0,numagents):
            # self.Qtable.append(np.zeros((len(PossibleActionTable),value//increment), dtype = np.double))

    def initQtable(self, value, increment, numagents):
        Qtable = [np.zeros((2,value//increment,self.numagents),dtype = np.double) for _ in range(0,numagents)]
        return(Qtable)



    def updateQtable(self, Auction, winningbidder, reward, fee): # Q[state, action] = Q[state, action] + lr * (reward + gamma * np.max(Q[new_state, :]) — Q[state, action])
        AuctionHistoryTable = Auction.AuctionHistory
        for n in range(0,self.numagents):
            for i in range(0,len(AuctionHistoryTable)):
           # if self.Qtable[n] < self.numactions:
            #    np.resize(self.Qtable[n], np.shape(2,self.numactions+1))
                    # AucRow = AuctionHistoryTable[i]
                    BidCount = 0
                    if n == winningbidder:                  
                        if AuctionHistoryTable[i][n] == "Bid":
                            agentgain = reward
                            OldQvalue = self.Qtable[n][0, i, BidCount]
                            NewQvalue = OldQvalue + self.alpha * (reward + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - OldQvalue)
                            self.Qtable[n][0, i, BidCount] = NewQvalue
                            print("Agent " + str(n) + " won and took action Bid in round " + str(i))
                            print("Agent " + str(n) + " reward was " + str(agentgain) + " and his Q value was updated from " + str(OldQvalue) + " to " + str(NewQvalue))
                            # self.Qtable[n][0, i, BidCount] = self.Qtable[n][1, i, BidCount] + self.alpha * (reward + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - self.Qtable[n][0, i, BidCount])
                        else:
                            agentgain = reward
                            OldQvalue = self.Qtable[n][1, i, BidCount]
                            NewQvalue = OldQvalue + self.alpha * (reward + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - OldQvalue)
                            # self.Qtable[n][1, i, BidCount] = self.Qtable[n][1, i, BidCount] + self.alpha * (reward + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - self.Qtable[n][1, i, BidCount])
                            print("Agent " + str(n) + " won and took action Pass in round " + str(i))
                            print("Agent " + str(n) + " reward was " + str(agentgain) + " and his Q value was updated from " + str(OldQvalue) + " to " + str(NewQvalue))
                    else:
                        if AuctionHistoryTable[i][n] == "Bid":
                            agentgain = -1*fee
                            OldQvalue = self.Qtable[n][0, i, BidCount]
                            NewQvalue = OldQvalue + self.alpha * (agentgain + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - OldQvalue)
                            print("Agent " + str(n) + " lost and took action Bid in round " + str(i))
                            print("Agent " + str(n) + " agentgain was " + str(agentgain) + " and his Q value was updated from " + str(OldQvalue) + " to " + str(NewQvalue))
                            # self.Qtable[n][1, i, BidCount] = self.Qtable[n][1, i, BidCount] + self.alpha * (-1*fee + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - self.Qtable[n][0, i, BidCount])
                        else:
                            agentgain = -1*fee
                            OldQvalue = self.Qtable[n][1, i, BidCount]
                            NewQvalue = OldQvalue + self.alpha * (agentgain + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - OldQvalue)
                            print("Agent " + str(n) + " lost and took action Bid in round " + str(i))
                            print("Agent " + str(n) + " agentgain was " + str(agentgain) + " and his Q value was updated from " + str(OldQvalue) + " to " + str(NewQvalue))
                            # self.Qtable[n][1, i, BidCount] = self.Qtable[n][1, i, BidCount] + self.alpha * (-1*fee + self.gamma * np.max(self.Qtable[n][:, i + 1, BidCount]) - self.Qtable[n][1, i, BidCount])
                    # TODO: FIX Q TABLE, IDK WHAT REWARD SHOULD BE
                    # QTable Rows are "Bid" "Pass", Columns are auction round. 
        # self.alpha = self.alpha/1.01
        Agent.numactions = 0

    def action(self):
            RoundActionTable = []

            for i in range(0,self.numagents):

                if self.Qtable[i].shape[1] < self.numactions + 1:
                    self.Qtable[i] = np.resize(self.Qtable[i], (2, self.numactions + 1, self.numagents))

                if self.PrevActionTable[i] == "Pass":
                    self.currentaction = "Pass"
                    RoundActionTable.append(self.currentaction)
                    print("Agent " + str(i) + " has already passed!")

                elif np.random.rand() < self.epsilon:
                    self.currentaction = self.PossibleActionTable[random.randint(0,1)]
                    RoundActionTable.append(self.currentaction)
                    print("Agent " + str(i) + " took a random action!")

                else:
                    # print(str(self.Qtable[i][:,self.numactions]))
                    NumBids = 0
                    self.currentaction = self.PossibleActionTable[np.argmax(self.Qtable[i][:,self.numactions, NumBids])]
                    # print(self.currentaction)
                    RoundActionTable.append(self.currentaction)
                    print("Agent " + str(i) + " took action " + str(self.currentaction) + " since the Q value was highest between " + str(self.Qtable[i][:,self.numactions, NumBids]))
            self.PrevActionTable = RoundActionTable
            print(RoundActionTable)
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
        # if CurrentActions.count("Pass") == self.numagents:
            # CurrentActions = Agent.action()
        Agent.numactions = Agent.numactions + 1
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

        print("Total Reward for Auction: " + str(reward))
        print("The winning bidder is: " + str(self.winningbidder))
        print("With winning bid: " + str(self.winningbid))
        RewardOverTime.append(reward)
        Agent.PrevActionTable = ["Bid" for _ in range(0, Agent.numagents)]
        Agent.updateQtable(self, self.winningbidder, reward, self.fee)

# Agents: self, numagents, value, increment, alpha, epsilon, gamma
# Auctions: self, numagents, value, increment, fee

numagents = 2
value = 20
increment = 1
alpha = 0.7
epsilon = 0.1
gamma = 0.8
fee = 10
RewardOverTime = []
numiterations = 1000
iteration = np.arange(0,numiterations)
B = Agent(numagents, value, increment, alpha, epsilon, gamma, PossibleActionTable=["Bid", "Pass"])
for i in range(0,numiterations):
    print("------------------------- NEW AUCTION ------------------------")
    A = Auction(numagents, value, increment, fee)
    A.run_auction(B)
plt.plot(iteration,RewardOverTime)
plt.show()