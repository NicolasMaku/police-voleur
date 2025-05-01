from models.Utilitaire.Util import Util


def parcours_largeur(graph, start, end, obstacles):
    queue = [(start, [start])]
    visited = []

    while queue:
        current, path = queue.pop(0)
        visited.append(current)

        if current == end:
            return path

        for neighbor in range(len(graph[current])):
            if graph[current][neighbor] and neighbor not in visited and neighbor not in obstacles:
                queue.append((neighbor, path + [neighbor]))

    return []


