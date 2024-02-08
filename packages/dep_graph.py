import json
import os
from typing import Dict, Any, List, Tuple

import matplotlib.pyplot as plt
import networkx as nx


def file_reader(filename: str) -> None:
    print("Hello")
    """
    Reads the JSON file and generates the dependency graph.

    Args:
        filename: The name of the JSON file.

    Returns:
        None
    """
    with open(filename) as file:
        graph = json.load(file)
    visualize_directed_graph(graph)
    dependency_graph = dependency_graph_builder(graph)
    print_graph(dependency_graph)


def dependency_graph_builder(graph: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    Builds the dependency graph.

    Args:
        graph: A dictionary representing the graph.

    Returns:
        A dictionary representing the dependency graph.
    """
    dependency_graph = dict()
    for package in graph.keys():
        dependency_graph.update(dependency_graph_builder_helper(package, graph))
    return dependency_graph


def dependency_graph_builder_helper(package: str, graph: Dict[str, List[str]]) -> Dict[str, Any]:
    """
    A helper function for building the dependency graph.

    Args:
        package: The name of the package.
        graph: A dictionary representing the graph.

    Returns:
        A dictionary representing the dependency graph.
    """
    sub_graph = {package: []}
    if len(graph[package]) == 0:
        return sub_graph
    for dependency in graph[package]:
        sub_graph[package].append(dependency_graph_builder_helper(dependency, graph))
    return sub_graph


def print_graph(graph: Dict[str, Any], n: int = 0) -> None:
    """
    Prints the dependency graph.

    Args:
        graph: A dictionary representing the dependency graph.
        n: The number of tabs for formatting purposes.

    Returns:
        None
    """
    for package in graph.keys():
        tabs = "\t" * n
        print(f"{tabs}-{package}")
        if len(graph[package]) == 0:
            return
        else:
            n += 1
            for each in graph[package]:
                print_graph(each, n)
            n = 0


def visualize_directed_graph(packages: Dict[str, List[str]]) -> None:
    """
    Visualizes a directed graph of the input format.

    Args:
        packages: A dictionary representing the packages and their dependencies.

    Returns:
        None
    """
    G = nx.DiGraph()
    for keys in packages:
        if len(packages[keys]) >= 1:
            for i in range(len(packages[keys])):
                G.add_edge(keys, packages[keys][i])
        else:
            continue
    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=1000, node_color="orange")
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="black", arrowsize=60)
    nx.draw_networkx_labels(G, pos)
    return plt.show()


if __name__ == "__main__":
    # Change the working directory to the location of the file
    os.chdir(os.path.dirname(__file__))
    file_reader("deps.json")
