def flipGame(arr):
    # Initialize a set to store unique results
    results = set()
    
    # Iterate through the array
    for i in range(len(arr)):
        # Check if the current element is 0
        if arr[i] == 0:
            # Flip the current element to 1
            arr[i] = 1
            
            # Add the new configuration to the results set
            results.add(tuple(arr))
            print(f"Current unique configurations: {results}")
            
            # Flip back to 0 for the next iteration
            arr[i] = 0
            
    return len(results)

print(flipGame([0, 0, 1, 0, 1]))  # Output: 3