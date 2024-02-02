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