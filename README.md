# Task 1. Comparison of Randomized and Deterministic QuickSort

Implement both the randomized and deterministic QuickSort sorting algorithms. Conduct a comparative analysis of their efficiency by measuring the average execution time on arrays of various sizes.

Results:
1. On random data – Deterministic QuickSort is consistently faster than Randomized QuickSort, because choosing a fixed pivot (last element) has no overhead, while randomized pivot selection adds extra cost in Python.
2. On sorted and reverse-sorted data – Deterministic QuickSort degrades to O(n²) (very slow), while Randomized QuickSort maintains O(n log n) performance by avoiding worst-case pivot choices.
3. Conclusion – Deterministic QuickSort is usually faster on typical random datasets, but Randomized QuickSort is more robust, guaranteeing stable performance even on adversarial inputs (sorted/reversed).


# Task 2. Creating a timetable using a greedy algorithm

Implement a program for creating a university timetable using a greedy algorithm for the set cover problem. The goal is to assign lecturers to subjects in such a way that the number of lecturers is minimized while covering all subjects.
