from stack import Stack
from string import ascii_letters, digits
import pytest


def infix2Postfix(infix_expression: str) -> str:
    """
    Converts an infix expression (A*B+C*D) to a Postfix expression (AB*CD*+).

    Pseudocode:
    1. Create an empty stack of operators. Create an empty list for output.
    2. Convert the input infix string to a list of "tokens".
    3. Scan the list of tokens from left to right.
        a) If token is an operand, append it to the output list.
        b) If token is a left parenthesis, push onto operators stack.
        c) If token is a right parenthesis, pop operators stack until the
        corresponding left parenthesis is removed. Append each operator to the
        output list.
        d) If token is an operator (*,/,+,-), push onto opstack. However, first
        remove any operators already on the opstack that have higher or equal
        precedence and append to the output list.
    4. When the input expression has been completely processed, check the
    operators stack. Any operators still on the stack can be removed and
    appended to the end of the output list."""

    precedence = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opstack = Stack()
    postfixList = []
    tokens = infix_expression.replace("(", " ( ").replace(")", " ) ").strip().split()

    for t in tokens:
        if (t in ascii_letters + digits) or (
            len(t) > 1 and all(True if d in digits else False for d in list(str(t)))
        ):
            postfixList.append(t)
        elif t == "(":
            opstack.push(t)
        elif t == ")":
            while (top := opstack.pop()) != "(":
                postfixList.append(top)
        else:
            while (not opstack.isEmpty()) and (
                precedence[opstack.peek()] >= precedence[t]
            ):
                postfixList.append(opstack.pop())
            opstack.push(t)

    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)


def postfixEval(postfix_expression: str) -> float:
    """Evaluates a Postfix expression (A B * C D * +).

    Psuedo Code:
    1. Create an empty stack for operations.

    2. Convert the input infix string to a list of "tokens".

    3. Scan the list of tokens from left to right.
        a) If the token is an operand, append it to the end of the output list.
        b) If the token is a left parenthesis, push it on the operators stack.
        c) If the token is a right parenthesis, pop the operators stack until
        the corresponding left parenthesis is removed. Append each operator to
        the end of the output list.
        d) If the token is an operator, *, /, +, or -, push it on the opstack.
        However, first remove any operators already on the opstack that have
        higher or equal precedence and append them to the output list.

    4. When the input expression has been completely processed, check the
    operators stack. Any operators still on the stack can be removed and
    appended to the end of the output list."""

    def doMath(op, op1, op2):
        if op in ("*", "/", "+", "-", "**"):
            return eval(f"{op1}{op}{op2}")

    operands = Stack()
    tokens = postfix_expression.split()

    for t in tokens:
        if t == "==":
            break
        try:  # TODO handle this better
            tt = float(t)
            operands.push(tt)
        except ValueError:
            op2, op1 = operands.pop(), operands.pop()
            operands.push(doMath(t, op1, op2))

    return operands.pop()


@pytest.mark.parametrize(
    "test, result",
    [
        ("( A + B ) * ( C + D )", "A B + C D + *"),
        ("( A + B ) * C", "A B + C *"),
        ("A + B * C", "A B C * +"),
        ("A * B + C * D", "A B * C D * +"),
        ("( A + B ) * C - ( D - E ) * ( F + G )", "A B + C * D E - F G + * -"),
        ("10 + 3 * 5 / (16 - 4)", "10 3 5 * 16 4 - / +"),
    ],
)
def test_infix2Postfix(test, result):
    assert infix2Postfix(test) == result


@pytest.mark.parametrize(
    "test, result",
    [("7 8 + 3 2 + /", 3.0), ("17 10 + 3 * 9 / =="), 9.0],
)
def test_postfixEval(test, result):
    assert postfixEval(test) == result