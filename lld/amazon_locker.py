# https://www.hellointerview.com/learn/low-level-design/problem-breakdowns/amazon-locker
# https://youtu.be/s6nGkoGJhXk (low level design)

# Design a locker system like Amazon Locker where delivery drivers can 
# deposit packages and customers can pick them up using a code.

# requirements -> entities -> class design -> implementation -> extensibility
# entities (state, behavior)
# implementation: seudo code or exact
# extensibility: how the desing could evolve w/ additiona capability

###### requirements ######
# questions to asks 3 categories: 
#     (main capabilities, error handling, scope boundary (in/out))
# main capabilities: 
# - compartment sizes
# - how do customers get the code
#
# error handling
# - unique access code
# - how long do the codes last
# - what if all comparments are full of a given size?

###### entities ######
# needed objects and how they interact w/ each other
# - look for the nouns in the requirements
# - package (is it in scope or out)
# - comparments, 
# - locker
# - access code

