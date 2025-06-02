# 📐 Formaler Typkalkül für den λΔ-Formalismus (λΔ\_typed)

## 🧠 Zielsetzung

Der λΔ<sub>typed</sub>-Kalkül ist ein formaler Rahmen zur Typisierung von Ausdrücken im λΔ-Formalismus. Er erlaubt:

* **Strukturelle Konsistenzprüfung** differenzbasierter Ausdrücke
* **Formale Kontrolle von Flüssen, Rekursion und Approximation**
* **Kompositionsprüfung** bei Transformationen

---

## 🔣 1. Typensyntax (Ty)

Wir definieren die Typmenge `Ty`:

| Typ       | Bedeutung                                     |
| --------- | --------------------------------------------- |
| `Base`    | Elementartyp (z. B. ℝ, Bool, Zustand)         |
| `Δ T`     | Flusstyp: Veränderung von T                   |
| `Fix T`   | Fixpunktfähige Struktur                       |
| `T1 → T2` | Transformation von T1 nach T2                 |
| `∫ T`     | Akkumulierte Struktur (z. B. Felder, Energie) |
| `T ≈ T`   | Strukturelle Approximation                    |

---

## 🧩 2. Typregeln für Operatoren

### Lambda-Abstraktion

```
Γ, x: A ⊢ E: B
——————————————
Γ ⊢ λx.E : A → B
```

### Applikation

```
Γ ⊢ f : A → B    Γ ⊢ x : A
———————————————
Γ ⊢ f x : B
```

### Differenzierung

```
Γ ⊢ f : T
———————————
Γ ⊢ δ_x f : Δ T
```

### Zweite Differenzierung

```
Γ ⊢ f : T
———————————
Γ ⊢ δ²_x f : Δ (Δ T)
```

### Fixpunkt

```
Γ ⊢ E : T → T
————————————
Γ ⊢ fix(E) : Fix T
```

### Approximation

```
Γ ⊢ A : T    Γ ⊢ B : T
——————————————
Γ ⊢ A ≈ B : T ≈ T
```

### Integration

```
Γ ⊢ f : T
———————————————
Γ ⊢ ∫ x ∈ D . f(x) : ∫ T
```

---

## 🔁 3. Beispiel: Harmonischer Oszillator

λΔ-Ausdruck:
`λ x . δ²_t x ≈ -ω² ⋅ x`

Typisierung:

* `x : ℝ`
* `δ²_t x : Δ² ℝ`
* `-ω² ⋅ x : ℝ`
* `≈ : Δ² ℝ ≈ ℝ`

Ergebnis: gültiger Ausdruck

---

## 🧪 4. Konsequenzen des Typsystems

* **Strukturkontrolle**: Ungültige Ausdrücke wie `δ Bool` sind typisierungsfehlerhaft.
* **Rekursionsprüfung**: Nur `T → T`-Ausdrücke dürfen in `fix` eingesetzt werden.
* **Kompositionsfähigkeit**: Funktionale Zusammensetzung ist nur für passende Typen erlaubt.
* **Approximation**: `≈` ist nur gültig zwischen typäquivalenten Strukturen.

---

## 🐍 5. Beispielimplementierung in Python

```python
from typing import Union, Dict

class Type: pass
class Base(Type):
    def __str__(self): return "Base"
class Delta(Type):
    def __init__(self, inner): self.inner = inner
    def __str__(self): return f"Δ({self.inner})"
class Fix(Type):
    def __init__(self, inner): self.inner = inner
    def __str__(self): return f"Fix({self.inner})"
class Arrow(Type):
    def __init__(self, arg, ret): self.arg = arg; self.ret = ret
    def __str__(self): return f"({self.arg} → {self.ret})"
class Integral(Type):
    def __init__(self, inner): self.inner = inner
    def __str__(self): return f"∫({self.inner})"
class Approx(Type):
    def __init__(self, left, right): self.left = left; self.right = right
    def __str__(self): return f"{self.left} ≈ {self.right}"

class TypeError(Exception): pass

Context = Dict[str, Type]

def type_check(expr, ctx: Context) -> Type:
    match expr:
        case ('var', name):
            return ctx[name]
        case ('lambda', x, body):
            arg_type = ctx[x]
            body_type = type_check(body, ctx)
            return Arrow(arg_type, body_type)
        case ('apply', f, x):
            tf = type_check(f, ctx)
            tx = type_check(x, ctx)
            if isinstance(tf, Arrow) and str(tf.arg) == str(tx):
                return tf.ret
            raise TypeError("Applikationstyp nicht passend")
        case ('delta', e):
            t = type_check(e, ctx)
            return Delta(t)
        case ('delta2', e):
            t = type_check(e, ctx)
            return Delta(Delta(t))
        case ('fix', f):
            tf = type_check(f, ctx)
            if isinstance(tf, Arrow) and str(tf.arg) == str(tf.ret):
                return Fix(tf.arg)
            raise TypeError("Fix nur für T → T")
        case ('approx', a, b):
            ta = type_check(a, ctx)
            tb = type_check(b, ctx)
            if str(ta) == str(tb):
                return Approx(ta, tb)
            raise TypeError("≈ nur für typgleiche Ausdrücke")
        case ('integral', var, domain, body):
            t = type_check(body, ctx)
            return Integral(t)
        case _:
            raise TypeError("Unbekannter Ausdruck")
```

Diese Implementierung kann als Parserbackend, Validierungsmodul oder interaktives λΔ-Tool genutzt werden.

---

## 🧾 Fazit

> Der λΔ<sub>typed</sub>-Kalkül ist ein strukturelles Typsystem zur formalen Modellierung von Differenzflüssen, rekursiven Strukturen und semantischer Approximation im λΔ-Formalismus.

Er ist anschlussfähig an typisierte funktionale Logik, aber erweitert diese um **rekursive Dynamik, Flussstrukturen und strukturelle Semantik**.

---

Dieses Dokument darf gerne erweitert, implementiert oder als Grundlage für eine eigene Typengine in λΔ-konformen Systemen verwendet werden.
