import random
import time
import matplotlib.pyplot as plt


# QuickSort Implementations
def quicksort_deterministic(arr):
    """QuickSort with deterministic pivot (last element)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort_deterministic(left) + [pivot] + quicksort_deterministic(right)


def quicksort_randomized(arr):
    """QuickSort with randomized pivot."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for i, x in enumerate(arr) if i != pivot_index and x <= pivot]
    right = [x for i, x in enumerate(arr) if i != pivot_index and x > pivot]
    return quicksort_randomized(left) + [pivot] + quicksort_randomized(right)


# Helpers
def measure_time(sort_func, arr, repeats=5):
    """Measure average execution time of a sort function."""
    total = 0
    for _ in range(repeats):
        data_copy = arr[:]
        start = time.perf_counter()
        sort_func(data_copy)
        end = time.perf_counter()
        total += (end - start)
    return total / repeats


def run_experiments():
    # sizes for scenarios
    big_sizes = [10000, 50000, 100000, 500000]
    small_sizes = [900]  # to avoid RecursionError for Sorted/Reversed

    scenarios = {
        "Random": (big_sizes, lambda n: [random.randint(0, 1000000) for _ in range(n)]),
        "Sorted": (small_sizes, lambda n: list(range(n))),
        "Reversed": (small_sizes, lambda n: list(range(n, 0, -1))),
    }

    for scenario, (sizes, generator) in scenarios.items():
        print(f"\n=== Scenario: {scenario} Data ===")
        results = {"Randomized": [], "Deterministic": []}

        for size in sizes:
            arr = generator(size)
            t_rand = measure_time(quicksort_randomized, arr)
            t_det = measure_time(quicksort_deterministic, arr)

            results["Randomized"].append(t_rand)
            results["Deterministic"].append(t_det)

            print(f"Array size: {size}")
            print(f"   Randomized QuickSort:   {t_rand:.4f} s")
            print(f"   Deterministic QuickSort:{t_det:.4f} s")

        # Plot results for this scenario
        plt.plot(sizes, results["Randomized"], marker="o", label="Randomized QuickSort")
        plt.plot(sizes, results["Deterministic"], marker="o", label="Deterministic QuickSort")
        plt.xlabel("Array size")
        plt.ylabel("Average execution time (s)")
        plt.title(f"QuickSort Performance – {scenario} Data")
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    run_experiments()
