# tarkasti
Crowdsourcing fact-checking

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

## Cool
identify domain experts
1. Pull twitters graph
2. Cluster
3. Label clusters
4. Indentify nodes with highest amount of folowers inside cluster (normalized?)
5. Profit

## Cons
- Not scalable

### But it's not as trsutless as what TruStory is building, right?
If we examine the threat model...

### Why is it called tarkasti?
tarkatsi is a finnish word that means "True", "precisely", "faithfully"...

### What is the purpose of all this?
The whole point is to build a Proof-of-Concept for TruStory to get them to hire me as an intern.
