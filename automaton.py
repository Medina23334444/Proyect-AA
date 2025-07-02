class ProbabilisticDeterministicAutomaton:
    def __init__(self):
        # States
        self.states = {"S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11"}

        # Alphabet
        self.events = {
            'login', 'failed_login', 'read_file', 'write_file', 'upload_script',
            'execute_binary', 'access_admin', 'create_user', 'change_config',
            'open_port', 'download_data', 'logout'
        }

        # Initial state
        self.initial_state = 'S0'

        # Final/accepting states
        self.final_states = {'S6', 'S7', 'S8', 'S9', 'S10'}

        # Transition table with probabilities
        self.transitions = {
            ('S0', 'login'): ('S1', 0.95),
            ('S0', 'failed_login'): ('S5', 0.85),
            ('S5', 'failed_login'): ('S5', 0.65),
            ('S1', 'read_file'): ('S2', 0.80),
            ('S1', 'write_file'): ('S3', 0.70),
            ('S1', 'upload_script'): ('S4', 0.30),
            ('S2', 'upload_script'): ('S4', 0.30),
            ('S3', 'upload_script'): ('S4', 0.30),
            ('S1', 'execute_binary'): ('S6', 0.20),
            ('S4', 'execute_binary'): ('S6', 0.20),
            ('S1', 'access_admin'): ('S7', 0.15),
            ('S5', 'access_admin'): ('S7', 0.10),
            ('S6', 'access_admin'): ('S7', 0.15),
            ('S7', 'create_user'): ('S8', 0.10),
            ('S8', 'change_config'): ('S9', 0.05),
            ('S9', 'open_port'): ('S10', 0.03),
            ('S1', 'download_data'): ('S11', 0.40),
            ('S1', 'logout'): ('S0', 0.90),
        }

        # Current state
        self.current_state = self.initial_state
        # Probability of reaching current state via processed sequence
        self.current_probability = 1.0

    def reset(self):
        """Reset automaton to the initial state."""
        self.current_state = self.initial_state
        self.current_probability = 1.0

    def process_event(self, event):
        """Process a single event and update state and probability."""
        if (self.current_state, event) not in self.transitions:
            raise ValueError(f"No transition defined for state {self.current_state} with event {event}")
        next_state, probability = self.transitions[(self.current_state, event)]
        self.current_state = next_state
        self.current_probability *= probability
        return self.current_state, probability

    def process_sequence(self, events):
        """Process a sequence of events."""
        self.reset()
        for event in events:
            self.process_event(event)
        return self.current_state, self.current_probability

    def is_accepting(self):
        """Check if current state is an accepting state."""
        return self.current_state in self.final_states


if __name__ == "__main__":
    # Example usage: process a sample sequence
    automaton = ProbabilisticDeterministicAutomaton()
    sequence = ['login', 'read_file', 'upload_script', 'execute_binary']
    state, prob = automaton.process_sequence(sequence)
    print(f"Final state: {state}")
    print(f"Probability: {prob:.4f}")
    print(f"Accepting: {automaton.is_accepting()}")
