# Tarkasti
> Crowdsourcing fact-checking

## What is it?
A wannabe TruStory clone that is implemented as a Twitter bot with an ethereum token on the rinkeby network. 

## Install
```bash
virtualenv --python=python3 venv
pip install -r requirements.txt
```
Then set up your API keys as outlined in the next section:

## API keys
Create a file named `secret.py` with the following contents:
```python
# Twitter's API keys
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# Account password as used in geth
gethPassword = 'XXXXXXXXXXXXX'
```

## Run
```bash
geth --syncmode "light" --rinkeby &
. venv/bin/activate
python bot.py
```

## How does it work?
1. Tweet a claim @tarkasti
2. Tarkasti will tweet your claim for everyone to see
3. Experts can vote on the veracity of the claim by replying to the tweet with either "true" or "false"
4. After a minute of voting, the side that has more voting power (a vote weight is decided by the balance of tokens of their owner) is elected as a winner
5. 20% of the tokens owned by each of the experts on the losing side are transferred to the experts on the winning side
The contract for the token being used is a (really) heavily modified version of OpenZeppelin's ERC20 contract and can be found on `contract/ERC20.sol`. The bot uses a deployment of it on the rinkeby network.

## Cool new things to explore
Currently the bot exploits twitter's network to decide how much tokens/trust should be put in a user by using the following function `e^(age)*followers`. But it's quite easy to see that usually experts are only experts in a specific area, so it would be really interesting to identify them and award domain-specific tokens to domain experts.  
A possible way to do that would be:
1. Pull twitters graph
2. Cluster
3. Label clusters
4. Indentify nodes with highest amount of folowers inside cluster (normalized?)
5. Profit

### Non-cool things to fix
- Race conditions caused by the interaction between blockchain and twitter bot
- Unchecked assumptions in code (marked in the source code)
- Make the voting blind to everybody else, revealing the results once the voting ends

## FAQ
### So is this what the TruStory team is building?
No, it's important to understand that this is just a proof of concept, and it has many shortcomings that the product Trustory is building doesn't have, such as:
- It is not scalable
- It has issues with traceability because in Twitter tweets can be deleted, edited...
- All token transferences are paid for by the bot, which introduces ultra-high maintenance costs
- ...
I chose to build it on Twitter because for a prototype it allowed me to get direct access to a huge audience of users that may be interested (essentially the entirety of Crypto Twitter), reducing a ton the friction these users would face if they wanted to use this (sending a tweet vs installing an app), while also letting me leverage Twitter's social graph to find experts (see "Cool new things to explore") to bootstrap the initial coin distribution.   
Also, some parts of the process a user goes through in the TruStory app have been remove to provide a better UX (eg: challenging a claim, in tarkasti voting starts automatically after a claim is issued).

### Is it as trustless as what TruStory is building?
It may seem that is not (as users don't hold their own private keys and all that), but because TruStory will use the Tendermint consesus algorith to drive their blockchain system, if you analyze the user's thread model it's possible to reach the conclusion that both (this bot's and TruStory's system) have the same thread model, therefore having the same 'trustlessness'.

### Why is it called tarkasti?
Tarkatsi is a finnish word that means "True", "precisely", "faithfully"...

### What is the purpose of all this?
The whole point is to build a Proof-of-Concept for TruStory to get them to hire me as an intern.
