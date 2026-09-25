import itertools

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr: str) -> set[str]:
            # Stack holds sets representing terms to be unioned at the current level
            groups = []
            # Current product set accumulates concatenated expressions
            current_product = {""}
            
            i = 0
            n = len(expr)
            
            while i < n:
                char = expr[i]
                
                if char == '{':
                    # Find matching closing brace for this nested group
                    level = 0
                    start = i
                    while i < n:
                        if expr[i] == '{':
                            level += 1
                        elif expr[i] == '}':
                            level -= 1
                            if level == 0:
                                break
                        i += 1
                    
                    # Recursively parse the inner expression inside { ... }
                    inner_set = parse(expr[start + 1:i])
                    # Concatenate with the current running product
                    current_product = {a + b for a in current_product for b in inner_set}
                    
                elif char == ',':
                    # Comma signifies union: finalize current product and start a new term
                    groups.append(current_product)
                    current_product = {""}
                    
                elif char.isalpha():
                    # Single letter concatenation
                    current_product = {a + char for a in current_product}
                    
                i += 1
                
            groups.append(current_product)
            
            # Take the union of all comma-separated groups
            return set().union(*groups)

        # Return sorted unique words
        return sorted(list(parse(expression)))    