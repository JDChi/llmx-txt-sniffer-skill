---
name: llms-txt-sniffer
description: A high-performance sniffer for AI-friendly documentation index files (llms.txt). It employs a two-stage discovery strategy—quick direct probing and advanced recursive sniffing—to instantly map documentation sites, reducing token consumption and manual navigation.
allowed-tools:
  - Bash(python3:*)
  - Bash(curl:*)
metadata:
  openclaw:
    requires:
      bins: ["python3", "curl"]
    triggers: ["docs/", "api-reference/", "platform.", ".txt"]
    version: "1.2.2"
---

# llms-txt-sniffer: The Smart Document Radar

This skill streamlines documentation ingestion by locating the most AI-optimized version of a site's content.

## 🧠 Why llms.txt?
The `llms.txt` file is an emerging standard for documentation sites (like those built with Mintlify). It provides a high-density, Markdown-based index specifically designed for LLMs to:
- **Map Entire Sites Instantly**: Get a complete tree of all documentation pages in a single request.
- **Reduce Noise**: Eliminate the need to scrape heavy HTML, JS, and UI elements (sidebars, footers).
- **Save Tokens**: Direct access to clean content prevents "token burn" caused by repeated browser rendering and navigation.

## 🚀 Discovery Strategy (Two-Stage)

### Stage 1: The "Quick Jump" (Instructional)
Before running heavy tools, the AI should perform two rapid checks:
1. **Current Directory**: Probe `${CURRENT_PATH}/llms.txt`.
2. **Domain Root**: Probe `https://${DOMAIN}/llms.txt`.

### Stage 2: Advanced Sniffing (Tool-based)
If Stage 1 fails, immediately run the specialized sniffer script to handle complex sub-directory structures (like Mintlify), breadcrumb upward probing, and sitemap extraction:
`python3 ./sniffer.py <URL>`

## 🎯 When to Use (Triggers)
Use this skill **immediately** when any of the following conditions are met:
1. **Documentation URLs**: The user provides a link containing `/docs/`, `/api-reference/`, `/guides/`, or a subdomain starting with `platform.`.
2. **"Map the Site" Requests**: The user asks "What features does this platform have?" or "Find all endpoints related to X."
3. **Scraping Failures**: Standard `web_fetch` returns heavy JS boilerplate, noise (sidebars/footers), or blocked content.
4. **Token Efficiency**: When dealing with large documentation sets where individual page scraping would be too slow or expensive.

## 🛠️ Operations

### How to Execute
1. Identify a documentation URL (e.g., MiniMax, Stripe).
2. Run the **Quick Jump** probes using `curl -I`.
3. If no `200 OK` is returned, invoke Stage 2.

## 📜 Behavioral Rules
- **Switch to High-Speed Mode**: Once an index is found (llms.txt), prioritize reading the index links over individual HTML scraping.
- **Index Summary**: Always present a brief overview of the detected structure to the user.
- **Resourceful Fallback**: If `llms.txt` is missing, use the script's `sitemap.xml` parser results.

---
