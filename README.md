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
consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
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
