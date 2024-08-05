/*-
Daily Coding Problem: Problem #986 [Easy]

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
156 = 10011100
*/

public class LongestConsecutiveRunOf1s {
  public static int longestConsecutiveRunOf1s(int n) {
    int longestLength = 0, length = 0;
    while (n > 0) {
      if ((n & 1) == 1) {
        length++;
        longestLength = Math.max(longestLength, length);
      } else {
        length = 0;
      }
      n >>= 1;
    }
    return longestLength;
  }

  public static void main(String[] args) {
    assert longestConsecutiveRunOf1s(156) == 3;
  }
}
