# Retry rendering with correct filename handling

from graphviz import Digraph

dot = Digraph(format='png')
dot.attr(rankdir='LR')
dot.attr('node', fontname='Anime Ace 2.0 BB')

dot.node('KI', 'KI im Schulalltag', style='filled', fillcolor='moccasin')

dot.node('Vorteile', 'Vorteile', style='filled', fillcolor='moccasin')
dot.node('Nachteile', 'Nachteile', style='filled', fillcolor='moccasin')
dot.node('Ambivalenz', 'Unentschiedenheit', style='filled', fillcolor='moccasin')

dot.edge('KI', 'Vorteile')
dot.edge('KI', 'Nachteile')
dot.edge('KI', 'Ambivalenz')

dot.node('Hilfe', 'Erklärhilfe\nbesseres Verständnis', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Effizienz', 'Zeitersparnis\nbessere Noten', shape='rectangle', style='filled', fillcolor='lightblue')

dot.edge('Vorteile', 'Hilfe')
dot.edge('Vorteile', 'Effizienz')

dot.node('Faulheit', 'weniger Eigenleistung', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Oberflaeche', 'oberflächliches Lernen', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Schummeln', 'Betrug & Tricks', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Misstrauen', 'Lehrer-Schüler\nVertrauensverlust', shape='rectangle', style='filled', fillcolor='lightblue')

dot.edge('Nachteile', 'Faulheit')
dot.edge('Nachteile', 'Oberflaeche')
dot.edge('Nachteile', 'Schummeln')
dot.edge('Nachteile', 'Misstrauen')

dot.node('Nachhilfe', 'KI als Nachhilfelehrer', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Zusammenfassung', 'automatische\nZusammenfassungen', shape='rectangle', style='filled', fillcolor='lightblue')

dot.edge('Hilfe', 'Nachhilfe')
dot.edge('Effizienz', 'Zusammenfassung')

dot.node('Methoden', 'Fotos, Zweithandys,\nStil-Anpassung', shape='rectangle', style='filled', fillcolor='lightblue')
dot.edge('Schummeln', 'Methoden')

dot.node('Kontrolle', 'mehr Kontrolle\n& Verdacht', shape='rectangle', style='filled', fillcolor='lightblue')
dot.edge('Misstrauen', 'Kontrolle')

dot.node('Dumm', 'einige: macht dümmer', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Klug', 'einige: macht klüger', shape='rectangle', style='filled', fillcolor='lightblue')
dot.node('Mehrheit', 'Mehrheit\nunentschieden', shape='rectangle', style='filled', fillcolor='lightblue')

dot.edge('Ambivalenz', 'Dumm')
dot.edge('Ambivalenz', 'Klug')
dot.edge('Ambivalenz', 'Mehrheit')

dot.node('Analog', 'analoger Unterricht\n(ohne KI)', style='filled', fillcolor='moccasin')
dot.node('MehrLernen', 'mehr Beteiligung\n& Eigenständigkeit', shape='rectangle', style='filled', fillcolor='lightblue')

dot.edge('Analog', 'MehrLernen')
dot.edge('KI', 'Analog', style='dashed')

dot.edge('Kontrolle','Schummeln', color='red', style='dashed', constraint='false', dir='both')

# Correct rendering (Graphviz automatically appends .png)
file_base = 'nzz_artikel_graph'
output_path = dot.render(file_base, cleanup=True)

output_path