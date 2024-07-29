"""Module contains function to merge k sorted lists."""

import heapq

def merge_k_lists(lists):
    """Merge sorted lists."""
    heap = []
    
    # Ініціалізуємо купу першими елементами кожного списку
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heapq.heappush(heap, (sorted_list[0], i, 0))
    
    result = []
    
    # Виконуємо злиття списків
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        if element_idx + 1 < len(lists[list_idx]):
            next_element = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_element, list_idx, element_idx + 1))
    
    return result

def main():
    """Main function."""
    lists = [[1, 4, 5], [1, 3, 4], [2, 3, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
    
if __name__ == "__main__":
    main()
