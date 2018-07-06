from collections import OrderedDict
class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def traverse_in_order(self):
        '''
            Part 2 A goes here
            Return a flat list
        '''
        raise NotImplementedError()
    
    def get_reverse_polish(self):
        '''
            Part 2 B
            Return a flat list
        '''
        raise NotImplementedError()

    def __str__(self):
        ''' This might count for traverseing in order '''
        return '<'+ str(value) + '\t' + str(left) + '\t' + str(right) + '>'

class ExpressionTree(Tree):

    operators = OrderedDict(
        [
            ('-', lambda x, y : x - y),
            ('+', lambda x, y : x + y),
            ('/', lambda x, y : x / y),
            ('*', lambda x, y : x * y)
        ])

    def __init__(self, expression):
        pass

    def evaluate(self):
        ''' 
            Returns an integer answer and prints
            out each step it performs
        '''
        return 10

def main():
    expr = input('Input Expression (hit enter to use default): ')
    if not expr:
        expr = '(3+2*6)/(8-5)'

    e_tree = ExpressionTree(expr)
    print(expr + ' = ' + str(e_tree.evaluate()))

if __name__ == '__main__':
    main()
