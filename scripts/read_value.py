# Reads from the Rinkeby blockchain a value we have already deployed
from brownie import SimpleStorage, accounts, config

def read_contract():
    # A contract object works the same as an array, containing all addresses of the deployed contract
    # SimpleStorage[-1] will return the address of the most recent deployment
    simple_storage = SimpleStorage[-1]
    # ABI and Address stored in deployments folder
    print(simple_storage.retrieve())

def main():
    read_contract()