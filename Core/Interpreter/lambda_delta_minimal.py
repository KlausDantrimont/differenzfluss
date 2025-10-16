
"""
lambda_delta_minimal.py
Minimal NumPy interpreter for the DFT seed ("osc-1d" example).

Usage (example):
  python lambda_delta_minimal.py

This runs a short demo and writes results to ./out/
"""
from __future__ import annotations
import json
import os
from dataclasses import dataclass
import numpy as np

# --------- Seed loading ---------
DEFAULT_SEED = {
  "dynamics": {
    "examples": {
      "osc-1d": {
        "Σ_type": "1D-Liste reeller Paare (a,v)",
        "Δ_rule": "Δk = (a[k+1]-a[k]) + (a[k-1]-a[k])",
        "Φ_rule": "v' = v + α*Δ - β*a; a' = a + γ*v'",
        "params": {"α": 0.2, "β": 0.01, "γ": 1.0},
        "note": "Harmonischer Oszillator mit Nachbarschaftskopplung"
      }
    }
  }
}

def load_seed(path: str = "dft_seed.json"):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_SEED

# --------- Model ---------
@dataclass
class Osc1DParams:
    alpha: float = 0.2  # α
    beta: float  = 0.01 # β
    gamma: float = 1.0  # γ
    boundary: str = "wrap"  # "wrap" | "reflect"

@dataclass
class Osc1DState:
    a: np.ndarray  # amplitudes
    v: np.ndarray  # "velocity"/difference component

def neighbors_roll(x: np.ndarray, mode: str):
    if mode == "wrap":
        left  = np.roll(x,  1)
        right = np.roll(x, -1)
    elif mode == "reflect":
        # simple reflect via pad-trick for ends
        left = x.copy(); right = x.copy()
        left[1:] = x[:-1]; left[0] = x[1]
        right[:-1] = x[1:]; right[-1] = x[-2]
    else:
        raise ValueError("Unknown boundary mode")
    return left, right

def step_osc1d(state: Osc1DState, p: Osc1DParams) -> Osc1DState:
    # Δk = (a[k+1]-a[k]) + (a[k-1]-a[k])
    left, right = neighbors_roll(state.a, p.boundary)
    delta = (right - state.a) + (left - state.a)

    v_new = state.v + p.alpha * delta - p.beta * state.a
    a_new = state.a + p.gamma * v_new
    return Osc1DState(a=a_new, v=v_new)

def run_osc1d(M=128, steps=2000, seed=42, params: Osc1DParams|None=None, boundary="wrap", save_dir="out"):
    rng = np.random.default_rng(seed)
    if params is None:
        params = Osc1DParams(boundary=boundary)
    else:
        params.boundary = boundary

    a0 = rng.normal(0.0, 0.05, size=M)
    v0 = np.zeros(M, dtype=float)
    state = Osc1DState(a=a0, v=v0)

    energies = []
    means = []
    # simple "energy-like" functional
    for t in range(steps):
        # local gradient proxy
        left, right = neighbors_roll(state.a, params.boundary)
        grad = 0.5*((right - state.a)**2 + (state.a - left)**2)
        E = float(grad.mean() + 0.5*(state.a**2).mean() + 0.5*(state.v**2).mean())
        energies.append(E)
        means.append(float(state.a.mean()))
        state = step_osc1d(state, params)

    os.makedirs(save_dir, exist_ok=True)
    np.save(os.path.join(save_dir, "a_final.npy"), state.a)
    np.save(os.path.join(save_dir, "v_final.npy"), state.v)
    np.save(os.path.join(save_dir, "energies.npy"), np.array(energies))
    np.save(os.path.join(save_dir, "means.npy"), np.array(means))

    # quick stats
    return {
        "M": M,
        "steps": steps,
        "alpha": params.alpha,
        "beta": params.beta,
        "gamma": params.gamma,
        "boundary": params.boundary,
        "E_start": energies[0],
        "E_end": energies[-1],
        "mean_a_end": float(state.a.mean()),
        "std_a_end": float(state.a.std()),
    }

# --------- CLI demo ---------
if __name__ == "__main__":
    seed_obj = load_seed("dft_seed.json")
    # pull defaults if present
    try:
        ex = seed_obj["dynamics"]["examples"]["osc-1d"]
        p = ex.get("params", {})
        alpha = float(p.get("α", 0.2))
        beta  = float(p.get("β", 0.01))
        gamma = float(p.get("γ", 1.0))
    except Exception:
        alpha, beta, gamma = 0.2, 0.01, 1.0

    stats = run_osc1d(M=128, steps=1500, seed=123,
                      params=Osc1DParams(alpha=alpha, beta=beta, gamma=gamma),
                      boundary="wrap", save_dir="out")
    print("Demo finished. Stats:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
