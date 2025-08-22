class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        multi_line = False
        for line in source:
            if not multi_line: buffer = []
            i = 0
            while i < len(line):
                if multi_line:
                    # Parsing through a Multi line comment
                    if line[i] == "*" and\
                        i+1 < len(line) and\
                        line[i+1] == "/":
                        # End of multi line comment encountered
                        multi_line = False
                        i += 2
                        continue
                    else:
                        # Content inside
                        # multi-line comment.
                        # Ignoring content
                        i += 1
                        continue
                else:
                    # Parsing through normal line
                    if line[i] == "/" and\
                    i+1 < len(line) and\
                    line[i+1] == "/":
                    # Single line comment encountered
                    # Ignoring the rest of the current line
                        break
                    elif line[i] == "/" and\
                    i+1 < len(line) and\
                    line[i+1] == "*":
                    # Encountered the start of a
                    # Multi Line comment
                        multi_line = True
                        i += 2
                        continue
                    else:
                    # Valid code. Hence putting it in buffer
                        buffer.append(line[i])
                i += 1
            
            # Amidst a multi-line comment
            # the line is still continuing
            if multi_line: continue

            # End of a valid line of code
            buffer = ''.join(buffer)    
            if buffer:
                answer.append(buffer)
        return answer