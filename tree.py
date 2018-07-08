from collections import OrderedDict
import re

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
        return '<'+ str(self.value) + '\t' + str(self.left) + '\t' + str(self.right) + '>'

class ExpressionTree(Tree):

    operators = OrderedDict(
        [
            ('-', lambda x, y : x - y),
            ('+', lambda x, y : x + y),
            ('/', lambda x, y : x / y),
            ('*', lambda x, y : x * y)
        ])

    def __init__(self, expression):
        print(expression)
        if not isinstance(expression, list):
            expression = self._format_phrase(expression)
        if  '(' in expression:
            expression = self._part_phrase_list(expression)
        if len(expression) == 1:
            self.value = expression[0]
            self.left = None
            self.right = None
        else:
            self.value, left_expr, right_expr = self._parse_expression(expression)
            if isinstance(left_expr[0], list):
                left_expr = left_expr[0]

            if isinstance(right_expr[0], list):
                right_expr = right_expr[0]
            self.left = ExpressionTree(left_expr)
            self.right = ExpressionTree(right_expr)

    def evaluate(self):
        ''' 
            Returns an integer answer and prints
            out each step it performs
        '''
        return 10

    def _parse_expression(self, expression):
        for operator in self.operators.keys():
            try:
                op_index = expression.index(operator)
                return expression[op_index], expression[0:op_index], expression[op_index + 1:]
            except ValueError:
                continue

    
    def _get_paren_regions(self, phrase):
        regions = []
        paren_counter = 0
        open_paren_index = 0
        curr_index = 0

        for e in phrase:
            if e == '(':
                if paren_counter == 0:
                    open_paren_index = curr_index
                paren_counter += 1
            elif e == ')':
                paren_counter -= 1
                if paren_counter == 0:
                    regions.append((open_paren_index, curr_index))
            curr_index += 1
        return regions

    def _part_phrase_list(self, phrase):
        regions = self._get_paren_regions(phrase)
        partitioned_list = []

        for e in regions:
            partition = phrase[e[0] + 1: e[1]]
            partitioned_list.append(partition)
        # Add any ops not in parens back into list
        for index in range(len(regions)-1):
            curr_region_end = regions[index][1]
            next_region_start = regions[index + 1][0]
            if next_region_start - curr_region_end > 1:
                insert_start = index + 1
                sub_phrase = phrase[curr_region_end+1:next_region_start]
                for index in range(len(sub_phrase)):
                    partitioned_list.insert(insert_start + index, sub_phrase[index])

        partitioned_list.append(phrase[regions[-1][1]+1:])

        # clean up the list
        if partitioned_list[-1] == []:
            del partitioned_list[-1]
        return partitioned_list

    def _format_phrase(self, phrase):
        regex = r'(\(|\)|\+|\-|\*|\/)'
        phrase = re.split(regex, phrase)
        phrase = list(filter(lambda e : e != '', phrase))
        return self._part_phrase_list(phrase)
def main():
    expr = input('Input Expression (hit enter to use default): ')
    if not expr:
        expr = '(3+2*6)/(8-5)'

    e_tree = ExpressionTree(expr)
    print(expr + ' = ' + str(e_tree))

if __name__ == '__main__':
    main()
