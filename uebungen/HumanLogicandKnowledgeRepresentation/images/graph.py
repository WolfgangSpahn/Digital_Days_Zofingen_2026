import matplotlib.pyplot as plt
import networkx as nx
import networkx.drawing.nx_pydot as nx_pydot

# --- Base nodes (original # Create layout using Graphviz dot for hierarchical layout

# --- Grundebene ---
nodes_refined_base = [
    "NS-Staat",
    "Gleichschaltung",
    "Propaganda",
    "Gewalt / Unterdrückung",
    "Diktatur",
    "Auslandsperspektive",
]

# --- Mittel-/Analyseebene ---
nodes_refined_better = [
    "Symbolik & Ironie",
    "Karikatur",
    "Metapher / Bildsymbolik",
    "Bildobjekte",
    "Kritik durch Übersteigerung",
    "Typenfiguren",
    "Text- und Wortinschriften",
    "Überfüllte Komposition",
]

# --- Meta-/Deutungsebene ---
nodes_excellent_new = [
    "Selbstinszenierung des Regimes",
    "Symbolische Verdichtung",
    "Moralische Wertung",
]

# --- Konkrete Karikaturanalyse ---
nodes_analysis_specific = [
    "Feindbilder",
    "Propagandamechanismen",
    "Leere Phrasen / Versprechungen",
    "Satirische Entlarvung",
    "Antifaschistische Kritik",
    "Ironische Umkehrung",
    "Visuelle Übertreibung",
    "Symbol für ideologische Waffen",
]

# --- Basisebene (historischer Kontext) ---
edges_base = [
    ("NS-Staat", "Gleichschaltung", "sichert Macht durch"),
    ("NS-Staat", "Propaganda", "lenkt Gesellschaft mittels"),
    ("NS-Staat", "Gewalt / Unterdrückung", "erhält Kontrolle durch"),
    ("NS-Staat", "Diktatur", "entwickelt sich zu"),
    ("NS-Staat", "Auslandsperspektive", "wird wahrgenommen aus"),
]

# --- Mittel-/Analyseebene ---
edges_better = [
    ("Karikatur", "Symbolik & Ironie", "erhöht Wirkung durch"),
    ("Bildobjekte", "Metapher / Bildsymbolik", "verdeutlichen"),
    ("Karikatur", "Bildobjekte", "setzt ein"),
    ("Karikatur", "Typenfiguren", "zeigt gesellschaftliche Rollen durch"),
    ("Karikatur", "Text- und Wortinschriften", "verwendet als Mittel der Kritik"),
    ("Überfüllte Komposition", "Kritik durch Übersteigerung", "unterstreicht"),
    ("Karikatur", "Überfüllte Komposition", "erzeugt Groteske durch"),
    ("Karikatur", "historische Quelle", "fungiert als"),
]

# --- Metaebene / Deutung ---
edges_excellent_new = [
    ("NS-Staat", "Selbstinszenierung des Regimes", "präsentiert sich durch"),
    ("Selbstinszenierung des Regimes", "Karikatur", "wird gespiegelt in"),
    ("Auslandsperspektive", "Karikatur", "verdeutlicht Wahrnehmung von"),
    ("Metapher / Bildsymbolik", "Symbolische Verdichtung", "bündelt Aussage in"),
    ("Symbolische Verdichtung", "Karikatur", "steigert Deutung von"),
    ("Propaganda", "Selbstinszenierung des Regimes", "trägt bei zu"),
    ("Kritik durch Übersteigerung", "Satirische Darstellung", "zeigt sich in"),
    ("Satirische Darstellung", "Moralische Wertung", "stützt sich auf"),
    ("Moralische Wertung", "Karikatur", "prägt Wahrnehmung von"),
]


edges_analysis_specific = [
    ("Karikatur", "Feindbilder", "entlarvt durch"),
    ("Feindbilder", "Propagandamechanismen", "werden erzeugt durch"),
    ("Propagandamechanismen", "NS-Staat", "stützen"),
    ("Karikatur", "Leere Phrasen / Versprechungen", "macht sichtbar"),
    ("Leere Phrasen / Versprechungen", "Propaganda", "stehen für"),
    ("Karikatur", "Satirische Entlarvung", "bewirkt"),
    ("Satirische Entlarvung", "Antifaschistische Kritik", "führt zu"),
    ("Antifaschistische Kritik", "Moralische Wertung", "unterstreicht"),
    ("Karikatur", "Ironische Umkehrung", "arbeitet mit"),
    ("Ironische Umkehrung", "Visuelle Übertreibung", "verstärkt durch"),
    ("Visuelle Übertreibung", "Kritik durch Übersteigerung", "verbindet sich mit"),
    ("Symbol für ideologische Waffen", "NS-Staat", "spiegelt Machtmittel des"),
    ("Symbol für ideologische Waffen", "Bildobjekte", "erscheint in"),
    ("Bildobjekte", "Feindbilder", "stellen dar"),
    ("Text- und Wortinschriften", "Leere Phrasen / Versprechungen", "verdeutlichen"),
]



# --- Build Graph ---
G = nx.Graph()

# Add all nodes
all_nodes = list(set(nodes_refined_base + nodes_refined_better + nodes_excellent_new + nodes_analysis_specific))
G.add_nodes_from(all_nodes)

# Add edges with color and layer
def add_edges(edge_list, color, weight):
    for u, v, label in edge_list:
        G.add_edge(u, v, color=color, weight=weight, label=label)

add_edges(edges_base, "gray", 1)
add_edges(edges_better, "gray", 1)
add_edges(edges_excellent_new, "gray", 1)
add_edges(edges_analysis_specific, "gray", 1)

# --- Node colors by category ---
node_colors = []
for n in G.nodes():
    if n in nodes_excellent_new:
        node_colors.append("orangered")  # meta-level
    elif n in ["Metapher / Bildsymbolik", "Bildobjekte", "Kritik durch Übersteigerung", "Visuelle Wahrnehmung / Auffassung"]:
        node_colors.append("orange")  # visual-symbolic level
    elif n in nodes_refined_better:
        node_colors.append("gold")  # analytical level
    else:
        node_colors.append("lightgray")  # base level

# --- Layout and drawing ---
# Assign node levels by category for shell layout
node_levels = {}
for n in G.nodes():
    if n in nodes_refined_base:
        node_levels[n] = 0
    elif n in nodes_refined_better:
        node_levels[n] = 1
    elif n in nodes_excellent_new:
        node_levels[n] = 2
    else:
        node_levels[n] = 3

# Create layout using Graphviz dot for hierarchical layout
pos = nx_pydot.graphviz_layout(G, prog='neato')
plt.figure(figsize=(18, 24))
edges = G.edges(data=True)
colors = [d["color"] for (u, v, d) in edges]
weights = [d["weight"] for (u, v, d) in edges]

nx.draw_networkx_edges(
    G,
    pos,
    edge_color=colors,
    width=weights,
    alpha=0.8
)

# Draw rectangular nodes
for i, node in enumerate(G.nodes()):
    x, y = pos[node]
    plt.text(
        x, y, node,
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="white", edgecolor="black", alpha=0.9)
    )

# Edge labels
edge_labels = {(u, v): data["label"] for u, v, data in G.edges(data=True) if data.get("label")}
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=11,
    font_color="darkred",
    rotate=False,
    bbox=dict(facecolor="white", edgecolor="none", alpha=0.7, pad=1),
)

plt.axis("off")
plt.gca().set_position([0, 0, 1, 1])
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.savefig('graph.svg', format='svg')
plt.show()
