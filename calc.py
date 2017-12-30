#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@date: 2017-12-09
@author: Daye Yee
@copyright: 2017 Daye Yee <tosony@163.com>
@license: BSD-3-clause
'''

op_set = {
    '(': None,
    ')': None,
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y,
}

op_priority = {
    '+': 10,
    '-': 10,
    '*': 20,
    '/': 20,
}


def parser_exp(exp):
    s = ''
    for c in exp:
        if c in op_set:
            if s:
                yield s
            s = ''
            yield c
        else:
            s += c
    if s:
        yield s


def find_last_op(l):
    for e in reversed(l):
        if e in op_set:
            return e


def force_stack(stack):
    r = stack.pop(-1)
    op = stack.pop(-1)
    l = stack.pop(-1)
    result = op_set[op](l, r)
    print('{} {} {} => {}'.format(op, l, r, result))
    stack.append(result)


def eval_exp(exp):
    stack = []
    for e in exp:
        if e == ')':
            break
        elif e == '(':
            stack.append(eval_exp(exp))
            continue
        if e not in op_set:
            stack.append(float(e))
            continue
        while True:
            last = find_last_op(stack)
            if last is None or op_priority[last] < op_priority[e]:
                break
            force_stack(stack)
        stack.append(e)
    while len(stack) > 1:
        force_stack(stack)
    return stack[0]


def calc(exp):
    '''calculation function'''
    s = parser_exp(exp)
    result = eval_exp(s)
    assert not list(s)
    return result


print(calc('2*3+1'))
print(calc('1+2*3'))
print(calc('(1.1+2.5/10)*3/4+1'))