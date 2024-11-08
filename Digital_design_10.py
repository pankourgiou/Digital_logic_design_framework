class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()

class ANDGate:
    def evaluate(self, input1, input2):
        """Evaluate AND gate: Output is 1 if both inputs are 1."""
        return input1 and input2

class ORGate:
    def evaluate(self, input1, input2):
        """Evaluate OR gate: Output is 1 if at least one input is 1."""
        return input1 or input2

class NOTGate:
    def evaluate(self, input1):
        """Evaluate NOT gate: Output is the inverse of the input."""
        return not input1

class NANDGate:
    def evaluate(self, input1, input2):
        """Evaluate NAND gate: Output is the inverse of AND gate."""
        return not (input1 and input2)

class NORGate:
    def evaluate(self, input1, input2):
        """Evaluate NOR gate: Output is the inverse of OR gate."""
        return not (input1 or input2)

class XORGate:
    def evaluate(self, input1, input2):
        """Evaluate XOR gate: Output is 1 if inputs are different."""
        return input1 != input2

class Circuit:
    def __init__(self):
        self.gates = []
        self.inputs = {}
        self.outputs = {}

    def add_gate(self, gate, gate_name, inputs):
        """Add a gate to the circuit."""
        self.gates.append({
            'gate': gate,
            'name': gate_name,
            'inputs': inputs
        })
        self.outputs[gate_name] = None

    def set_input(self, input_name, value):
        """Set input values to the circuit."""
        self.inputs[input_name] = value

    def evaluate(self):
        """Evaluate the circuit based on current inputs."""
        for gate in self.gates:
            # Retrieve inputs for the gate
            gate_name = gate['name']
            inputs = gate['inputs']
            
            # Extract values for the gate inputs
            if isinstance(inputs, tuple):
                input_values = [self.inputs[input] for input in inputs]
            else:
                input_values = [self.inputs[inputs]]

            # Evaluate the gate and store the result in outputs
            self.outputs[gate_name] = gate['gate'].evaluate(*input_values)

    def get_output(self, gate_name):
        """Return the output of a gate by its name."""
        return self.outputs.get(gate_name)

    def display_truth_table(self):
        """Display truth table for the circuit."""
        import itertools

        # Determine all possible input combinations
        input_names = list(self.inputs.keys())
        all_combinations = list(itertools.product([0, 1], repeat=len(input_names)))

        print(f"Truth Table for Circuit: {', '.join(input_names)}")
        print("-" * (len(input_names) * 4 + 10))

        # Print the truth table for each combination
        for combination in all_combinations:
            # Set inputs for the current combination
            for i, input_name in enumerate(input_names):
                self.set_input(input_name, combination[i])

            # Evaluate the circuit for current inputs
            self.evaluate()

            # Print the inputs and corresponding output of each gate
            outputs = [str(self.get_output(gate['name'])) for gate in self.gates]
            inputs_str = " | ".join(map(str, combination))
            print(f"{inputs_str} | {' | '.join(outputs)}")

# Example of using the framework to design a circuit
def main():
    # Create the circuit
    circuit = Circuit()

    # Add gates to the circuit (using the gate classes)
    circuit.add_gate(ANDGate(), 'AND1', ('A', 'B'))
    circuit.add_gate(ORGate(), 'OR1', ('A', 'B'))
    circuit.add_gate(NOTGate(), 'NOT1', 'A')
    circuit.add_gate(NANDGate(), 'NAND1', ('A', 'B'))
    circuit.add_gate(XORGate(), 'XOR1', ('A', 'B'))

    # Set inputs for the circuit (e.g., A and B)
    circuit.set_input('A', 0)
    circuit.set_input('B', 1)

    # Evaluate the circuit
    circuit.evaluate()

    # Get outputs for specific gates
    print("Output of AND1:", circuit.get_output('AND1'))
    print("Output of OR1:", circuit.get_output('OR1'))
    print("Output of NOT1:", circuit.get_output('NOT1'))
    print("Output of NAND1:", circuit.get_output('NAND1'))
    print("Output of XOR1:", circuit.get_output('XOR1'))

    # Display the truth table for the circuit
    circuit.display_truth_table()

if __name__ == "__main__":
    main()
