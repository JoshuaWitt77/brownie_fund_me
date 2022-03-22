from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account, 
    deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)
from web3 import Web3

def deploy_fund_me():
    account = get_account()

    # if we are on rinkbey so on - use associated address
    # otherwise deploy moks

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS: 
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        # Deploy fake get price function is the network is fake like Ganeche  
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        publish_source = config["networks"][network.show_active()].get("verify")
    )
    
    print(f'\n\n')
    print(f'Active network is {network.show_active()}')
    print(f'Price_feed_address is {price_feed_address}')
    print(f'From account is {account}')
    print(f'Contract deployed to {fund_me.address}')
    print(f'For second git commit')
    print(f'\n\n')

    return fund_me

def main():
    deploy_fund_me()
