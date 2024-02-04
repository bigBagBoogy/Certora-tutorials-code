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
