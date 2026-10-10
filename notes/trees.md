# Trees (Mermaid)

GitHub draws Mermaid natively and adapts it to the viewer's light or dark theme. The code lives right in this file.

## Binary search tree

```mermaid
flowchart TD
    N8((8)) --> N3((3))
    N8 --> N10((10))
    N3 --> N1((1))
    N3 --> N6((6))
    N10 --> N14((14))
    N6 --> N4((4))
    N6 --> N7((7))
    N14 --> N13((13))
```

| Traversal | Result |
|---|---|
| Inorder (L, Root, R) | 1, 3, 4, 6, 7, 8, 10, 13, 14 |
| Preorder (Root, L, R) | 8, 3, 1, 6, 4, 7, 10, 14, 13 |
| Postorder (L, R, Root) | 1, 4, 7, 6, 3, 13, 14, 10, 8 |

## Search path for 7

The visited nodes and edges are highlighted: `8 → 3 → 6 → 7`.

```mermaid
flowchart TD
    N8((8)) --> N3((3))
    N8 --> N10((10))
    N3 --> N1((1))
    N3 --> N6((6))
    N10 --> N14((14))
    N6 --> N4((4))
    N6 --> N7((7))
    N14 --> N13((13))

    classDef visited fill:#6366f1,stroke:#4338ca,stroke-width:2px,color:#ffffff
    class N8,N3,N6,N7 visited
    linkStyle 0,3,6 stroke:#dc2626,stroke-width:3px
```

> [!TIP]
> `linkStyle` numbers count edges in the order they are written, starting at 0. Here edge 0 is `8 → 3`, edge 3 is `3 → 6`, and edge 6 is `6 → 7`.
