#this is going to be the one and only python file for this assignment
import argparse


class DFAStringMatcher:
    def __init__(self, pattern):
        self.pattern = pattern
        self.dfa = self.build_dfa(pattern)

    def build_dfa(self, pattern):
        """Construct DFA transition table for the pattern."""
        m = len(pattern)
        alphabet = set(pattern)  # Number of unique characters in the pattern
        dfa = [{} for _ in range(m)]

        for state in range(m):
            for char in alphabet:
                next_state = 0
                if state < m and char == pattern[state]:
                    next_state = state + 1
                else:
                    # Compute longest prefix which is also a suffix
                    for ns in range(state, 0, -1):
                        if pattern[:ns] == (pattern[state-ns+1:state] + char):
                            next_state = ns
                            break
                dfa[state][char] = next_state

        return dfa

    def search(self, text):
        state = 0
        m = len(self.pattern)
        print("Processing transitions:")
        for i, char in enumerate(text):
            prev_state = state
            state = self.dfa[state].get(char, 0)
            print(f"Char '{char}' at position {i}: {prev_state} -> {state}")
            if state == m:
                print("Pattern found!")
                return True
        print("Pattern not found.")
        return False




def main():
    parser = argparse.ArgumentParser(description="2. String Matching using Finite automata")
    parser.add_argument('input1', type=str, help='First input (either pattern or text)')
    parser.add_argument('input2', type=str, help='Second input (either pattern or text)')
    args = parser.parse_args()

    # Determine pattern and text based on length
    if len(args.input1) < len(args.input2):
        pattern, text = args.input1, args.input2
    else:
        pattern, text = args.input2, args.input1

    print(f"\nPattern: '{pattern}'")
    print(f"Text:    '{text}'\n")

    matcher = DFAStringMatcher(pattern)
    matcher.search(text)


if __name__ == "__main__":
    main()


# Example inputs
# python .\main.py ab xxabxxx
# python .\main.py xxabxxx ab 
'''Expected output:


Processing transitions:
Char 'x' at position 0: 0 -> 0
Char 'x' at position 1: 0 -> 0
Char 'a' at position 2: 0 -> 1
Char 'b' at position 3: 1 -> 2
Pattern found!
'''