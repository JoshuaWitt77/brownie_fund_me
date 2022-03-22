from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account, 
    deploy_mocks, 
    LOCAL_BLOCKCHAIN_ENVIRONMENTS
)
from web3 import Web3

def deploy_fund_me():
    account = get_account()

    print(f'Active network is {network.show_active()}')
    print(f'Active account is {account}')

    # if we are on rinkbey so on - use associated address
    # otherwise deploy moks
    # network.show_active() not in ['development', 'ganache-local']:  

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS: 
        # if our network is not Development or Lockal Ganache - then we go to get address of oracle in config
        print(f'Go to get Aggregator address of forked-network')
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
            ]
    else:
        # if our network is Development then go to Deploy fake
        print(f'Go to deploy mocks')
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account}, 
        publish_source = config["networks"][network.show_active()].get("verify")
    )
    
    print(f'\n\n')
    print(f'Contract deployed to {fund_me.address}')
    print(f'FundMe len is {len(FundMe)}')
    print(f'Price_feed_address is {price_feed_address}')
    print(f'\n\n')

    return fund_me

def main():
    deploy_fund_me()
