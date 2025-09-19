"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {")": "(", "]": "[", "}": "{"}
        stack = []

        for p in s:
            if stack and stack[-1] == mapper.get(p):
                stack.pop()
            else:
                stack.append(p)

        return not stack


def test_task():
    s = Solution()

    assert s.isValid("([])")
    assert s.isValid("()[]{}")
    assert s.isValid("()")
    assert not s.isValid("(")
    assert not s.isValid("([)]")
    assert not s.isValid("(]")
    assert not s.isValid("(){}}{")


if __name__ == "__main__":
    test_task()
