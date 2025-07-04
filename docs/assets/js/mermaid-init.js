// pick a neutral, modern theme and configure global settings:
mermaid.initialize({
  startOnLoad: true,
  theme: 'neutral',        // or 'forest', 'dark', etc.
  flowchart: {
    curve: 'linear',       // crisp right-angle connectors
    arrowMarkerAbsolute: false
  },
  fontFamily: 'Inter, sans-serif',
  securityLevel: 'loose'   // so relative includes work if you choose that route
});
