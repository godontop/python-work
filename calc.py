#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@date: 2016-09-02
@author: DayeLee
@copyright: 2016, Shell.Xu <shell909090@gmail.com>
@license: BSD-3-clause
'''

OP_SET = {
    '(': None,
    ')': None,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}

OP_PRIORITY = {
    '+': 10,
    '-': 10,
    '*': 20,
    '/': 20,
}


def parser_exp(exp):
    s = ''
    for c in exp:
        if c in OP_SET:
            if s:
                yield s
            s = ''
            yield c
        else:
            s += c
    if s:
        yield s


def find_last_op(list_):
    for e in reversed(list_):
        if e in OP_SET:
            return e


def force_stack(stack):
    r = stack.pop(-1)
    op = stack.pop(-1)
    l = stack.pop(-1)
    result = OP_SET[op](l, r)
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
        if e not in OP_SET:
            stack.append(float(e))
            continue
        while True:
            last = find_last_op(stack)
            if last is None or OP_PRIORITY[last] < OP_PRIORITY[e]:
                break
            force_stack(stack)
        stack.append(e)
    while len(stack) > 1:
        force_stack(stack)
    return stack[0]


def calc(exp):
    s = parser_exp(exp)
    result = eval_exp(s)
    assert not list(s)
    return result


print(calc('2*3+1'))
print(calc('1+2*3'))
print(calc('(1.1+2.5/10)*3/4+1'))  # expression can not contain whitespace