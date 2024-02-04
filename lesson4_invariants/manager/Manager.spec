/**
 * # Spec for funds manager `IManager.sol`
 * Write an invariant verifying that no two funds have the same manager.
 */
methods {
    function getCurrentManager(uint256) external returns (address) envfree;
    function getPendingManager(uint256) external returns (address) envfree;
    function isActiveManager(address) external returns (bool) envfree;
}
// need all funds
// need 

invariant noTwoFundsHaveTheSameManager() manager[funds] != manager[funds]