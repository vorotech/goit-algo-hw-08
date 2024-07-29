"""Module contains function to find minimum cost to connect cables."""

import heapq

def min_cost_to_connect_cables(cables):
    """Return minimum cost to connect cables."""
    if len(cables) == 0:
        return 0
    
    heapq.heapify(cables)
    print(f"Initial heap: {cables}")
    
    total_cost = 0
    
    while len(cables) > 1:
        # Get two shortest cables
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        print(f"Popped cables: {first}, {second}")
        
        # Connect two cables
        combined = first + second
        print(f"Combined cable: {combined}")
        
        # Add combined cable back to heap
        heapq.heappush(cables, combined)
        print(f"Heap after push: {cables}")
        
        # Update total cost
        total_cost += combined
        print(f"Current total cost: {total_cost}")
    
    return total_cost

def main():
    """Main function."""
    cables = [4, 3, 2, 6]
    print(f"Minimum cost to connect cables: {min_cost_to_connect_cables(cables)}")
    
if __name__ == "__main__":
    main()
