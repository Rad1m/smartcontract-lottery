from scripts.helpful_scripts import get_account, get_contract, fund_with_link, bcolors
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
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print(f"{bcolors.OKGREEN}\nDeployed lottery!\n{bcolors.ENDC}")
    return lottery


def start_lottery():
    account = get_account()
    lottery = Lottery[-1]
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)  # wait for transaction to finish
    print(f'{bcolors.OKGREEN}\n"The lottery has started!\n{bcolors.ENDC}")


def enter_lottery():
    account = get_account()
    lottery = Lottery[-1]
    value = lottery.getEntranceFee() + 100000000
    tx = lottery.enter({"from": account, "value": value})
    tx.wait(1)  # wait for transaction to finish
    print(f"{bcolors.WARNING}\nYou entered the lottery!\n{bcolors.ENDC}")


def end_lottery():
    account = get_account()
    lottery = Lottery[-1]
    # fund the contract with LINK token
    # then end the lottery
    tx = fund_with_link(lottery.address)
    tx.wait(1)  # wait for transaction to finish
    ending_transaction = lottery.endLottery({"from": account})
    ending_transaction.wait(1)
    i = 60
    while i > 0:
        print(f"{bcolors.OKCYAN}Waiting ... {i} seconds{bcolors.ENDC}\r")
        time.sleep(1)
        i -= 1
    print(
        f"{bcolors.OKGREEN}{lottery.recentWinner()} is the new winner!\n{bcolors.ENDC}"
    )


def main():
    deploy_lottery()
    start_lottery()
    enter_lottery()
    end_lottery()
