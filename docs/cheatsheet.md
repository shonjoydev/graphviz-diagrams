# Color and Style Cheatsheet

Copy the hex codes into the `node` and `edge` lines of your dot block.

## Palettes

### Indigo (default)

| Element | Light | Dark |
|---|---|---|
| Node fill | `#eef2ff` | `#1e293b` |
| Node border | `#4f46e5` | `#818cf8` |
| Node text | `#1e1b4b` | `#e0e7ff` |
| Edge line | `#64748b` | `#94a3b8` |
| Weight text | `#b45309` | `#fbbf24` |
| Highlight | `#dc2626` | `#f87171` |

### Emerald

| Element | Light | Dark |
|---|---|---|
| Node fill | `#ecfdf5` | `#022c22` |
| Node border | `#059669` | `#34d399` |
| Node text | `#064e3b` | `#d1fae5` |
| Edge line | `#6b7280` | `#9ca3af` |
| Weight text | `#c2410c` | `#fcd34d` |
| Highlight | `#dc2626` | `#fb7185` |

### Mono (ultra minimal)

| Element | Light | Dark |
|---|---|---|
| Node fill | `#ffffff` | `#111827` |
| Node border | `#111827` | `#f3f4f6` |
| Node text | `#111827` | `#f3f4f6` |
| Edge line | `#6b7280` | `#9ca3af` |
| Weight text | `#374151` | `#d1d5db` |
| Highlight | `#dc2626` | `#f87171` |

### Rose

| Element | Light | Dark |
|---|---|---|
| Node fill | `#fff1f2` | `#2a0a14` |
| Node border | `#e11d48` | `#fb7185` |
| Node text | `#4c0519` | `#ffe4e6` |
| Edge line | `#78716c` | `#a8a29e` |
| Weight text | `#0369a1` | `#38bdf8` |
| Highlight | `#7c3aed` | `#c4b5fd` |

### Neutral (one image for both themes)

| Element | Value |
|---|---|
| Node fill | `#6366f1` |
| Node border | `#4338ca` |
| Node text | `#ffffff` |
| Edge line | `#64748b` |
| Weight text | `#d97706` |

## Style tokens

| Property | Value |
|---|---|
| Background | `bgcolor=transparent` |
| Node shape | `circle`, `fixedsize=true`, `width=0.66` |
| Line widths | `penwidth=2.5` (highlight: `4`) |
| Fonts | `Times-Bold` 22 (nodes), 20 (weights) |
| Layout | `layout=neato` with `pos="x,y!"` |
| Weight beside the edge | `xlabel` plus `forcelabels=true` |
| Weight on the edge | `label` |

## Template

```
node [shape=circle, fixedsize=true, width=0.66,
      fontname="Times-Bold", fontsize=22, style=filled,
      fillcolor="<NODE_FILL>", color="<NODE_BORDER>",
      fontcolor="<NODE_TEXT>", penwidth=2.5];
edge [color="<EDGE>", penwidth=2.5,
      fontname="Times-Bold", fontsize=20, fontcolor="<WEIGHT>"];
```

## Highlight a path or MST

```
A -- D [xlabel="5", color="#dc2626", penwidth=4];
```

## Tips

- On a transparent background, use mid-tone edge colors so they stay readable on white and near-black pages.
- Use one accent color for weights and one for highlights.
- Positions are in inches, `pos="x,y!"`. The `!` pins the node, and the origin is the bottom-left.
- `graph` with `--` is undirected, `digraph` with `->` is directed.
