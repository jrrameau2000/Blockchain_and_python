# Blockchain_and_python
Making Python interact with Blockchain. Generated a few wallets and private keys and attempted to send transactions with those generated wallets

## Modules used
These modules were installed in order to do this project.

<img width="473" alt="modules" src="https://user-images.githubusercontent.com/79224741/127550415-50872dc4-fae1-4c9a-8125-72883316b198.png">

## Create function 'derive_wallet'
The following flags must be passed into the shell command as variables:

Mnemonic (--mnemonic) must be set from an environment variable, or default to a test mnemonic
Coin (--coin)
Numderive (--numderive) to set number of child keys generated
Format (--format=json) to parse the output into a JSON object using json.loads(output)
<img width="711" alt="derive_wallet" src="https://user-images.githubusercontent.com/79224741/127550399-12bb7548-f04e-4233-93ee-a8e2d977dfc3.PNG">

## Create function 'private_key'
This function will convert the privkey string in a child key to an account object that bit or web3.py can use to transact.


This function needs the following parameters:


coin -- the coin type (defined in constants.py).

priv_key -- the privkey string will be passed through here.



You will need to check the coin type, then return one of the following functions based on the library:

For ETH, return Account.privateKeyToAccount(priv_key)

This function returns an account object from the private key string. You can read more about this object here.


For BTCTEST, return PrivateKeyTestnet(priv_key)

This is a function from the bit libarary that converts the private key string into a WIF (Wallet Import Format) object. WIF is a special format bitcoin uses to designate the types of keys it generates.

<img width="593" alt="private_key" src="https://user-images.githubusercontent.com/79224741/127550430-3c03d3ab-c4f6-4313-b711-0b296e383af8.PNG">

## Create dictionary 'Coin' to use for functions
<img width="868" alt="coins" src="https://user-images.githubusercontent.com/79224741/127550365-e59fabc9-6b06-4e1e-a2e0-339a9acb99e0.PNG">

## Create function 'create_tx'
This function will create the raw, unsigned transaction that contains all metadata needed to transact.


This function needs the following parameters:


coin -- the coin type (defined in constants.py).

account -- the account object from priv_key_to_account.

to -- the recipient address.

amount -- the amount of the coin to send.

<img width="575" alt="create_tx" src="https://user-images.githubusercontent.com/79224741/127550381-9f133859-24a4-4345-bc63-8bc0506645c7.PNG">


## Create function 'send_tx'

This function will call create_tx, sign the transaction, then send it to the designated network.


This function needs the following parameters:


coin -- the coin type (defined in constants.py).

account -- the account object from priv_key_to_account.

to -- the recipient address.

amount -- the amount of the coin to send.



You may notice these are the exact same parameters as create_tx. send_tx will call create_tx, so it needs all of this information available.

<img width="547" alt="send_tx" src="https://user-images.githubusercontent.com/79224741/127550456-ce23aedc-8fef-40d4-abbd-75bb0330edb4.PNG">
