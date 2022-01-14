# brownie has an accounts package
from brownie import (
    accounts,
    config,  # config is used since we are grabbing env variables from config file
    SimpleStorage,  # brownie allows you to import contracts directly into the script
)

# "import os" only needed if loading directly from the .env


def deploy_simple_storage():
    account = accounts[0]
    # must always add who you are going to transact from
    simpleStorage = SimpleStorage.deploy({"from": account})
    # brownie knows whether you are making a transaction or a call
    stored_value = simpleStorage.retrieve()
    print(stored_value)
    transaction = simpleStorage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simpleStorage.retrieve()
    print(updated_stored_value)


# def deploy_simple_storage():
# GANACHE-CLI
# account = accounts[0]
#
# TESTNET
# in the command line use: brownie accounts new "accountName"
# account = accounts.load("test-account")
#
# ENVIRONMENT VARIABLES FROM ENV
# account = accounts.add(os.getenv("PRIVATE_KEY"))
#
# ENVIRONMENT VARIABLES FROM CONFIG
# account = accounts.add(config["wallets"]["from_key"])


def get_account():
    if network.show_active() == "development":
        return


def main():
    print("test")
    deploy_simple_storage()
