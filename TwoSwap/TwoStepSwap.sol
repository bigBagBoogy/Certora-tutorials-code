// SPDX-License-Identifier: SEE LICENSE IN LICENSE
pragma solidity 0.8.17;

import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// fix import + pseudo code

contract TwoStepSwap {
    struct Swap {
        address user;
        uint256 amount;
        address[] swapPath;
        bool unwrapNativeToken;
    }

    uint256 swapNonce;
    mapping(uint256 => Swap) pendingSwaps;

    function createSwap(uint256 _amount, address[] memory _swapPath, bool _unwrapNativeToken) external {
        IERC20(_swapPath[0]).safeTransferFrom(msg.sender, address(this), _amount);
        pendingSwaps[swapNonce++] =
            Swap({user: msg.sender, amount: _amount, swapPath: _swapPath, unwrapNativeToken: _unwrapNativeToken});
    }

    function cancelSwap(uint256 _id) external {
        Swap memory swap = pendingSwaps[_id];
        require(msg.sender == swap.user);
        delete pendingSwaps[_id];

        IERC20(swap.swapPath[0]).safeTransfer(swap.user, swap.amount);
    }

    function executeSwap(uint256 _id) external onlySwapExecuter nonReentrant {
        Swap memory swap = pendingSwaps[_id];

        // If a swapPath ends in WETH and unwrapNativeToken is true, send ether to the user
        ISwappwer(swapper).swap(swap.user, swap.swapPath, swap.amount, swap.unwrapNativeToken);
        delete pendingSwaps[_id];
    }
}
