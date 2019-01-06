pragma solidity ^0.4.24;

import "./SafeMath.sol";

/**
 * @title Mutilated and backdoored ERC20 token
 *
 * @dev Implementation of the basic standard token.
 * https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md
 * Originally based on code by FirstBlood: https://github.com/Firstbloodio/token/blob/master/smart_contract/FirstBloodToken.sol
 *
 */
contract ERC20 {
    using SafeMath for uint256;

    mapping (string => uint256) private _balances;
    mapping (string => bool) private _given;

    uint256 private _totalSupply;

    modifier onlyOwner(){
        require(msg.sender == address(0x9D30fc83B2467D2c7a1a1dC80943AA898ce0bBf6));
        _;
    }

    /**
    * @dev Total number of tokens in existence
    */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
    * @dev Gets the balance of the specified address.
    * @param owner The address to query the balance of.
    * @return An uint256 representing the amount owned by the passed address.
    */
    function balanceOf(string owner) public view returns (uint256) {
        return _balances[owner];
    }


    function mint(string to, uint256 value) public onlyOwner returns (bool) {
        require(_given[to]==false);
        _given[to]=true;
        _mint(to, value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another.
     * @param from address The address which you want to send tokens from
     * @param to address The address which you want to transfer to
     * @param value uint256 the amount of tokens to be transferred
     */
    function transferFrom(string from, string to, uint256 value) onlyOwner public returns (bool) {
        _transfer(from, to, value);
        return true;
    }

    event Transfer(string indexed from, string indexed to, uint256 value);

    /**
    * @dev Transfer token for a specified addresses
    * @param from The address to transfer from.
    * @param to The address to transfer to.
    * @param value The amount to be transferred.
    */
    function _transfer(string from, string to, uint256 value) internal {
        _balances[from] = _balances[from].sub(value);
        _balances[to] = _balances[to].add(value);
        emit Transfer(from, to, value);
    }

    /**
     * @dev Internal function that mints an amount of the token and assigns it to
     * an account. This encapsulates the modification of balances such that the
     * proper events are emitted.
     * @param account The account that will receive the created tokens.
     * @param value The amount that will be created.
     */
    function _mint(string account, uint256 value) internal {
        _totalSupply = _totalSupply.add(value);
        _balances[account] = _balances[account].add(value);
        emit Transfer("", account, value);
    }
}
