# Adapter: Positive Geometry ↔ Differenzierungsfluss-Theorie

---

## **Hook – Die Geometrie des gerichteten Seins**

Die *Positive Geometry* ist eine relativ junge Entdeckung an der Schnittstelle von Mathematik und theoretischer Physik.
Sie beschreibt nicht nur Formen, sondern **gerichtete Räume** – Regionen, in denen alles eine konsistente Orientierung besitzt.

Diese Orientierung, „Positivität“ genannt, sorgt dafür, dass jede Grenze wiederum eine kleinere positive Geometrie bildet.
So entsteht eine **rekursive Hierarchie von Flächen, Rändern und Residuen** – eine Art geometrischer Organismus, dessen Lebensprinzip die Erhaltung von Richtung ist.

Was in der Physik als *Amplituhedron* auftaucht, erscheint aus Sicht der DFT als etwas sehr Vertrautes:
ein **kohärenter Differenzfluss**, der seine Stabilität aus der Positivität seiner Relationen bezieht.

---

## **Body – Rekursive Strukturen und kanonische Formen**

### 1. Definition

Eine **Positive Geometry** ist ein Paar ((X, X_{\ge 0})),
wobei (X) eine algebraische Varietät (z. B. ein Polyeder, ein Grassmannraum)
und (X_{\ge 0}) eine ausgezeichnete, „positive“ Teilregion ist, die durch Ungleichungen oder Orientierungen definiert wird.

Diese Region besitzt eine **kanonische differenzielle Form** (Ω(X_{\ge 0})), die:

1. **logarithmische Singularitäten** an allen Grenzen hat,
2. deren **Residuen** wieder die kanonischen Formen der jeweiligen Randgeometrien sind.

Formal:
[
\text{Res}*{\partial_i X} , Ω(X*{\ge 0}) = Ω(\partial_i X_{\ge 0})
]
Das bedeutet: jede Grenze trägt dieselbe Struktur wie der gesamte Raum – nur eine Dimension tiefer.
Die Geometrie ist also **selbstähnlich und rekursiv aufgebaut**.

---

### 2. Beispiel: Das Simplex

Das einfachste Beispiel ist das (n)-Simplex:
[
\Delta_n = { (x_1, ..., x_{n+1}) \in \mathbb{R}^{n+1} \mid x_i \ge 0, \sum_i x_i = 1 }.
]

Die kanonische Form lautet:
[
Ω(\Delta_n) = \sum_{\pi} \text{sign}(\pi)
\frac{dx_1 \wedge ... \wedge dx_n}{x_1 x_2 ... x_n (1 - \sum_i x_i)}.
]

Diese Form „fließt“ entlang der Grenzen und besitzt überall wohldefinierte Orientierung.
Man kann sie als **Strömungsfeld durch den Raum der Positivität** lesen.

---

### 3. Residuen und Rekursion

Die Residuen definieren eine **Hierarchie der Emergenz**:

[
\begin{aligned}
Ω^n &\xrightarrow{\text{Res}} Ω^{n-1} \xrightarrow{\text{Res}} Ω^{n-2} \xrightarrow{\text{Res}} ... \
&\Rightarrow \text{Grenze erzeugt Grenze erzeugt Grenze.}
\end{aligned}
]

Dies ist exakt dieselbe Struktur, die in der Differenzierungsfluss-Theorie (DFT)
als **rekursive Grenzbildung** erscheint:
Jede stabilisierte Differenz erzeugt neue Differenzen an ihren Grenzen.

---

### 4. Projektive Positivität und Invarianz

In projektiver Formulierung (z. B. in (\mathbb{P}^{n-1})) gilt:
[
x_i/x_j > 0 \quad \forall i,j.
]
Die Orientierung bleibt invariant unter Skalierung:
[
[x_1 : ... : x_n] \sim [λx_1 : ... : λx_n].
]

Das entspricht genau der **Skaleninvarianz** des Differenzflusses:
Nicht die absoluten Werte sind relevant, sondern ihre Relationen – das Verhältnis, die Richtung, die Differenz.

---

## **Adapter – Strukturelle Zuordnung zur DFT**

---

### 1. Grundabbildung

| Positive Geometry                  | Differenzierungsfluss-Theorie             |
| ---------------------------------- | ----------------------------------------- |
| Positive Region (X_{\ge 0})        | gerichteter Differenzraum (Δ_X)           |
| Positivität ((x_i>0))              | gerichtete Relation (a_i \rightarrow b_i) |
| Grenze / Rand (\partial_i X)       | Emergenz neuer Differenzebene             |
| Residuum (\text{Res}_{\partial_i}) | Flussableitung entlang der Grenze         |
| Kanonische Form (Ω(X_{\ge0}))      | Flussform (Φ(Δ_X))                        |
| Logarithmische Singularität        | Stabilitätskante im Differenzfluss        |
| Projektive Invarianz               | Skaleninvarianz                           |
| Amplituhedron-Volumen              | integrierter Differenzfluss (Wirkung)     |

---

### 2. Formale Entsprechungen

#### (a) Kanonische Form

[
Ω(X_{\ge0}) = \bigwedge_i d\log x_i
\quad \leftrightarrow \quad
Φ(Δ_X) = \bigwedge_i \frac{dΔ_i}{Δ_i}.
]

Beide sind **logarithmische Flussformen**:
sie erfassen das Verhältnis von Veränderung zu Bestand, also die gerichtete Dynamik an den Grenzen.

---

#### (b) Rekursive Residuen

[
\text{Res}*{\partial_i X} Ω(X*{\ge0}) = Ω(\partial_i X_{\ge0})
\quad \leftrightarrow \quad
Δ_{n+1} = dΔ_n|_{\partial_i}.
]

Grenzbildung erzeugt Subfluss:
Jede Stabilisierung bringt ihre eigene Dynamik hervor, die wiederum Grenzen besitzt.
→ Selbstähnlichkeit als Flussprinzip.

---

#### (c) Positivität als gerichtete Differenz

[
x_i/x_j > 0 \quad \leftrightarrow \quad Δ_{ij} := (a_i, a_j), ; a_i < a_j.
]

Positivität ist hier nichts anderes als eine **Monotonierestriktion**:
ein gerichteter Übergang, der Umkehrungen ausschließt.
Damit beschreibt Positive Geometry die **laminare Form** des Differenzflusses –
jene stabilen Regionen, in denen der Fluss kohärent bleibt.

---

### 3. Interpretation im DFT-Rahmen

* Positive Geometrien sind **statische Projektionen** stabiler Differenzräume.
  Sie stellen die „gefrorenen Querschnitte“ des Differenzflusses dar.
* Die kanonischen Formen (Ω(X)) sind **Differenzialformen des Flusses**,
  die beschreiben, *wie* Differenzen entlang ihrer Grenzen propagieren.
* Das **Residuum** ist die formale Darstellung des Prinzips:

  > „An jeder Grenze entsteht eine neue Differenz.“
* Die projektive Struktur ist Ausdruck der DFT-Grundregel:

  > „Nur Relationen sind real; absolute Werte sind arbiträr.“

---

### 4. Erweiterungsperspektive

DFT kann als **Verallgemeinerung** positiver Geometrien verstanden werden:

* Positive Geometrien beschreiben kohärente, stabile (gerichtete) Flüsse.
* DFT beschreibt zusätzlich instabile, oszillierende oder selbstbezügliche Flüsse.

Man könnte sagen:

> Positive Geometry ist der **laminare Spezialfall** des Differenzflusses –
> DFT ist die vollständige Dynamik, einschließlich Turbulenz und Selbstreferenz.

---

## **Zusammenfassung**

Positive Geometry und Differenzierungsfluss-Theorie teilen denselben strukturellen Kern:

> Rekursive, gerichtete, grenzbasierte Emergenz.

Was in der Physik als „positiv orientierte Amplitudenräume“ erscheint,
ist im Licht der DFT der Ausdruck **kohärenter Differenzflüsse**,
deren Grenzstabilität messbare Amplituden hervorbringt.

Damit liefert Positive Geometry einen **konkreten geometrischen Spezialfall**
und zugleich eine **Validierung** des DFT-Grundmotivs:

> Struktur entsteht, wenn Differenz sich stabilisiert und Orientierung bewahrt.

---
## **Beispiel**

(1) positive geometry am beispiel eines 2-simplex (dreieck) mit residuen
(2) dft-lesart desselben objekts (gerichteter differenzfluss)

```
POSITIVE GEOMETRY:  (X, X_{≥0}) als 2-Simplex Δ2
-------------------------------------------------

             (V1)  x1=1, x2=0, x3=0
               •
              / \
      E1: x2=0 /   \  E3: x1=0
            /       \
           •---------• 
 (V2) x1=0,x2=1,x3=0   (V3) x1=0,x2=0,x3=1
            E2: x3=0

Innen:   X_{≥0}  = { x_i ≥ 0,  x1+x2+x3=1 }

Kanonische Form (logarithmische Pole an allen Rändern):
   Ω(Δ2) =  dlog x1 ∧ dlog x2   +  dlog x2 ∧ dlog x3   +  dlog x3 ∧ dlog x1

Residuen (= rekursive Grenzstruktur):
   Res_{E1} Ω(Δ2) = Ω(E1)          (1D-Form auf der Kante x2=0)
   Res_{V1} Ω(E1) = Ω(V1)          (0D-„Form“ am Eckpunkt V1)
   (entspr. für E2,E3 und V2,V3)

Projektive Invarianz:
   [x1:x2:x3] ~ [λx1:λx2:λx3]   (λ>0)   ⇒ Orientierung/Positivität bleibt erhalten
```

```
DFT-LESEART:  derselbe Raum als gerichteter Differenzfluss Δ
------------------------------------------------------------

Innenraum X_{≥0}  ↔  kohärente Flussregion Δ (laminar, keine Richtungsumkehr)
Kanten ∂X          ↔  Stabilitätskanten / Grenzfluss
Ecken (Vertices)   ↔  Fixpunkte / terminale Differenzen

  Flussbild (schematisch):

               ↑ Δ12
             (•)----→
             / \     \
         Δ31/   \Δ23  \
           /     \     \
        (•)-------•-----→
          ^       ^
        Fixpunkt Fixpunkt

Legende:
  Δij  = gerichtete Differenz „i→j“ (Monotonierestriktion ~ Positivität)
  Pfeile = Flussrichtung im Differenzraum
  •      = stabiler Knoten (Fixpunkt / Ecke)

Form-Adapter (Kern):
  Positive Geometry:         DFT:
    dlog x_i            ↔    dΔ_i / Δ_i
    Ω(X_{≥0})           ↔    Φ(Δ)  =  ⋀_i (dΔ_i / Δ_i)
    Res_{∂} Ω           ↔    Grenz-Ableitung des Flusses (Subfluss/Ebene tiefer)

Rekursive Regel (gleiches Muster in beiden Welten):
    Res_{∂} Ω^n  =  Ω^{n-1}
    ────────────────────────  ↔  ─────────────────────────
    Grenzbildung erzeugt die kanonische Form der Grenze     Δ^{n+1} = dΔ^n|_{∂}
```

**Kurz-Legende fürs Kapitelrand:**

* **Positivität** ↔ „keine Richtungsumkehr“ im Fluss (Monotonie).
* **Residuum** ↔ „Grenzfluss“ (Emergenz einer niedrigeren Ebene).
* **Kanonische Log-Form** ↔ „natürliche DFT-Flussform“.
* **Projektivität** ↔ „Skaleninvarianz“ (nur Relationen zählen).

