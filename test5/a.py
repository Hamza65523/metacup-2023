def can_reach_goal(graph, start_node, end_node):
    """Returns True if there is a path from the start node to the end node in the given graph that uses all the same edges as the shortest path except for one edge, False otherwise."""

    # Find the shortest path from the start node to the end node.
    shortest_path = find_shortest_path(graph, start_node, end_node)

    # If there is no shortest path, then it is not possible to reach the goal.
    if shortest_path is None:
        return False

    # Initialize the visited set.
    visited = set()

    # Start at the start node.
    current_node = start_node

    # While we have not reached the end node:
    while current_node != end_node:

        # Find an edge that is not used in the shortest path.
        neighbor = None
        for n in graph[current_node]:
            if n not in shortest_path:
                neighbor = n
                break

        # If we cannot find an edge that is not used in the shortest path, then it is not possible to reach the goal.
        if neighbor is None:
            return False

        # Mark the current node as visited.
        visited.add(current_node)

        # Move to the next node.
        current_node = neighbor

    # If we have reached the end node, then we have found a path that uses all the same edges as the shortest path except for one edge.
    return True


def find_shortest_path(graph, start_node, end_node):
    """Returns the shortest path from the start node to the end node in the given graph, or None if there is no such path."""

    # Initialize the queue.
    queue = [(start_node, [start_node])]

    # Initialize the visited set.
    visited = set()

    # While the queue is not empty:
    while queue:

        # Get the current node and its path from the queue.
        current_node, path = queue.pop(0)

        # If we have reached the end node, then we have found the shortest path.
        if current_node == end_node:
            return path

        # Mark the current node as visited.
        visited.add(current_node)

        # Add the neighbors of the current node to the queue.
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # If we reach this point, then there is no path from the start node to the end node.
    return None



def solve_hop_scotch_problem(graph, queries):
  """Returns the sum of the answers to all the queries in the given graph."""

  # Initialize the answer.
  answer = 0

  # For each query:
  for query in queries:

    # Get the start node and the end node for the query.
    start_node = query[0]
    end_node = query[1]

    # Check if it is possible to reach the goal.
    if can_reach_goal(graph, start_node, end_node):

      # Find the shortest path from the start node to the end node.
      shortest_path = find_shortest_path(graph, start_node, end_node)

      # Initialize the number of edges we have to travel through multiple times.
      num_edges_traveled_multiple_times = 0

      # For each edge in the shortest path:
      for i in range(len(shortest_path) - 1):

        # If we have already traveled through this edge before, then increment the number of edges we have to travel through multiple times.
        if shortest_path[i] not in shortest_path[i + 1:]:
          num_edges_traveled_multiple_times += 1

      # Add the number of edges we have to travel through multiple times to the answer.
      answer += num_edges_traveled_multiple_times

    # Otherwise, it is not possible to reach the goal and the answer is -1.
    else:
      answer += -1

  # Return the answer.
  return answer
def main():
    """Solves the Hop-Scotch problem."""

    # Read the number of test cases.
    num_test_cases = int(input())

    # For each test case:
    for test_case in range(1, num_test_cases + 1):

        # Read the number of nodes, edges, and queries in the graph.
        num_nodes, num_edges, num_queries = map(int, input().split())

        # Create an empty graph.
        graph = {}
        for i in range(num_nodes):
            graph[i] = []

        # Read the edges in the graph.
        for _ in range(num_edges):
            start_node, end_node = map(int, input().split())
            graph[start_node].append(end_node)
            graph[end_node].append(start_node)

        # Read the queries.
        queries = []
        for _ in range(num_queries):
            start_node, end_node = map(int, input().split())
            queries.append((start_node, end_node))

        # Solve the hop-scotch problem.
        answer = solve_hop_scotch_problem(graph, queries)

        # Print the answer.
        print("Case #%d: %d" % (test_case, answer))


if __name__ == "__main__":
  main()
