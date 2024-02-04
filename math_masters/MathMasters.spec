

// The methods block below gives various declarations regarding solidity methods.
methods
{
    // When a function is not using the environment (e.g., `msg.sender`), it can be
    // declared as `envfree`
    function mulWad(uint, uint) external returns (uint) envfree;
    // function mulWadUp(uint256, uint256) external returns (uint256) envfree;
    // function sqrt() external returns (uint256) envfree;
}

rule mulWadDoesntRevert(uint x, uint y) {




    require x < max_uint256 - 1;
    require y < max_uint256 - 1;
    
    mulWad(x, y);
    assert !lastReverted;
}
