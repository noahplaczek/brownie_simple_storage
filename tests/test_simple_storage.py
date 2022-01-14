# file name must start with "test"
from brownie import SimpleStorage, accounts

# run all tests with: brownie test
# run a single test with: brownie test -k "nameOfTest"
# enter python shell upon failure (analyze): brownie test --pdb
# additional information and print lines: brownie test -s


def test_deploy():
    # Arrange: setup
    account = accounts[0]
    # Act: what we're actually testing
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_update_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    # Assert
    assert expected == simple_storage.retrieve()
