# Girl_Hackathon_Ideation_Round
The problem statement states that given a circuit design with four inputs and the location of the stuck-at fault, write an algorithm to identify the input vector required to identify the fault at a given node in a given circuit, assuming that the circuit contains a single fault.
We use the Forward Tracing Path Sensitization algorithm to give the required output. This technique is used to identify the input vectors required to detect a stuck-at-fault in a digital circuit. It works by propagating sensitization from the fault node to the primary inputs of the circuit, generating test vectors along the sensitized paths. By propagating sensitization from the fault node to the key inputs of the circuit, the Forward Tracing Path Sensitization method quickly finds the input vectors required to detect a stuck-at fault. It ensures that each sensitized node is only visited once, avoiding unnecessary calculations. The test vectors generated can be utilized to confirm the presence of the stuck-at fault in the circuit.

Inputs:
Circuit: A representation of the circuit with the stuck-at fault(s)
Fault Node: The node where the fault is located
Fault Type: SA0 (stuck-at-0) or SA1 (stuck-at-1)
Outputs:

Test Vectors: The input vectors required to detect the fault
