
def flatten(elements: list):
    """ Given an array of integers or arrays of integers, flatten them """
    for item in elements:
        try:
            iter(item)
        except TypeError:
            yield item
        else:
            yield from flatten(item)
