# twoSwap - cross-function reentrancy

It is often the case that reentrancy occurs across functions, and across contracts like this.

For this reason, you should make note of every single external call and examine the possibility of reentering the system through any function.

It is often helpful to simply grep the codebase for all external/public functions and evaluate the reentrancy risk for each one considering each external call.

Some reentrancies are sneakily hidden inside popular libraries/standards, such as ERC721.

Every time you transfer an ERC721 token to an address, the `onERC721Received` function is called at that address.

This means that the receiving address can take over the execution of the tx and possibly reenter into the smart contract system.

Pay very close attention when minting and transferring NFTs.

The check-effects-interactions pattern is an excellent approach to avoid reentrancies.

Executing all critical logic before making any external calls ensures that any invariants crucial to the system can still hold.
fravoll.github.io
Checks Effects Interactions

Note that in many cases, check-effects-interactions can be superior to a `nonReentrant` modifier, removing the possibility for cross-function reentrancy vulnerabilities like seen above + gas savings.

However, check-effects-interactions might not always be possible, in which case a combination of `nonReentrant` modifiers and careful review can mitigate Reentrancy vectors.

Reentrancy will continue to be a risk, especially in large smart contract projects that span multiple contracts.

Make sure to check those external calls. 🙏

If you thought this thread had valuable information about reentrancy, give it a retweet so we can reach more auditors and protect the ecosystem. 🫡

### in createSwap():
```diff
-  IERC20(_swapPath[0]).safeTransferFrom(msg.sender, _amount);           
+  IERC20(_swapPath[0]).safeTransferFrom(msg.sender, address(this), _amount); 
```