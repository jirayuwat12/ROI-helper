import sys
import os
import json
from utils import get_fact_dic

class Controller:
    def __init__(self):
        self.COMMAND_DIC = {
            "help": self.help,
            "open": self.open_project,
            "close": self.close_project,
            "projects" : self.list_projects,
            "demands": self.list_demands,
            "edit_demand": self.edit_demand,
            "delete_demand": self.delete_demand,
            "plan_demand": self.plan_demand,
            "get_fact": self.get_fact,
            "show_demand": self.show_demand,
            "set_version": self.set_version,
            "save": self.save_project,
            "exit": self.exit,
            "" : lambda: None
        }
        self.version = "2130"

        self.current_project = ''
        self.demands = {} # dictionay - key: demand name, value: amount_per_day


    def run(self):
        while True:
            command, args = self.get_command()
            if command in self.COMMAND_DIC:
                try:
                    self.COMMAND_DIC[command](*args)
                except Exception as e:
                    print(e)
            else:
                print("Command not found. Type 'help' for available commands")


    def get_command(self):
        '''get command from user input'''
        prefix = '' if len(self.current_project) == 0 else ("(" + self.current_project + ") ")
        buffer = input(f"{prefix}>>> ")
        command, *args = buffer.split(" ")
        
        return command.lower(), args


    def help(self):
        '''show available commands'''
        print("Available commands:")
        for command in self.COMMAND_DIC.keys():
            if command == '':
                continue
            print('\t',command,'.'*(15-len(command)), self.COMMAND_DIC[command].__doc__)


    def open_project(self, project_name):
        '''open project or create if not exists'''
        self.current_project = project_name

        # load project data from project folder
        project_path = f"projects/{project_name}"
        if not os.path.exists(project_path):
            os.makedirs(project_path)
            
            # create demands file
            f = open(f"{project_path}/demands.json", "w")
            f.write("{}")
            f.close()

            print("Project created")
        
        # load demands
        demands_path = f"{project_path}/demands.json"
        with open(demands_path, "r") as demands_file:
            self.demands = json.load(demands_file)
            print("Project loaded")


    def close_project(self):
        '''close current project'''
        self.current_project = ''
        self.demands = {}
        print("Project closed")


    def list_projects(self):
        '''list all projects'''
        print("Projects:")
        for project in os.listdir("projects"):
            print('\t',project)


    def list_demands(self):
        '''list all demands'''
        if len(self.demands) == 0:
            print("No demands")
            return

        print("Demands:")
        for demand in self.demands.keys():
            print('\t',demand, '-', self.demands[demand], 'per day')


    def edit_demand(self, demand_name, amount_per_day):
        '''edit demand'''
        amount_per_day = float(eval(amount_per_day))

        if demand_name in self.demands:
            self.demands[demand_name] = amount_per_day
            print("Demand edited")
        else:
            self.demands[demand_name] = amount_per_day
            print("Demand created")


    def delete_demand(self, demand_name):
        '''delete demand by name'''
        if demand_name in self.demands:
            del self.demands[demand_name]
            print("Demand deleted")
        else:
            print("Demand not found")


    def plan_demand(self, demand_name, amount_per_day):
        '''plan demand from given amount per day'''
        amount_per_day = float(eval(str(amount_per_day)))
        factory_dic = get_fact_dic({
            "name": demand_name,
            "amount_per_day": amount_per_day,
            "version": self.version
        })

        print(f"Result for {demand_name} - {round(amount_per_day*30,2)} per month:")
        self.show_fact_list(factory_dic)


    def get_fact(self):
        '''get factory dictionary from demands'''
        factory_dic = {}
        for demand in self.demands:
            temp = get_fact_dic({
                "name": demand,
                "amount_per_day": self.demands[demand],
                "version": self.version
            })
            for obj in temp:
                if obj not in factory_dic:
                    factory_dic[obj] = temp[obj]
                else:
                    factory_dic[obj]["factory"] += temp[obj]["factory"]
        if len(factory_dic) == 0:
            print("No demands")
            return
        
        print(f"Result for current demands:")
        self.show_fact_list(factory_dic)


    def show_demand(self):
        '''show demand'''
        if len(self.demands) == 0:
            print("No demands")
            return

        for demand in self.demands:
            print(f"{demand} - {round(self.demands[demand]*30,2)} per month")


    def set_version(self, version):
        '''set version'''
        self.version = version
        print("Version set")


    def save_project(self):
        '''save current project'''
        if len(self.current_project) == 0:
            print("No project opened")
            return

        project_path = f"projects/{self.current_project}"
        demands_path = f"{project_path}/demands.json"
        with open(demands_path, "w") as demands_file:
            json.dump(self.demands, demands_file)
            print("Project saved")


    def exit(self):
        '''exit program'''
        sys.exit(0)


    def show_fact_list(self, factory_dic):
        '''show factory list'''
        factory_list = factory_dic.items()
        factory_list = sorted(factory_list, key=lambda x: x[1]["from"], reverse=True)
        for obj, factory in factory_list:
            print(f"\t{obj} from {factory['from'].upper()} : {round(factory['factory'],1)} factory")
