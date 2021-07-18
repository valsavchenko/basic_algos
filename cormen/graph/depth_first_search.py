"""
T. H. Cormen et. al. - Introduction to Algorithms, 3rd edition, ISBN 978-0262033848
22.3 Depth-first search (p. 603)

The strategy followed by depth-first search is, as its name implies, to search
"deeper" in the graph whenever possible. Depth-first search explores edges out
of the most recently discovered vertex v that still has unexplored edges leaving it.
Once all of v's edges have been explored, the search "backtracks" to explore edges
leaving the vertex from which v was discovered. This process continues until we
have discovered all the vertices that are reachable from the original source vertex.
If any undiscovered vertices remain, then depth-first search selects one of them as
a new source, and it repeats the search from that source. The algorithm repeats this
entire process until it has discovered every vertex
"""

import collections
import enum

def find_path(graph, srcId, tgtId):
    """
    Finds a path between given vertices in O(V + E) time

    Parameters
    ----------
    graph : {int: (int, ...)}
        An adjacency list

    srcId, tgtId : int
        Ids of the source and target vertices

    Returns
    -------
    [int, ...]
        A path between the source and target vertices
    """
    COLORS = enum.Enum('COLORS', 'WHITE GRAY')

    path = []

    # Initialize the auxiliary data to fill during the lookup phase
    # and to utilize through reconstructions of a solution 
    data = {vId: {'color': COLORS.WHITE, 'previous': None} for vId in graph}

    # Explore the structure of the graph in the depth-first fashion
    queue = collections.deque([srcId])
    while queue:
        vId = queue.popleft()
        if tgtId == vId:
            # Wrap up the lookup, if the target vertex is reached
            break

        if COLORS.GRAY == data[vId]['color']:
            # Skip a vertex, that was discovered during a previous streak
            continue
        data[vId]['color'] = COLORS.GRAY

        for nvId in graph[vId]:
            if COLORS.WHITE != data[nvId]['color']:
                # Skip a vertex, which was discovered by an earlier streak
                continue

            # Update a reference to the previous vertex
            # (might be initialized by previous streaks)
            data[nvId]['previous'] = vId

            # Extend the queue at the beginning to follow the depth-first paradigm
            queue.appendleft(nvId)

    # Reconstruct a path from the target towards the source vertex
    if srcId == tgtId:
        # The source and the target vertices are the same
        path = [srcId, tgtId]
    elif data[tgtId]['previous'] is None:
        # The target could not be reached from the source
        pass
    else:
        # A path exists
        vId = tgtId
        while vId:
            path.append(vId)
            vId = data[vId]['previous']
        path.reverse()
        assert path[0] == srcId and path[-1] == tgtId

    return path

if __name__ == '__main__':
    import unittest

    class DFS(unittest.TestCase):
        def test_fig_22_4(self):
            graph = {'u': ('x', 'v'), 'x': ('v', ), 'v': ('y', ), 'y': ('x', ),
                     'w': ('y', 'z'), 'z': ('z', )}

            paths = {'u': {'u': ['u', 'u'], 'x': ['u', 'v', 'y', 'x'], 'v': ['u', 'v'],
                           'y': ['u', 'v', 'y'], 'w': [], 'z': []},
                     'x': {'u': [], 'x': ['x', 'x'], 'v': ['x', 'v'],
                           'y': ['x', 'v', 'y'], 'w': [], 'z': []},
                     'v': {'u': [], 'x': ['v', 'y', 'x'], 'v': ['v', 'v'],
                           'y': ['v', 'y'], 'w': [], 'z': []},
                     'y': {'u': [], 'x': ['y', 'x'], 'v': ['y', 'x', 'v'],
                           'y': ['y', 'y'], 'w': [], 'z': []},
                     'w': {'u': [], 'x': ['w', 'y', 'x'], 'v': ['w', 'y', 'x', 'v'],
                           'y': ['w', 'y'], 'w': ['w', 'w'], 'z': ['w', 'z']},
                     'z': {'u': [], 'x': [], 'v': [],
                           'y': [], 'w': [], 'z': ['z', 'z']}}

            for srcId in sorted(paths):
                for tgtId in sorted(paths[srcId]):
                    expected = paths[srcId][tgtId]
                    with self.subTest(srcId=srcId, tgtId=tgtId, expected=expected):
                        path = find_path(graph=graph, srcId=srcId, tgtId=tgtId)
                        self.assertEqual(path, expected)

        def test_fig_22_6(self):
            graph = {'q': ('s', 'w', 't'), 'r': ('y', 'u'), 's': ('v', ), 't': ('x', 'y'), 'u': ('y', ),
                     'v': ('w', ), 'w': ('s', ), 'x': ('z', ), 'y': ('q', ), 'z': ('x', )}

            paths = {'q': {'q': ['q', 'q'], 'r': [], 's': ['q', 'w', 's'], 't': ['q', 't'], 'u': [],
                           'v': ['q', 'w', 's', 'v'], 'w': ['q', 'w'], 'x': ['q', 't', 'x'],
                           'y': ['q', 't', 'y'], 'z': ['q', 't', 'x', 'z']},
                     'r': {'q': ['r', 'u', 'y', 'q'], 'r': ['r', 'r'], 's': ['r', 'u', 'y', 'q', 'w', 's'],
                           't': ['r', 'u', 'y', 'q', 't'], 'u': ['r', 'u'], 'v': ['r', 'u', 'y', 'q', 'w', 's', 'v'],
                           'w': ['r', 'u', 'y', 'q', 'w'], 'x': ['r', 'u', 'y', 'q', 't', 'x'],
                           'y': ['r', 'u', 'y'], 'z': ['r', 'u', 'y', 'q', 't', 'x', 'z']}}

            for srcId in sorted(paths):
                for tgtId in sorted(paths[srcId]):
                    expected = paths[srcId][tgtId]
                    with self.subTest(srcId=srcId, tgtId=tgtId, expected=expected):
                        path = find_path(graph=graph, srcId=srcId, tgtId=tgtId)
                        self.assertEqual(path, expected)

    unittest.main()