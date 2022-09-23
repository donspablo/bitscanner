![image](https://user-images.githubusercontent.com/6468571/191927625-55edf5b9-267d-4c41-ae18-ac718ee25d3b.png)

<p align="center">🦄 PLEASE REMEMBER TO SMASH THE ⭐🔨 BUTTON AND <a href="https://github.com/sponsors/donspablo/dashboard">SUPPORT</a> 🌈 THANK YOU.</sub></sup></p>
<p align="center">📢<sub><sup> <i><b> YOUR SUPPORT IS GREATLY APPRECIATED / </b> <a href="https://www.patreon.com/donPabloNow">PATREON.COM/DONPABLONOW</a> / <b>BTC</b>  3HVNOVVMLHVEWQLSCCQX9DUA26P5PRCTNQ / <b>ETH</b> 0X3D288C7A673501294C9289C6FC42480A2EA61417 </i> </p>
  
<p align="center"><img src="https://user-images.githubusercontent.com/6468571/191125670-003a61ea-411f-42c0-b820-ad19124307a8.png"></img></p>

  | <p align="center"><img height="150px" src="https://user-images.githubusercontent.com/6468571/191125131-4e76fe43-770b-49e8-aa66-d1c8723f7e7a.png"></img></p><sub><sup><a href="https://github.com/4dboard/Proxy-yxorP">YXORP PROXY</a>: Web Proxy 🐮 yxorP: SAAS(y) Guzzler + App (GUI Dashboard incl.). Feature Rich, Multi-tenancy, Headless, Plug & Play, Augmentation & Content Spinning Web Proxy with Caching - PHP CURL+Composer are Optional. Leveraging SAAS architecture to provide multi-tenancy, multiple threads, caching, and an article spinner service.</sub></sup> | <p align="center"><img height="150px" src="https://user-images.githubusercontent.com/6468571/191125113-9d991af2-f911-43df-8994-a573aaf9a7ac.png"></img></p><sub><sup><a href="https://github.com/meanos/meanOs">MEANOS</a>: The operating system with the smallest memory footprint and the highest performance levels. NEW RELEASE A new version of the Web3 operating system will be released in the near future. https://mean.ơs.com. Operating systems have been subjected to significant revisions; if you would want to be informed when the subsequent version is made available, please subscribe.</sub></sup> |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<p align="center"><img src="https://user-images.githubusercontent.com/6468571/191124256-20415448-9bd5-4879-bfff-cca988bd7bfa.png"></img></p>

# Bitscanner Bitcoin Brute Forcer

Bitscanner is a Bitcoin wallet collider that use brute force to do transactions on random wallet addresses in an effort to detect a wallet containing money. It does this by simultaneously completing transactions on an enormous number of wallets. This is done in an effort to locate a wallet or other container carrying money. It should not be considered more than a proof-of-concept at this moment owing to the remote possibility that it may connect to a bitcoin wallet. The likelihood of it being linked to a Bitcoin wallet is low, hence it was just created for educational purposes.

Given that Bitcoin wallet addresses are created randomly, it is possible for two wallets to seem to have identical addresses. However, this is not the case. The owners of both wallets would have access to and be able to spend the same amount of money if this were the case. Alternatively, the opposite is true. Each Bitcoin wallet has a unique address. Shocking? Please do not get your expectations up, since the probability of this occurring is rather low. You will be notified when this content becomes available. Consider the likelihood that a similar situation may occur in the future. Bitcoin users have access to a maximum of 2^160 addresses at any one time.

When the address generator is configured to generate addresses at random, statistical analysis may be used to determine the possibility that two distinct wallets would create the same address. This is possible when the address generator is configured to generate addresses at random. This is theoretically conceivable if the generator is configured to produce random addresses. Please read the following article to enhance your mathematics knowledge.Therefore, the possibility of an address collision, often known as your wallet randomly producing the same address as another wallet, is 1 in 6.35.10^24, which is very low. This indicates that the probability of address information inconsistency is rather low. However, the reason for such a large number is unknown.

# Like This Project? Give It A Star

[![](https://img.shields.io/github/stars/donspablo/Bitscanner.svg)](https://github.com/donspablo/Bitscanner)

# Dependencies

<a href="https://www.python.org/downloads/">Python 3.6</a> or higher

Python modules listed in the <a href="/requirements.txt">requirements.txt<a/>
  
Minimum <a href="#memory-consumption">RAM requirements</a>

# Installation

```
$ git clone https://github.com/donspablo/bitscanner.git bitscanner

$ cd bitscanner && pip3 install -r requirements.txt
```

# Quick Start

```
$ python3 bitscanner.py
```

# How It Works

Using the os.urandom() method to generate private keys provides a high level of cryptographic security. These private keys are then stored as 32-byte hexadecimal strings. Using this string as the key, the contents are encrypted, resulting in ciphertext. Using the'starkbank-ecdsa' Python package, the private keys are converted to their respective hosts' public keys. This is done to secure the secrecy of the private keys. The 'binascii' and 'hashlib' standard libraries are then used to turn the public keys into their corresponding Bitcoin wallet addresses. The process of creating Bitcoin addresses has completed.


The establishment of a database comprising all precalculated P2PKH Bitcoin addresses and the corresponding amount of cash is a significant aspect of this project. This database includes Bitcoin addresses for the P2PKH project. Detailed information on each of the addresses is provided below. If the newly formed address includes a balance, the private key, public key, and wallet address are placed in the text file "success.txt" on the user's hard drive. Only if the freshly formed address has a balance is this true. Even if it finds out that the questioned address is cashless, the transaction will proceed routinely. This occurrence occurs immediately after a database search for the newly created address has been finished. Only if the given address has an outstanding balance will this occur. This application employs parallel computing to do computations in parallel. In specifically, the questioned function leverages parallel processing "parallel processing Process()."

# Proof Of Concept

Private keys, also known as secret numbers, are required to spend bitcoins. Private keys consist of numbers. If a wallet already contains Bitcoins, the private key permits the user to manage the wallet and spend any Bitcoins or other cryptocurrencies it contains. A user with access to the public key of a Bitcoin wallet cannot add Bitcoins to an empty wallet. This is true only if the private key is used to access the wallet. This program attempts to determine the Bitcoin private keys for wallets with a credit balance. Due to our inability to determine which private keys control wallets containing funds and which control wallets without funds, we are compelled to randomly examine all possible private keys in the hopes of discovering one that contains a balance. It is impossible to determine which private keys govern wallets with or without funds. It is impossible to distinguish between private keys that control wallets with funds and those that do not. This is due to an inability to distinguish between the two.

This piece of software is fundamentally an algorithm for making educated guesses using brute force. This is achieved by continuously generating Bitcoin private keys at random, converting them into their respective wallet addresses, and then checking the balance of each wallet address. This is referred to as "mining." When a wallet's balance is confirmed, the user's private key, public key, and wallet address are stored on their local hard drive in a text file named "success.txt." This file is accessed each time the wallet is rescanned. This file is accessed during the examination of a wallet containing a balance. The ultimate objective is to devise a method for generating random numbers in order to choose one of the 2160 possible wallets with a positive balance. Currently, there are 2160 wallets available, bringing the total number of wallets that can be used to 2160.

# Expected Output

When this software checks the balance of an address that the user has specified, the user will get a notification alerting them of the outcome of the check each time the program does the check. In the event that it is discovered that a wallet does not contain any funds, the address of the wallet will be stored on the device that is processing the transaction in the "failed.txt". 

On the other hand, if a wallet that has a balance is discovered, all of the pertinent information about that wallet will be written down and stored in the text file known as "success.txt." Here's an example:

>Wallet Address: 1Kz2CTvjzkZ3p2BQb5x5DX6GEoHX2jFS45
>Public Key: 04393B30BC950F358326062FF28D194A5B28751C1FF2562C02CA4DFB2A864DE63280CC140D0D540EA1A5711D1E519C842684F42445C41CB501B7EA00361699C320
>Private Key (Hex): 5A4F3F1CAB44848B2C2C515AE74E9CC487A9982C9DD695810230EA48B1DCEADD
>Private Key (WIF): 5JW4RCAXDbocFLK9bxqw5cbQwuSn86fpbmz2HhT9nvKMTh68hjm

# Memory Consumption

This application requires around 2 GB per CPU of random access memory (RAM). Due to the software's use of multiprocessing, it is hard to establish how much RAM it really needs. We kept a careful eye on this piece of software while it tried to brute-force identify 10,000 addresses on a system that had four logical processors and eight gigabytes of memory. The stack trace for memory use may now be produced as a direct result of this issue, which means that it is now possible to do so. As a direct consequence of this, there are now four child processes, and the amount of random access memory (RAM) required by each is around 2 gigabytes (RAM).

# Efficiency

It takes `0.0032457721` seconds for this progam to brute force a __single__ Bitcoin address. 

However, through `multiprocessing.Process()` a concurrent process is created for every CPU your computer has. So this program can brute force addresses at a speed of `0.0032457721 ÷ cpu_count()` seconds.



# Database FAQ

In order to determine the balance of Bitcoin addresses that have already been created, it is necessary to make use of an offline database. 
