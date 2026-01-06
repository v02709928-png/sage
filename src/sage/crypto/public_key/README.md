Public Key Cryptography in Sage
===============================

This directory contains experimental infrastructure for public-key
cryptography in Sage.

The goal of this framework is to provide a common, math-oriented API for
prototyping public-key cryptographic schemes using Sage’s existing
mathematical objects (groups, rings, curves, etc.), rather than thin
wrappers around external libraries.

### Design principles

- Focus on correctness and clarity over performance.
- Schemes are expressed in terms of mathematical objects already
  available in Sage.
- Base classes are intended to expose common invariants that can be
  tested automatically using Sage’s TestSuite.

### Testing and correctness

As new public-key protocols (starting with key exchange) are added, it
is expected that implementations expose standardized correctness checks.
For example, key exchange protocols should be able to assert shared-
secret agreement between two parties.

This allows Sage’s TestSuite to validate implementations automatically
and helps catch misuse (e.g. incompatible parameters) early.

