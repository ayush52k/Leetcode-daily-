class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know_map = {key: val for key, val in knowledge}
        
        res = []
        in_bracket = False
        current_key = []
        
        for char in s:
            if char == '(':
                in_bracket = True
            elif char == ')':
                in_bracket = False
                key_str = "".join(current_key)
                res.append(know_map.get(key_str, "?"))
                current_key = []
            else:
                if in_bracket:
                    current_key.append(char)
                else:
                    res.append(char)
                    
        return "".join(res)