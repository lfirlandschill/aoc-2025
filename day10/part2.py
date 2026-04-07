from pathlib import Path
import re
import sympy as sp
from itertools import product
import time

path = Path(__file__).parent / "input.txt"
with open(path, 'r') as f:
    lines = f.readlines()

res = 0
for l, line in enumerate(lines):
    start = time.perf_counter()
    target = [int(x) for x in line.split('{')[-1].replace('}','').split(',')]
    buttons = [
    [int(x.strip()) for x in part.split(',')]
    for part in re.findall(r'\((.*?)\)', line)
    ]
    n_var = len(buttons)
    n_eq = len(target)
    A = sp.zeros(n_eq, n_var)
    for n in range(n_var):
        for toggle in buttons[n]:
            A[toggle, n] = 1
    b = sp.Matrix(target)
    vars = sp.symbols(f'x0:{n_var}')
    sol = sp.linsolve((A, b), vars)
    sol_tuple = next(iter(sol))
    _, pivots = A.rref()
    free_vars = [vars[j] for j in range(len(vars)) if j not in pivots]
    fns = [sp.lambdify(free_vars, expr) for expr in sol_tuple]

    ranges = []
    for free_var in free_vars:
        idx = int(str(free_var)[1:])
        max_presses = float('inf')
        for counter in buttons[idx]:
            max_presses = min(max_presses, target[counter])
        ranges.append(range(0, max_presses + 1))


    fewest_presses = None
    for choice in product(*ranges):
        sol = [fn(*choice) for fn in fns]
        if all(p >= 0 and abs(p - round(p)) < 1e-9 for p in sol):
            n_presses = sum(round(p) for p in sol)
            if fewest_presses is None or n_presses < fewest_presses:
                fewest_presses = n_presses

    end = time.perf_counter()
    print(f"Line {l}: {fewest_presses} ({end - start:.6f} s)")
    res += fewest_presses

print(f"Total presses: {res}")