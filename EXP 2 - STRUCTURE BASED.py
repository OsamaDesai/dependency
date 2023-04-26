import pandas as pd
import networkx as nx

# Load the Facebook network dataset from a CSV file
df = pd.read_csv("C:/Users/nnair/Downloads/exp6 (network) - athletes_edges.csv")

# Create a NetworkX graph from the dataset"
G = nx.from_pandas_edgelist(df, source="node_1", target="node_2")

# Compute degree centrality
degree_centrality = nx.degree_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print the centralities for each node
for node in G.nodes():
    print(f"Node {node}:")
    print(f"\tDegree centrality: {degree_centrality[node]}")
    print(f"\tEigenvector centrality: {eigenvector_centrality[node]}")

# Find bridges in the network
bridges = list(nx.bridges(G))
print(f"Bridges in the network: {bridges}")

# # Compute betweenness centrality
# betweenness_centrality = nx.betweenness_centrality(G)

# # Compute edge centrality
# edge_centrality = nx.edge_betweenness_centrality(G)
