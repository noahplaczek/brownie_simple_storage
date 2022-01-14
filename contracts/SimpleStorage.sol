// SPDX-License-Identifier: MIT
// license identifier. this is the most common and means that anyone can use the code.

pragma solidity ^0.6.0;

contract SimpleStorage {
    // uint, int... most will do uint256 to be more precise
    // uint is unsigned i.e. not positive or negative
    // integers are whole numbers
    // 256 means it is an integer of 256 bytes

    // this will get initialized to 0
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    // People public person = People({favoriteNumber: 2, name: "Josh"});

    People[] public people;

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }

    // takes a key and returns the variable it is mapped to
    mapping(string => uint256) public nameToFavoriteNumber;

    /*
    bool favoriteBool = false;
    string favoriteString = "String";
    int256 favoriteInt = -5;
    address favoriteAddress = 0xdf0B3E2218b3bfb128eaEc6142F84227fC00bbDE;
    bytes32 favoriteBytes = "cat"; // converts to a bytes object
    */

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    // view, pure
    //... just reading off the blockchain, so don't need to make a transaction.
    // they do not save the state
    // public variables also have view functions
    // pure functions purely do math
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function retrieve2(uint256 _favoriteNumber) public pure {
        _favoriteNumber + _favoriteNumber;
    }
}
