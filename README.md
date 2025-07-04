
# Science Flowchart

A living, version-controlled map of the scientific disciplines and how they interconnect.  
The single source-of-truth for the diagram is  
```

diagrams/core-sciences.mmd

```
which is rendered in both:

- **`docs/index.html`** (for local preview and GitLab Pages)  
- **This README** (inline, via Mermaid)

---

## Project layout

```

/
├── data/                   # optional: raw taxonomy (JSON/YAML)
│   └── disciplines.json
├── diagrams/
│   └── core-sciences.mmd   ← master Mermaid file
├── docs/                   # GitLab Pages site & local preview
│   ├── index.html
│   └── assets/
│       ├── css/style.css
│       └── js/mermaid-init.js
├── scripts/
│   └── gen\_mermaid.py      # (optional) regenerates core-sciences.mmd
├── .gitlab-ci.yml          # CI to publish `docs/` as Pages
├── README.md               ← you are here
└── LICENSE

````

---

## 1. View locally

Serve the **project root** on port 8000:

```bash
python3 -m http.server 8000
````

Then open in your browser:

```
http://localhost:8000/docs/index.html
```

This page will fetch and render `diagrams/core-sciences.mmd` via Mermaid.

---

## 2. Publish on GitLab Pages

1. Ensure `.gitlab-ci.yml` copies `docs/ -> public/`.
2. Push to the `main` branch.
3. In GitLab, go to **Settings → Pages** for your site URL:

   ```
   https://<namespace>.gitlab.io/<project>/
   ```
4. Visit that URL to see your live, interactive Science Flowchart.

---

## 3. Single source-of-truth

All chart content lives in one file:

```
diagrams/core-sciences.mmd
```

**To extend**: edit that file, add or reorganize nodes/arrows, then commit & push.
On load (local or Pages), the diagram updates automatically.

---

## 4. Inline flowchart

Below is the full flowchart as rendered here in GitHub-compatible Markdown.
(The same content is in `diagrams/core-sciences.mmd`.)

```mermaid
flowchart TD
  %% Top-level categories
  FS[Formal Sciences]
  NS[Natural Sciences]
  SS[Social Sciences]
  AS[Applied Sciences]
  ID[Interdisciplinary]

  FS --> NS
  FS --> SS
  FS --> AS
  NS --> ID
  SS --> ID
  AS --> ID

  %% A few key subfields
  FS --> MATH[Mathematics]
  FS --> LOGIC[Logic]

  NS --> PHYS[Physics]
  NS --> CHEM[Chemistry]
  NS --> BIO[Biology]

  AS --> ENG[Engineering]
  AS --> CS[Computer Science]

```

---

## 5. Contributing

1. Edit `data/disciplines.json` (if using the JSON source) or directly `diagrams/core-sciences.mmd`.
2. (Re-)run `scripts/gen_mermaid.py` if you edited the JSON.
3. Commit & push.
4. Refresh `docs/index.html` (local or Pages) and update the inline block above if you want this README to reflect the latest structure.

---

## License

Apache 2.0 © 2025 Your Name

```
```
