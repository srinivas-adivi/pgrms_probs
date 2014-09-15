import lib
from problems10to19 import problem18


def problem67(triangle):
    '''Find the maximum sum travelling from the top.
    >>> from constants import triangle3
    >>> problem18(triangle3)
    7273
    '''
    triangle = triangle.split('\n')
    twodi_list_of_num = [ map(lib.convert_int, words)     
                                for words in map(lambda line: line.split(' '), triangle)]                                                  

    return max(reduce(lib.path_sum, twodi_list_of_num))
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
