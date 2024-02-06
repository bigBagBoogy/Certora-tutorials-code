# Tutorials code

This repository contains the code examples for the
[Certora Prover Tutorials](https://docs.certora.com/projects/tutorials/en/latest/).
The [Certora Prover](https://www.certora.com/) is a formal verification tool for
smart contract. The tutorials are part of the
[Certora Prover Documentation](https://docs.certora.com/en/latest/).

first run:   `export CERTORAKEY=your_certora_key_here`

then run the command to scan from the tutoral folder (so you need th `cd` into it)

example: ```certoraRun ERC20.sol --verify ERC20:ERC20.spec```

always omit the suggested ```--solc solc8.0```

When using a `.conf` file run: `certoraRun YourFile.conf`

to run only 1 specific rule use the flag:  `--rule yourRule`

Important: Optimistic loop
When running the spec ERC20.spec you must add "optimistic_loop": true to your config file, or use --optimistic_loop flag if running from command line. Otherwise, you will get a violation whenever the Prover encounters the getters name() and symbol(). The violation occurs because the Prover uses loops to handle strings, or any dynamic array. Loops require special care and handling which we will address in a later lesson. For now, simply use this flag whenever you have a string.

## see this for the symbols used
https://docs.certora.com/en/latest/docs/cvl/invariants.html#invariants-and-induction

=> means: "implies"       so:

``` javascript
transfer(e, recipient, amount);
// amount being more than 0 `implies` that balance has gone up (balanceAfter > balanceBefore)
assert amount > 0 => balanceAfter > balanceBefore
// below is possible too, here the assertion checks both ways, so: "if balance increased, check that amount was greater than `0`"
assert amount > 0 <=> balanceAfter > balanceBefore
```

In predicate logic, the symbol used to represent `"for all"` is the universal quantifier, often denoted by the symbol "`∀`" (pronounced "for all"). So, if you have a statement like "For all x, P(x)," you would write it as "∀x P(x)," where P(x) is a predicate representing some property or condition involving the variable x.


## playlist Certora tutorial:

https://www.youtube.com/watch?v=CwCX0TuDfTE&list=PLKtu7wuOMP9XHbjAevkw2nL29YMubqEFj&index=2

### ***ALWAYS:*** use MUST or MUST NOT in your assert messages, so it's clear what supposed to happen.

Certora IS available in your other projects, but NOT "checkable" by running: 
`certora --version`
Thing is tho, you need to be inside the folder where your `.sol` is when running `certoraRun`
