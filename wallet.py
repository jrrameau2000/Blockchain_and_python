# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
from constants import *
from bit import *
from web3 import Web3, HTTPProvider
from eth_account import Account
from bit import Key, PrivateKey, PrivateKeyTestnet
from bit.network import NetworkAPI
from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
mnemonic=os.getenv("mnemonic")
from variable import *


# Load and set environment variables
load_dotenv('mnemonic.env')
mnemonic=os.getenv("mnemonic")


# Create a function called `derive_wallets`
def derive_wallets(coin=BTC, mnemonic=mnemonic, depth=3):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --cols=all --coin={coin} --numderive={depth} --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)


# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {
    ETH: derive_wallets(coin = ETH),
    BTCTEST: derive_wallets(coin = BTCTEST),
}
print(coins)


# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
#CRreates wallet address or private key
def priv_key_to_account(coin, priv_key):
    if coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    elif coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    
Eth_PrivateKey = coins["eth"][0]['privkey']
Btc_PrivateKey = coins['btc-test'][1]['privkey']
print(Eth_PrivateKey)
print(Btc_PrivateKey)


# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin,account,to,amount):
    if coin == ETH:
        value= w3.toWei(amount,"ether")
        gas_estimate=w3.eth.estimateGas({'to':to,
                                        'from':account.address,
                                        'amount':value})
        gas_price=w3.eth.generateGasPrice()
        nonce=w3.eth.getTransactionCount(account.address)
        chainID=w3.eth.chain_id
        return {"to":to,
               'from':account.address,
               "value":value,
               "gas":gas_estimate,
               "gasPrice":gas_price,
               "nonce":nonce,
               "chainID":chainID}
            
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
    
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin,account,to,amount):
    raw_tx = create_tx(coin,account,to,amount)
    if coin == ETH:
        signedtx=account.signTransaction(raw_tx)
        return w3.eth.sendRawTransaction(signedtx.rawTransaction)
                
                
    if coin== BTC:
        signedtx=account.sign_transaction(raw_tx)
        return NetworkAPI.broadcast_tx_testnet(signedtx)

    
    
