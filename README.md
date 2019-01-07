# Tarkasti
> Crowdsourcing fact-checking

## What is it?
A trustory clone 

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

## Cons
- Not scalable

### But it's not as trsutless as what TruStory is building, right?
If we examine the threat model...

### Why is it called tarkasti?
tarkatsi is a finnish word that means "True", "precisely", "faithfully"...

### What is the purpose of all this?
The whole point is to build a Proof-of-Concept for TruStory to get them to hire me as an intern.
