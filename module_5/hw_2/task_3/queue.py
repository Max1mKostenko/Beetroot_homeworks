def get_from_stack(queue_list):
    """
    First variant
    """
    if "e" in queue_list:
        print(queue_list)
        print(queue_list.pop(queue_list.index("e")))
    else:
        print(queue_list)
        raise ValueError("Element 'e' not in a stack")
    print(queue_list)

    """
    Second variant
    """
    # for index, item in enumerate(queue_list):
    #     if item == "e":
    #         print(queue_list)
    #         print(queue_list.pop(index))
    #         break
    #     elif "e" not in queue_list:
    #         print(queue_list)
    #         raise ValueError("Element 'e' not in a stack")
    # print(queue_list)


get_from_stack([1, 2, 3, 4, "e", "b", "c", "s"])
