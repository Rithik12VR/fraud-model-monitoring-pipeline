import math
from typing import Iterable, List, Tuple


def _safe_pct(count: int, total: int, epsilon: float = 1e-6) -> float:
    if total == 0:
        return epsilon
    return max(count / total, epsilon)


def calculate_psi(
    baseline_counts: Iterable[int],
    current_counts: Iterable[int],
    epsilon: float = 1e-6,
) -> float:
    """
    Calculate Population Stability Index using bucket counts.

    PSI = sum((current_pct - baseline_pct) * ln(current_pct / baseline_pct))
    """
    baseline = list(baseline_counts)
    current = list(current_counts)

    if len(baseline) != len(current):
        raise ValueError("baseline_counts and current_counts must have same length")

    baseline_total = sum(baseline)
    current_total = sum(current)

    psi = 0.0
    for base_count, curr_count in zip(baseline, current):
        base_pct = _safe_pct(base_count, baseline_total, epsilon)
        curr_pct = _safe_pct(curr_count, current_total, epsilon)
        psi += (curr_pct - base_pct) * math.log(curr_pct / base_pct)

    return round(psi, 6)


def bucket_score(score: float, bins: List[float]) -> str:
    for lower, upper in zip(bins[:-1], bins[1:]):
        if lower <= score < upper:
            return f"{lower:.1f}-{upper:.1f}"
    if score == bins[-1]:
        return f"{bins[-2]:.1f}-{bins[-1]:.1f}"
    return "out_of_range"
