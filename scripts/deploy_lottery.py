from scripts.helpful_scripts import get_account, get_contract, bcolors
from brownie import Lottery, network, config
import time


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active].get("verify", False),
    )
    print(f"{bcolors.OKGREEN}\nDeployed lottery!\n{bcolors.ENDC}")


def main():
    deploy_lottery()
