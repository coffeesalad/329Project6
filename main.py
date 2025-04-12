# this is going to be the one and only python file for this assignment
import argparse


class DFAStringMatcher:
    """
    Init the matcher with a pattern.
    Automatically builds the DFA table.
    """

    def __init__(self, pattern):
        self.pattern = pattern
        self.dfa = self.build_dfa(pattern)

    def build_dfa(self, pattern):
        """
        Construct DFA transition table for the inpute pattern.
        Each state is how many characters of the pattern have been matched
        """
        m = len(pattern)
        alphabet = set(pattern)  # Unique chars
        dfa = [{} for _ in range(m)]    # Creating m states

        # Transitions for each state
        for state in range(m):
            for char in alphabet:
                next_state = 0
                if state < m and char == pattern[state]:
                    # If char matches the expected in the pattern, move to the next state
                    next_state = state + 1
                else:
                    # Else, find the longest prefix of the pattern that is a suffix
                    # of pattern[0:state] + other
                    for ns in range(state, 0, -1):
                        if pattern[:ns] == (pattern[state-ns+1:state] + char):
                            next_state = ns
                            break
                dfa[state][char] = next_state  # set the transition

        return dfa

    def search(self, text):
        """
        Run the DFA on the input text to check if the pattern exists.
        Prints each transition and whether the pattern was found.
        """
        state = 0  # Start at the beginning state
        m = len(self.pattern)

        print("Processing...")
        for i, char in enumerate(text):
            prev_state = state
            # Get the next state; default to 0 if char not found or NULL
            state = self.dfa[state].get(char, 0)
            print(
                f"Character '{char}' at position {i}: {prev_state} -> {state}")
            if state == m:
                # final state reached - Success!!
                print("Pattern found!")
                return True
        # Else pattern not found
        print("Pattern not found.")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="2. String Matching using Finite automata")
    parser.add_argument('input1', type=str,
                        help='First input (either pattern or text)')
    parser.add_argument('input2', type=str,
                        help='Second input (either pattern or text)')
    args = parser.parse_args()

    # Determine pattern and text based on length
    if len(args.input1) < len(args.input2):
        pattern, text = args.input1, args.input2
    else:
        pattern, text = args.input2, args.input1

    print(f"\nPattern: \n{pattern}")
    print(f"Text:\n{text}\n")

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
