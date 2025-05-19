import time
import hashlib
import json

#the blockchain okembs
class Blockchain : 
    def __init__(self ,  timestamp  , transactions ,prior_hash = ''  )   :
       # self.index = index
        self.prior_hash = prior_hash 
        self.transactions = transactions
        self.coin = 0 
        self.timestamp = timestamp
        self.hash = self.create_hash()


    def create_hash(self) :
      #  block_string = f'{self.index} {self.prior_hash}{self.timestamp}{self.data}'.encode()
        #update by converting them to string them i will create a transaction class
        block_string2 = (str(self.prior_hash) +str(self.timestamp ) + str(self.transactions) + str(self.coin)).encode()
        return  hashlib.sha256(block_string2).hexdigest()
    
    #implemeting proof of work for the blockchain
    def mine_crypto(self , diff) : 
         print(self.hash[:diff])
         target = '0' * diff
         while self.hash[:diff] != target : 
              self.coin += 1
              self.hash = self.create_hash()
              print(f'crypto : hash :{self.hash} coin: {self.coin} ')
    



#for any Transaction call this class Transaction
class Transaction: 
     def __init__(self , sender_addr , recv_addr, amount) :
          self.sender_addr = sender_addr 
          self.recv_addr = recv_addr 
          self.amount = amount 
          
# the name of the blocchain okembs coin
class OkembsChain : 
    def __init__(self ):
        self.chain = [self.create_genesis_block()]
        self.difficult = 2 
        self.pending_Transactions = []
        self.mining_reward = 9
        
        

    def create_genesis_block(self) : 
          #create an array of block 
          return Blockchain(time.time() , [] , '0')
         # return Blockchain(1 , '04/03/2026', 'okembscoin' , '0') 

    def get_lastBlock(self) : 
            return self.chain[-1]

    def add_block(self, new_block):
        new_block.prior_hash = self.get_lastBlock().hash
        new_block.hash = new_block.create_hash()
        self.chain.append(new_block)

    def mining_pendingTransaction(self , miningAddress) : 
         #creating a new Block with all the whole pending transactions 
         block = Blockchain(time.time() , self.pending_Transactions , self.get_lastBlock())
         #call the mine_crypto func to mine
         block.mine_crypto(self.difficult)
         #apppend the block to the chain
         self.chain.append(block)

         #reset the transaction back 
         #calling the transactions class here 
         self.pending_Transactions = [Transaction(None , miningAddress , self.mining_reward)]
         pass
    

    #function for creating the transaction 
    def create_transaction(self , transaction) : 
         self.pending_Transactions.append(transaction)

    def get_Balance_Address(self , Address) : 
         balance:int  = 0 

         #loop and iterate between values
         for xBlock in self.chain : 
              for xtranc in xBlock.transactions : 
                   if xtranc.sender_addr  == Address : 
                         balance -= xtranc.amount
                   if xtranc.recv_addr == Address : 
                       balance += xtranc.amount
         return balance
                    

         
         

    #func to check if the Blockchain is valid 
    def isValid(self) : 
         for x in range( 1, len(self.chain)) : 
              current_block = self.chain[x]
              previous_block = self.chain[x - 1]
              print(f'previous Block : {previous_block }')
              print(f'current Block : {current_block.hash}')

             #check if the current block is correct 
              if current_block.hash != current_block.create_hash() : 
                   return False 
              #check if the current blockPoints is correct to the previous own 
              if current_block.prior_hash == current_block.create_hash() : 
                   return False 
              
              return True 
        




OkCoin = OkembsChain();
print(OkCoin)
OkCoin.create_genesis_block();
OkCoin.create_transaction(Transaction('address1' , 'adress2' , 10))
OkCoin.create_transaction(Transaction('address24' , 'adkfrrrmcmfhgoro' , 30))
OkCoin.mining_pendingTransaction('address1')
get_chain = json.dumps(OkCoin.chain , default=lambda o : o.__dict__ , indent=4)
print(get_chain)
