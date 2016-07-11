def main():
    dict_ingrediants = {'taco':5, 'meat': 4, 'beef':3, 'rice':1}
    print(dict_ingrediants['meat'])
    max_value = max(dict_ingrediants['meat'], dict_ingrediants['beef'], dict_ingrediants['rice'])
    min_value = min(dict_ingrediants['meat'], dict_ingrediants['beef'], dict_ingrediants['rice'])
    remaining_value = max_value - min_value
    item1 = [k for k, v in dict_ingrediants.iteritems() if v == max_value]
    item2 = [k for k, v in dict_ingrediants.iteritems() if v == min_value]
    total_items = [k for k, v in dict_ingrediants.iteritems()]
    print(total_items)
    list_items = [item1.pop(), item2.pop(),'taco']
    print(list_items)
    item3 = list(set(total_items)-set(list_items)).pop()
    print(item3)

    value_item3 = dict_ingrediants[str(item3)]
    total_items_made = min_value+min(remaining_value, value_item3)
    print("total Items that can be made"+ str(min(total_items_made,dict_ingrediants['taco'])))

if __name__ == '__main__':
    main()