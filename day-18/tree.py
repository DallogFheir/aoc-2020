import operator
import re

class Tree:
    def __new__(cls,expr_str,mode):
        tokenized_expr = cls._tokenize_expression(expr_str)
        return cls._convert_tokens_to_tree(tokenized_expr,mode)

    @classmethod
    def _tokenize_expression(cls,expr):
        tokenized_expr_str = [
            token
            for token in re.split(
            r" |(\d+)|(\+|\*)|(\(|\))",
            expr
            )
            if token
        ]

        tokenized_expr = [
            int(token)
            if re.match(r"\d+",token)
            else token
            for token in tokenized_expr_str
        ]

        return tokenized_expr

    @classmethod
    def _divide_one_level_into_subexpressions(cls,expr_lst):
        subexprs = []
        brackets = []
        open_brackets = 0

        for token in expr_lst:
            if token=="(":
                if open_brackets!=0:
                    brackets.append("(")

                open_brackets += 1
            elif token==")":
                open_brackets -= 1

                if open_brackets==0:
                    subexprs.append(brackets)
                    brackets = []
                else:
                    brackets.append(")")
            else:
                if open_brackets==0:
                    subexprs.append(token)
                else:
                    brackets.append(token)

        return subexprs

    @classmethod
    def _divide_into_subexpressions(cls,expr_lst):
        if "(" in expr_lst or ")" in expr_lst:
            new_lst = cls._divide_one_level_into_subexpressions(expr_lst)

            for i, item in enumerate(new_lst):
                if isinstance(item,list):
                    new_lst[i] = cls._divide_into_subexpressions(item)

            return new_lst
        else:
            return expr_lst

    @classmethod
    def _convert_tokens_to_tree(cls,tokenized_expr,mode):
        if mode=="standard":
            output = cls._convert_tokens_left_to_right(tokenized_expr)
        elif mode=="advanced":
            output = cls._convert_tokens_advanced(tokenized_expr)
        else:
            raise ValueError("Unknown mode.")

        return output

    @classmethod
    def _convert_tokens_left_to_right(cls,tokenized_expr):
        expr_lst = cls._divide_into_subexpressions(tokenized_expr)

        while len(expr_lst)!=1:
            l, op, r = expr_lst[:3]

            l = cls._convert_tokens_left_to_right(l) if isinstance(l,list) else Const(l) if isinstance(l,int) else l 
            r = cls._convert_tokens_left_to_right(r) if isinstance(r,list) else Const(r) if isinstance(r,int) else r 

            if op=="+":
                res = Addition(l,r)
            elif op=="*":
                res = Multiplication(l,r)
            else:
                raise ValueError("Unknown operator.")

            del expr_lst[:3]
            expr_lst.insert(0,res)

        return expr_lst[0]

    @classmethod
    def _convert_tokens_advanced(cls,tokenized_expr):
        expr_lst = cls._divide_into_subexpressions(tokenized_expr)

        while "+" in expr_lst:
            plus_index = expr_lst.index("+")

            l, _, r = expr_lst[plus_index-1:plus_index+2]

            l = cls._convert_tokens_advanced(l) if isinstance(l,list) else Const(l) if isinstance(l,int) else l 
            r = cls._convert_tokens_advanced(r) if isinstance(r,list) else Const(r) if isinstance(r,int) else r 

            res = Addition(l,r)

            del expr_lst[plus_index-1:plus_index+2]
            expr_lst.insert(plus_index-1,res)
        while "*" in expr_lst:
            mul_index = expr_lst.index("*")

            l, _, r = expr_lst[mul_index-1:mul_index+2]

            l = cls._convert_tokens_advanced(l) if isinstance(l,list) else Const(l) if isinstance(l,int) else l 
            r = cls._convert_tokens_advanced(r) if isinstance(r,list) else Const(r) if isinstance(r,int) else r 

            res = Multiplication(l,r)

            del expr_lst[mul_index-1:mul_index+2]
            expr_lst.insert(mul_index-1,res)

        return expr_lst[0]

# NODES
class Node:
    def __add__(self,other):
        return self._add(other)

    def __radd__(self,other):
        return self._add(other)

    def _add(self,other):
        is_tree = isinstance(other,Tree)

        if is_tree or isinstance(other,int):
            other_value = other.eval() if is_tree else other

            return self.eval() + other_value
        else:
            return NotImplemented

# SUBCLASSES
# binary operations
class BinaryOperation(Node):
    def __init__(self,l,r):
        self.l = l
        self.r = r

    def __repr__(self):
        return f"({str(self.l)} {self.sign} {str(self.r)})"

    def eval(self):
        return self.operation(self.l.eval(), self.r.eval())

class Addition(BinaryOperation):
    sign = "+"
    operation = operator.add

class Multiplication(BinaryOperation):
    sign = "*"
    operation = operator.mul

# constants
class Const(Node):
    def __init__(self,value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def eval(self):
        return self.value
