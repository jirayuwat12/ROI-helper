# ROI-helper

This is python program that help **Rise of Industry (ROI)** player tocalculate the nessessary amount of factory to produce a certain amount of demand.

## Table of Contents
- [ROI-helper](#roi-helper)
  - [Table of Contents](#table-of-contents)
  - [How to use ?](#how-to-use-)
    - [Use the program directly](#use-the-program-directly)
      - [Example to plan individual demands](#example-to-plan-individual-demands)
      - [Example to plan multiple demands](#example-to-plan-multiple-demands)
    - [Use the program with command line](#use-the-program-with-command-line)
      - [Example to plan individual demands](#example-to-plan-individual-demands-1)
  - [For Your Information](#for-your-information)
  
## How to use ?
There are 2 ways to use this program.
1. Use the program directly
1. Use the program with command line

### Use the program directly
1. Must installed python.
1. Clone this repository.
1. Run `python main.py` in the repository directory.
1. Interact with the program.

#### Example to plan individual demands
```bash
# Example to plan factory that produce gold 2 per 30 days.
>>> plan_demand gold 2/30
Result for gold - 2.0 per month:
GATHERERS:
        gold : 0.2 factory
```

#### Example to plan multiple demands
```bash
# Open project or create new project. 
>>> open example_project
Project created
Project loaded
(example_project) >>>
# Plan multiple demands.
(example_project) >>> edit_demand gold 2/15
Demand created
(example_project) >>> edit_demand steel 2/15  
Demand created
(example_project) >>>
# Show the result.
(example_project) >>> get_fact
Result for current demands:
        GATHERERS:
                gold : 0.4 factory
                steel : 0.4 factory
Do you want to open marker for build factory? (y/n)?
# If you type 'y', the program will open marker for build factory.
```

### Use the program with command line
1. Must installed python.
1. Clone this repository.
1. Run `python main.py --help` in the repository directory.
1. Interact with the program with command line.
```bash
C:\Users\Me\Desktop\ROI-helper> python main.py --help
usage: main.py [-h] [-n NAME] [-apd AMOUNT_PER_DAY] [-v VERSION]

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the target
  -apd AMOUNT_PER_DAY, --amount_per_day AMOUNT_PER_DAY
                        Amount of output needed per day
  -v VERSION, --version VERSION
                        Version of the target
```

#### Example to plan individual demands
```bash
PS C:\Users\Me\Desktop\ROI-helper> python main.py -n gold -apd 4/30
Result for gold (4.00 per month):
        gold from GATHERERS : 0.4 factory
PS C:\Users\jiray\Desktop\ROI-helper>
```
> Note : This method can't plan multiple demands.

## For Your Information
this amount of factory is calculated by the maximum amount of sub-factory (e.g. 5 havester per 1 gatherer) and 100% of paid worker.
