import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit import QuantumCircuit, transpile

load_dotenv()
service = QiskitRuntimeService(channel="ibm_quantum", token=os.getenv("API_KEY"))
backend = service.least_busy(operational=True, simulator=False, min_num_qubits=2)
print(backend.name)

def qrng(qc, bits):
	random_number = 0
	sampler = Sampler(backend)
	for i in range(bits):
		job = sampler.run([qc], shots=1)
		random_bit = int(next(iter(job.result()[0].data.meas.get_counts())))
		random_number = (random_number << 1) | random_bit
	return random_number

if __name__ == "__main__":
	qc = QuantumCircuit(1)
	qc.h(0)
	qc.measure_all()
	print(qc.draw())

	qc_transpiled = transpile(qc, backend)
	print(qc_transpiled.draw())

	print(f"Random number: {qrng(qc_transpiled, bits=32)}")
