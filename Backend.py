from fastapi import FastAPI
from BlockChain import OkembsChain
from BlockChain import Transaction 
from BlockChain import OkCoin
from BlockChain import Blockchain
from pydantic import BaseModel



app = FastAPI();




@app.get('/') 
async def root() : 
    return {'message': 'welcome to okembscoin'}

@app.get('/okembsCoin/{mine}')
async def crypto_mine(mine) : 
    return {'coins' : mine}


@app.post('/mineCrypto/{Adress}')
async def mine(Adress:str) :
    OkCoin.mining_pendingTransaction(Adress)
    return {'mined_coined' : 'succesfull' , "welcome": "homeboy" , "Address": Adress}
