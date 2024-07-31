import java.util.*;

/*-
Daily Coding Problem #984 [Hard]

Given a string of parentheses, find the balanced string that can be produced from it using the minimum
number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

---

input = ""
output = ""

---

input = "("
output = "()" OR ""

---

input = ")"
output = "()" OR ""

---

input = "(()"
output = "(())" OR "()"

---

input = "))()("
output = "()()()()" OR "()"

input = "))()("
stack = []
output = "()"
output = "()()"
output = "()()("
output = "()()()"
output = "()()()("
output = "()()()()"

---

input = ")()))((()))"
output = "()()()()((()))" OR "()((()))"

---

input = ")()))((()())"
output = "()()()()((()()))"

stack = []
output = "()"

stack = [(]
output = "()"

stack = []
output = "()()"

stack = []
output = "()()()"

stack = []
output = "()()()()"

stack = [(]
output = "()()()()("

stack = [((]
output = "()()()()(("

stack = [(((]
output = "()()()()((("

stack = [((]
output = "()()()()((()"

stack = [((]
output = "()()()()((()()"

stack = [(]
output = "()()()()((()())"

stack = []
output = "()()()()((()()))"

if found open parenthesis add ( to output and to the stack
if found close parenthesis with non empty stack, add ) to output
if found close parenthesis with empty stack, add () to output

after everything, add a close parenthesis for every open parenthesis in the stack
*/

public class BalancedStringWithMinimumInsertionsAndDeletions {
  public static String balanceParenthesis(String str) {
    Deque<Character> stack = new LinkedList<>();
    StringBuilder output = new StringBuilder();
    for (int i = 0; i < str.length(); i++) {
      if (str.charAt(i) == '(') {
        output.append("(");
        stack.push('(');
      } else {
        if (stack.isEmpty()) {
          output.append("()");
        } else {
          output.append(")");
          stack.pop();
        }
      }
    }
    while (!stack.isEmpty()) {
      output.append(")");
      stack.pop();
    }
    return output.toString();
  }

  public static void main(String[] args) {
    assert balanceParenthesis("").equals("");
    assert balanceParenthesis("(").equals("()");
    assert balanceParenthesis(")").equals("()");
    assert balanceParenthesis("(()").equals("(())");
    assert balanceParenthesis("))()(").equals("()()()()");
    assert balanceParenthesis(")()))((()))").equals("()()()()((()))");
    assert balanceParenthesis(")()))((()())").equals("()()()()((()()))");
  }
}
