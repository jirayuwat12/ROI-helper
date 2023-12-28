from recipe import get_recipe

def get_fact_dic(args):
    queue = []

    recipe = get_recipe(version = args['version'])

    if args['name'] not in recipe:
        print(f"Target object not found ({args['name']})")
        return

    factory_dic = {}

    # object_name, multiplier
    exec(f"args['amount_per_day'] = float({args['amount_per_day']})")
    queue.append((args['name'], args['amount_per_day'] / recipe[args['name']]["output_per_day"]))
    while len(queue) > 0:
        obj, multiplier = queue.pop(0)

        if obj not in factory_dic:
            factory_dic[obj] = {
                "from": recipe[obj]["from"],
                "factory": 0
            }
        factory_dic[obj]["factory"] += multiplier

        if "input_per_day" not in recipe[obj]:
            continue
        for need in recipe[obj]["input_per_day"]:
            queue.append((need, multiplier * (recipe[obj]["input_per_day"][need] / recipe[need]["output_per_day"])))

    return factory_dic
