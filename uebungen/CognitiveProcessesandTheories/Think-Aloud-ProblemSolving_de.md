---
geometry: left=3cm,right=3cm,top=3cm,bottom=3cm
title: Think-Aloud Problemlösen
abstract: >
  Lautes Denken ist eine Methode, um den eigenen Denkprozess sichtbar zu machen. Durch das Verbalisieren von Gedanken und Überlegungen können Lernende ihre Problemlösungsstrategien reflektieren und verbessern. Diese Technik bringt interessanterweise auch ein LLM (Large Language Model) dazu, seine „Gedanken“ zu strukturieren und zu erklären, was zu besseren und nachvollziehbareren Antworten Richtung System 2 denken führt.
author: Dr. W. Spahn
---

# Lautes Denken beim Problemlösen
*

## Ausgewähltes Problem: Das Monty-Hall-Problem

* **Szenario:** Ein Spielshow-Kandidat wird mit 3 Türen konfrontiert. Hinter einer ist ein Auto, hinter den anderen beiden sind Ziegen. Der Kandidat wählt eine Tür. Der Moderator (der weiß, was hinter jeder Tür ist) öffnet eine andere Tür und zeigt eine Ziege. Der Kandidat hat dann die Wahl: bei seiner ursprünglichen Wahl bleiben oder zur verbleibenden ungeöffneten Tür wechseln.

---

## Teilnehmeransätze

### Teilnehmer A (Intuitives Denken – „System 1“)

* **Verbalisierter Prozess:**

  * „Ich habe bereits eine Tür gewählt, also sind die Chancen jetzt 50/50. Es spielt keine Rolle, ob ich wechsle oder bleibe.“
* **Ergebnis:** Blieb bei der ersten Wahl.
* **Kommentar:** Verließ sich auf intuitives Denken, indem die Situation mit einem Münzwurf gleichgesetzt wurde.

### Teilnehmer B (Analytisches Denken – „System 2“)

* **Verbalisierter Prozess:**

  * „Anfangs hatte ich eine 1/3 Chance, richtig zu liegen. Das bedeutet, die anderen beiden Türen zusammen hatten eine 2/3 Chance. Der Moderator entfernt eine Ziege, aber das ändert die anfänglichen Wahrscheinlichkeiten nicht. Also trägt die ungeöffnete Tür jetzt die volle 2/3 Chance. Ich sollte wechseln.“
* **Ergebnis:** Wechselte die Türen.
* **Kommentar:** Nutzte Schritt-für-Schritt-Logik, um die Intuition zu widerlegen.

### Teilnehmer C (Hybrider Ansatz – Schema + Heuristik)

* **Verbalisierter Prozess:**

  * „Ich erinnere mich, dass ich schon einmal von diesem Rätsel gelesen habe – es hieß, wechseln sei besser. Also wechsle ich.“
* **Ergebnis:** Wechselte die Türen.
* **Kommentar:** Verließ sich auf vorheriges Schema anstatt es vollständig durchzudenken.

---

## Vergleichende Analyse

* **System 1 vs. System 2:** Die Intuition von Teilnehmer A spiegelt *System-1-Denken* wider (schnell, automatisch, aber fehleranfällig), während Teilnehmer B *System-2-Denken* zeigt (langsamer, überlegt, genauer).
* **Schema-Nutzung:** Teilnehmer C zeigt, wie vorheriges Wissen (Schemata) das Denken abkürzen kann.
* **Beobachtete Verzerrungen:** Das Denken von Teilnehmer A zeigt eine *Repräsentativitätsheuristik* – Annahme gleicher Chancen ohne vollständige Analyse.

---

## Implikationen für KI

* **Menschliches vs. KI-Denken:**

  * Menschen greifen oft auf Heuristiken oder Intuition zurück, was manchmal zu falschen Antworten führt.
  * KI-Systeme, wenn sie mit *Ketten-denken-Reasoning* entworfen werden, ähneln Teilnehmer B: explizites Durcharbeiten der logischen Schritte, um zur richtigen Antwort zu gelangen.

* **Herausforderungen:**

  * Wie Menschen kann KI auch zu sehr auf „Schemata“ (Trainingsdatenmuster) vertrauen, was zu übermäßiger Zuversicht, aber falschen Antworten führt.
  * Die Förderung von Transparenz (z.B. Schritt-für-Schritt-Reasoning in KI) spiegelt die Vorteile der Laut-denken-Methode für Menschen wider.

---

## Reflexion

Diese Aktivität hebt die Vielfalt menschlicher Problemlösungsstrategien hervor. Während Intuition effizient ist, neigt strukturiertes Denken dazu, in formalen Logikproblemen genauer zu sein. Die Parallelen zum KI-Denken zeigen, warum explizite Reasoning-Methoden wichtig für den Aufbau vertrauenswürdiger KI-Systeme sind.