# Weighted Graph

## Both modes (light and dark)

![Weighted graph][graph-light]
![Weighted graph][graph-dark]

## One image for both themes

![Weighted graph][graph-neutral]

---

## Source code

Edit a block and push. GitHub Actions updates the URL lines at the bottom of this file.

> [!NOTE]
> **Light mode source**
>
> ```dot
> // graphviz: graph-light
> graph G {
>     layout=neato;
>     bgcolor=transparent;
>     forcelabels=true;
>
>     node [shape=circle, fixedsize=true, width=0.66,
>           fontname="Times-Bold", fontsize=22,
>           style=filled, fillcolor="#eef2ff", color="#4f46e5",
>           fontcolor="#1e1b4b", penwidth=2.5];
>     edge [color="#64748b", penwidth=2.5,
>           fontname="Times-Bold", fontsize=20, fontcolor="#b45309"];
>
>     A [pos="1.21,4.35!"];
>     B [pos="6.36,4.01!"];
>     C [pos="3.66,3.42!"];
>     D [pos="1.22,1.76!"];
>     E [pos="5.41,2.23!"];
>     F [pos="3.20,0.77!"];
>     G [pos="6.53,0.77!"];
>
>     A -- C [xlabel="7"];
>     A -- D [xlabel="5"];
>     C -- B [xlabel="8"];
>     C -- D [xlabel="9"];
>     C -- E [xlabel="7"];
>     B -- E [xlabel="5"];
>     D -- E [xlabel="15"];
>     D -- F [xlabel="6"];
>     E -- F [xlabel="8"];
>     E -- G [xlabel="9"];
>     F -- G [xlabel="11"];
> }
> ```

> [!NOTE]
> **Dark mode source**
>
> ```dot
> // graphviz: graph-dark
> graph G {
>     layout=neato;
>     bgcolor=transparent;
>     forcelabels=true;
>
>     node [shape=circle, fixedsize=true, width=0.66,
>           fontname="Times-Bold", fontsize=22,
>           style=filled, fillcolor="#1e293b", color="#818cf8",
>           fontcolor="#e0e7ff", penwidth=2.5];
>     edge [color="#94a3b8", penwidth=2.5,
>           fontname="Times-Bold", fontsize=20, fontcolor="#fbbf24"];
>
>     A [pos="1.21,4.35!"];
>     B [pos="6.36,4.01!"];
>     C [pos="3.66,3.42!"];
>     D [pos="1.22,1.76!"];
>     E [pos="5.41,2.23!"];
>     F [pos="3.20,0.77!"];
>     G [pos="6.53,0.77!"];
>
>     A -- C [xlabel="7"];
>     A -- D [xlabel="5"];
>     C -- B [xlabel="8"];
>     C -- D [xlabel="9"];
>     C -- E [xlabel="7"];
>     B -- E [xlabel="5"];
>     D -- E [xlabel="15"];
>     D -- F [xlabel="6"];
>     E -- F [xlabel="8"];
>     E -- G [xlabel="9"];
>     F -- G [xlabel="11"];
> }
> ```

> [!NOTE]
> **Neutral source (works on both)**
>
> ```dot
> // graphviz: graph-neutral
> graph G {
>     layout=neato;
>     bgcolor=transparent;
>     forcelabels=true;
>
>     node [shape=circle, fixedsize=true, width=0.66,
>           fontname="Times-Bold", fontsize=22,
>           style=filled, fillcolor="#6366f1", color="#4338ca",
>           fontcolor="#ffffff", penwidth=2.5];
>     edge [color="#64748b", penwidth=2.5,
>           fontname="Times-Bold", fontsize=20, fontcolor="#d97706"];
>
>     A [pos="1.21,4.35!"];
>     B [pos="6.36,4.01!"];
>     C [pos="3.66,3.42!"];
>     D [pos="1.22,1.76!"];
>     E [pos="5.41,2.23!"];
>     F [pos="3.20,0.77!"];
>     G [pos="6.53,0.77!"];
>
>     A -- C [xlabel="7"];
>     A -- D [xlabel="5"];
>     C -- B [xlabel="8"];
>     C -- D [xlabel="9"];
>     C -- E [xlabel="7"];
>     B -- E [xlabel="5"];
>     D -- E [xlabel="15"];
>     D -- F [xlabel="6"];
>     E -- F [xlabel="8"];
>     E -- G [xlabel="9"];
>     F -- G [xlabel="11"];
> }
> ```

[graph-light]: https://kroki.io/graphviz/svg/eNqV0slugzAQBuB7noK6V8fCxkCiyIfSLC_QW9QDy5AgORgBUZNWffeCWRxQLvVxvhn8j8WpDIuzdbB-FlZzZHhX11rkENZqoyvRKVZSlaIuw7wqwhLyuoNUlTHIMAJZNXiFzUKXc5WAdazOYQEizspYArbS7AZJlX2DbsTWV5bUZ2ETz8N6pjupyus8vIBAH9kFqmWgZIKwLutZxh67q_ouQaSZlJC0N0jZ5USvAClL02ZyKPCUe-Ci-V0DU6ARj5r-AvIuGSPuZ7ckJKdmm6HT4z5fzTv_tYKNJ1dH3HXsNfrs3-7NOhaqEogSRjEnjvuC-hxBLx5xvEZsOsp7L077mg7hbJSt-RrDlPjeKLteXMIpZoQ5o-zHrzVRbeL7oxzGBK5jpI-9XLY5bvpvEMgfZjRsDbgmdAOBgdUEHibWE9g9uSOYgWvWnwKdyt6IZ95lCqsJHJ7E2s-A0lZ-F3-3md5j#gh-light-mode-only

[graph-dark]: https://kroki.io/graphviz/svg/eNqV0ktugzAQBuB9TkHplljY5hVFXpTmcYHuoi4MjBMkByMgatKqd68xBALKpl7ON4P_sThWvDxZe-tnYekj-U1dGlYAb9TaVJJjqqSqWFPxoi55BUXTgVBVCpInIGuNF1gvTLlQGViH-sRLYGlepRIcS-RXyOr8G0yjY33lWXNiLgoCx8x0R6iiKfgZmP2Rn6FexkpmtmPKZpaQx-66uUlgIpcSsvYGKbuc9isGsqKJnrwXIhylIrLnd90ZXAiF0P0lFF0ygvzPbknIjnqbe-fK4zSJZp3_WsF1JleLJBHEsz_7t3uzDqWqmY0RwY6HqP9i9zniXgJEAy0uHuS9F9q-JkUeGWQzfo04GIXBINtefORhhyBCB9kNX9NRXRSGg-yHBD4dpY-9XLY5ruZvYHZ4nzGwGcEfQ2uIR4gm8DCxmsD2yR3xDPxx_SngqexGCcZ3mUI0gf2TWLsZYNzK7-IPOdzeyA==#gh-dark-mode-only

[graph-neutral]: https://kroki.io/graphviz/svg/eNqV0k1vgyAYB_B7P4VjV0oEFG0aD3N9-QK7NTtQxdaEilGbtVv23UfRQjW9jCM_Hp7_Qzg0vD56W-9n5ukl-VWdu6QSvFNLs7M_ZEqqJukaXrU1b0TV9VCoJhOS74VsNZ7Fcma2K5ULb9ceeS2SrGwyKaBXlBeRt-W3MAeh91Xm3THxEWPQ1PSrUFVX8ZNIwEd5Eu08VTIH0GybWkIeT7fdVYqkKKUU-a2DlH1O8MooYwXWlfeNgNI442Da686FWfp8Lao-GUHhZz-kyA96GntzEAXxfnLyXyP4cNQ6X0SRz8Dn8HZv3q5WbQIwIhgGiIYvYMiRDsIQZVp8bOV9EHp7TYoCYmXlbiMQo4hZWQ8SogBDggi1srG36ag-iiIrW5sgpE6G2PP5LcfF_IYERPcaAysHoQutIXUQj-ChYjGC9ZMe6QRCN_4Y8Fg2Tph7lzHEI9g-ibWZAMY3-Z39AU4o3kg=
