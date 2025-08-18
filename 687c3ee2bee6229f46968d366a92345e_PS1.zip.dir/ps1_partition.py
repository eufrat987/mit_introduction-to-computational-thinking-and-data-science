# From codereview.stackexchange.com                    
def partitions(set_):
    # If set is empty do nothing special
    if not set_:
        yield []
        return

    # eg. set of 1,2,3 then we need 3 bits 
    # we can get 000 001 010 011 100 101 110 111
    # this is 8 combinantions
    # So we need only first half of it
    # this is 8/2=4 combinations 
    # why? because eg. 001 is same as 100 :)
    for i in range(2**len(set_)//2):
        # 0 - go to first set, 1 - second
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1

        # Recursive call to itself
        # Do same thing to second set
        # eg. split elements between first and ~second 
        # ~second which be splitted later
        # Do it until second set is empty
        # Merge all parts to list
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def get_partitions(set_):
    for partition in partitions(set_):
        # Replace all sets inside to list 
        # list[set set] -> list[list list]
        yield [list(elt) for elt in partition]

