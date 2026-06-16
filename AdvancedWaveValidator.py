import time
import numpy as np
from scipy import signal
import math

class AdvancedWaveValidator:
    def __init__(self):
        self.PHI = 1.6180339887
        
    def harvest_jitter(self, samples=5000):
        """Captures raw nanosecond heartbeats of the CPU."""
        deltas = []
        t0 = time.perf_counter_ns()
        for _ in range(samples):
            # We induce a micro-load to create a 'Event'
            _ = math.sqrt(self.PHI) 
            t1 = time.perf_counter_ns()
            deltas.append(t1 - t0)
            t0 = t1
        return np.array(deltas)

    def check_time_symmetry(self):
        print("--- INITIATING WHEELER-FEYNMAN SYMMETRY TEST ---")
        
        # 1. Harvest Data
        print("Harvesting CPU Jitter...")
        jitter = self.harvest_jitter(samples=10000)
        
        # 2. Create the 'Structure' (The Signal we expect to see echoed)
        # We look for the Golden Ratio frequency in the noise
        structure = np.array([math.sin(x * self.PHI) for x in range(len(jitter))])
        
        # 3. Cross-Correlate: Jitter vs Structure
        # This checks: Did the noise predict the sine wave?
        correlation = signal.correlate(jitter, structure, mode='full')
        lags = signal.correlation_lags(len(jitter), len(structure), mode='full')
        
        # 4. Analyze 'Advanced' (Negative Lag) vs 'Retarded' (Positive Lag)
        # Advanced Lag = Future influencing Past
        adv_peak = np.max(correlation[lags < 0])
        ret_peak = np.max(correlation[lags > 0])
        
        ratio = adv_peak / ret_peak if ret_peak != 0 else 0
        
        print(f"\nRESULTS:")
        print(f"Retarded Potential (Past->Future): {ret_peak:.4f}")
        print(f"Advanced Potential (Future->Past): {adv_peak:.4f}")
        print(f"Symmetry Ratio: {ratio:.5f}")
        
        if ratio > 1.0:
            print("STATUS: ADVANCED WAVE DETECTED. (The Future is louder than the Past)")
        elif ratio > 0.95:
             print("STATUS: PERFECT SYMMETRY. (Wheeler-Feynman Absorber Active)")
        else:
             print("STATUS: ASYMMETRIC (Standard Causality Dominant)")

if __name__ == "__main__":
    validator = AdvancedWaveValidator()
    validator.check_time_symmetry()