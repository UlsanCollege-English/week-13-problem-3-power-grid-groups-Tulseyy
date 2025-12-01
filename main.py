

def count_power_groups(stations, lines):
    """
    Count how many connected groups of power stations exist.

    stations: list of station name strings.
    lines: list of (a, b) pairs, meaning there is an undirected line between a and b.

    Return: integer number of connected components (groups) in the network.
    """

    # Step 4: Build adjacency list graph representation
    graph = {station: [] for station in stations}
    for a, b in lines:
        graph[a].append(b)
        graph[b].append(a)
    
    # Track visited stations
    visited = set()
    groups = 0
    
    # Step 6: Implement DFS to explore each connected component
    def dfs(station):
        visited.add(station)
        for neighbor in graph[station]:
            if neighbor not in visited:
                dfs(neighbor)
    
    # Count connected components
    for station in stations:
        if station not in visited:
            dfs(station)
            groups += 1
    
    return groups


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
