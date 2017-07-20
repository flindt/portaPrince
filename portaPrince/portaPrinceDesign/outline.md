Data structuress

    exchange rates class

    It holds the exchange rate for a given paper, and can download them if they are not in the cache. It should also be able to translate between the different yahoo, goole, nordnet and others specific naming conventions.

    The parper names comes from the config files below.

    target mix class

    Contains the target values for the mix. Will contain the concept of "group" of papers, and something about having specific share of a specific paper.
    Includes "cash" also?
    This originates from a config file, which is a manually written text file.

    Status and transactions

    How many of each paper do we have and which transactions have we made.

    This could be from a copy'n'paste from nordnet, or a manually written text file.

Business logic

    We want to be able to simulate a strategy based on historic data.
    We want it to be able to do recommendations for buying/selling based on a specific strategy.

Presentation layer:
