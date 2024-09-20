import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

def qrng(qc, bits):
	random_bits = []
	simulator = Aer.get_backend('qasm_simulator')
	for i in range(bits):
		job = simulator.run(qc, shots=1)
		random_bit = int(list(job.result().get_counts().keys())[0])
		random_bits.append(random_bit)
	random_number = int("".join(map(str, random_bits)), 2)
	return random_bits, random_number

if __name__ == "__main__":
	qc = QuantumCircuit(1)
	qc.h(0)
	qc.measure_all()
	print(qc.draw())

	print(f"Random number: {qrng(qc, bits=32)[1]}")
