// 1. The highestBid is higher than or equal to any other bid. You may assume that address(0) cannot place a bid.

// 2. The bid of the highestBidder equals the highestBid.

// we write into existance some getters:
methods {
    function bids(address) external returns (uint256) envfree;
    function highestBid() external returns (uint256) envfree;
    function highestBidder() external returns (address) envfree;

}
// q How do I target all other bids to compare to highestBid?


    // pass bidder as a virtual arg:
    // the getter `bids` with arg `bidder` returns all possible bids
invariant integrityOfHighestBid(address bidder) bids(bidder) <= highestBid();

// we need: 1. higest bidder, 2. highest bid
invariant highestBidderHasHighestBid() 
(highestBidder() != 0) => (bids(highestBidder()) == highestBid());  
