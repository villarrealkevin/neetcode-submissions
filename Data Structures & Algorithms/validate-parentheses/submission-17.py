class Solution:
    def isValid(self, s: str) -> bool:
        clave = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        op = []

        if len(s) % 2 != 0:
            return False
        elif s[0] in clave.keys():
            return False

        for i in range(len(s)):
            if s[i] in clave.values():
                op.append(s[i])
            else:
                if len(op) == 0:
                    return False
                else:
                    last = op.pop()
                    if clave[s[i]] != last:
                        return False
        
        if len(op) == 0:
            return True
        else:
            return False