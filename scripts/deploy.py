import os
from brownie import network, accounts, config, Hello
#INFURA_API = 

def main():
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    hello = Hello.deploy({'from': dev})
    print(hello.address)