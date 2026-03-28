---
name: llms-txt-sniffer
description: Locate and utilize AI-friendly documentation index files (llms.txt, llms-full.txt) or sitemap.xml. Use when the user provides a documentation URL (containing /docs/, /api-reference/, /guides/, or platform subdomains) to instantly map entire sites, reduce token burn, and bypass heavy HTML/JS noise for more accurate extraction.
metadata:
  openclaw:
    version: "1.3.0"
---

# llms-txt-sniffer: The Smart Document Radar

This skill streamlines documentation ingestion by locating the most AI-optimized version of a site's content.

## Discovery Strategy (Two-Stage)

### Stage 1: Quick Jump Probes
Perform two rapid checks using `curl -I` before running complex tools:
1. **Current Directory**: Probe `${CURRENT_PATH}/llms.txt`.
2. **Domain Root**: Probe `https://${DOMAIN}/llms.txt`.

### Stage 2: Advanced Sniffing
If Stage 1 fails, run the specialized sniffer script to handle recursive sub-directories, breadcrumb probing, and sitemap extraction:
`python3 /root/.openclaw/workspace/skills/llms-txt-sniffer/sniffer.py <URL>`

## Behavioral Rules
- **Switch to High-Speed Mode**: Once an index is found, prioritize reading the index links over individual HTML scraping.
- **Index Summary**: Always present a brief overview of the detected structure to the user.
- **Resourceful Fallback**: If `llms.txt` is missing, use the script's `sitemap.xml` results.
