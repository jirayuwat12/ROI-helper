import json
import argparse
import os
import sys

from recipe import get_recipe
from utils import get_fact_dic
from controller import Controller

arg = argparse.ArgumentParser()
arg.add_argument("-n",
                 "--name",
                 required=False,
                 type=str,
                 help="Name of the target")

arg.add_argument("-apd",
                "--amount_per_day",
                required=False,
                type=str,
                help="Amount of output needed per day")

arg.add_argument("-v",
                "--version",
                default="2130",
                type=str,
                help="Version of the target")


if __name__ == "__main__":
    if arg.parse_args().name is None and arg.parse_args().amount_per_day is None:
        controller_instance = Controller()
        controller_instance.run()

    elif arg.parse_args().name is None or arg.parse_args().amount_per_day is None:
        if arg.parse_args().name is None:
            print("Please provide a name")
            sys.exit(0)
        elif arg.parse_args().amount_per_day is None:
            print("Please provide a amount_per_day")
            sys.exit(0)
    else:
        factory_dic = get_fact_dic({
            "name": arg.parse_args().name,
            "amount_per_day": arg.parse_args().amount_per_day,
            "version": arg.parse_args().version
        })

        print(f"Result for {arg.parse_args().name} ({eval(arg.parse_args().amount_per_day)*30:.2f} per month):")
        factory_list = factory_dic.items()
        factory_list = sorted(factory_list, key=lambda x: x[1]["from"], reverse=True)
        for obj, factory in factory_list:
            print(f"\t{obj} from {factory['from'].upper()} : {round(factory['factory'],1)} factory")
