# 📊 Excel PROCV (VLOOKUP) Guide

This repository contains theory, syntax, and practical examples of how to use the `PROCV` function in Excel (equivalent to `VLOOKUP` in English versions). It’s perfect for those learning Excel or preparing for Excel-based data tasks.

---

## 📘 What is PROCV?

**PROCV** stands for **"PROcura na Coluna Vertical"**. It's used to search for a value in the first column of a table and return a value in the same row from another column.

> In English, the equivalent function is **VLOOKUP**: Vertical Lookup.

---

## 🧠 Syntax

```excel
PROCV(valor_procurado, tabela_array, núm_índice_coluna, [procurar_intervalo])
```

| Argumento           | Descrição                                                                 |
|---------------------|---------------------------------------------------------------------------|
| `valor_procurado`   | Valor a ser encontrado na primeira coluna da tabela.                      |
| `tabela_array`      | Intervalo de células onde a busca será realizada.                         |
| `núm_índice_coluna` | Número da coluna (na tabela) da qual o valor será retornado.              |
| `procurar_intervalo`| [Opcional] `FALSO` para correspondência exata, `VERDADEIRO` para aproximada.|

---

## ✅ Examples

### 🔎 Example 1: Exact Match

**Goal:** Find the price of a product.

| Produto | Preço |
|---------|-------|
| Maçã    | 3.50  |
| Banana  | 2.00  |
| Uva     | 4.00  |

```excel
=PROCV("Banana", A2:B4, 2, FALSO)
```

**Result:** `2.00`

---

### 🔎 Example 2: Approximate Match (Grades)

**Goal:** Return letter grade based on numeric score.

| Nota Mínima | Conceito |
|-------------|----------|
| 0           | F        |
| 60          | D        |
| 70          | C        |
| 80          | B        |
| 90          | A        |

If the student's score is in cell `D2`:

```excel
=PROCV(D2, A2:B6, 2, VERDADEIRO)
```

**Result:** Corresponding grade based on the score.

---

## 📝 Notes

- `PROCV` only works **vertically**, and the **search value must be in the first column** of the range.
- For more flexibility (e.g., searching to the left), consider using `ÍNDICE` + `CORRESP`.
- Newer versions of Excel support `PROCX (XLOOKUP)` which is more powerful and flexible.

---

