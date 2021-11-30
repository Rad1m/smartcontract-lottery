// SPDX-License-Identifier: MIT
pragama solidity ^0.6.6;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract Lottery {

    address payable[] public players;
    uint256 public usdEntryFee;
    AggregatorV3Interface internal ethUSDPriceFeed;

    constructor(address _priceFeedAddress) public {
        usdEntryFee = 50 *(10**18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }

    function enter() public payable {
        // $50 minimum fee
        players.push(msg.sender);
    }


    function getEntranceFee() {     
    }


    function startLottery() public {}

    function endLottery() public {}
}