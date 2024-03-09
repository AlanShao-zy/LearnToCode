from typing import List


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_list = list(s)
        p_list = list(p)

        i = 0
        n = len(s_list)
        while i < n:
            if len(p_list) > 0 and (s_list[i] == p_list[0] or p_list[0] == '.'):
                if len(p_list)<2 or p_list[1]!='*':
                    p_list.pop(0)
                i += 1
            else:
                if len(p_list)>1 and p_list[1]=='*':
                    p_list.pop(0)
                    p_list.pop(0)
                else:
                    return False
        
        if len(p_list) == 0 or (len(p_list) == 2 and p_list[-1] == '*'):
            return True
        return False


def test():
    s = "aa"
    p = "a*"
    solution = Solution()
    print(solution.isMatch(s, p))


if __name__ == "__main__":
    test()