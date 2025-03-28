def heapSize(heap: list[int]) -> int:
    return len(heap)


def addHeap(heap: list[int], new_value: int) -> list[int]:
    heap.append(new_value)
    i = heapSize(heap) - 1
    parent = (i - 1) // 2

    while i > 0 and heap[parent] < heap[i]:
        heap[i], heap[parent] = heap[parent], heap[i]

        i = parent
        parent = (i - 1) // 2

    return heap


heap = [1, 2, 3, 5, 7, 10, 12]
print(addHeap(heap, 10))
