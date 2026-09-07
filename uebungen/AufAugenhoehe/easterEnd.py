from graphviz import Digraph

dot = Digraph(format='png')
dot.attr(rankdir='TB')
dot.attr('node', fontname='cursive')

# Emotion nodes
emotions = [
    ("e1", "Wonder & Curiosity"),
    ("e2", "Isolation & Mystery"),
    ("e3", "Prosperity & Growth"),
    ("e4", "Overreach & Competition"),
    ("e5", "Collapse & Desperation"),
    ("e6", "Warning & Reflection"),
]

for eid, label in emotions:
    dot.node(eid, label=label, shape='oval', style='filled', fillcolor='moccasin')

# Force horizontal alignment
with dot.subgraph() as s:
    s.attr(rank='same')
    for eid, _ in emotions:
        s.node(eid)

# Facts
facts = {
    "e1": ["Vanished civilizations raise questions",
           "Easter Island statues astonish explorers",
           "Polynesian origins confirmed"],
    "e2": ["Most isolated habitable island",
           "No trees, limited animals by 1722",
           "No external contact evidence"],
    "e3": ["Initial lush forest ecosystem",
           "Population grew (7k–20k)",
           "Abundant food: birds, porpoises, crops"],
    "e4": ["Statue building intensified (1200–1500)",
           "Deforestation for transport, fuel, farming",
           "Rats prevented forest regeneration",
           "Resource competition among clans"],
    "e5": ["Forest and species extinction",
           "Loss of canoes → no fishing/porpoises",
           "Cannibalism and warfare emerge",
           "Population collapse (~1700)",
           "Statues toppled by 1864"],
    "e6": ["Gradual decline unnoticed year-to-year",
           "Modern parallels: resource depletion",
           "Global society lacks escape",
           "History offers chance to learn"]
}

# Add visible arrows between emotion nodes
# for i in range(len(emotions)-1):
#     dot.edge(emotions[i][0], emotions[i+1][0])

# Add fact nodes and edges
for eid, flist in facts.items():
    prev = eid
    for i, f in enumerate(flist):
        fid = f"{eid}_f{i}"
        dot.node(fid, label=f, shape='rect', style='filled', fillcolor='lightblue')
        dot.edge(prev, fid)
        prev = fid

# Render
file_path = "eastersEndGraph"
dot.render(file_path)

file_path