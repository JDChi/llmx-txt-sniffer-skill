# llms-txt-sniffer

A high-performance sniffer for AI-friendly documentation index files (`llms.txt`). 

Two-stage discovery strategy — quick direct probing + advanced recursive sniffing — to instantly map documentation sites, reducing token consumption and manual navigation.

## Why llms.txt?

The `llms.txt` file is an emerging standard for documentation sites (like those built with Mintlify). It provides a high-density, Markdown-based index specifically designed for LLMs to:

- **Map Entire Sites Instantly** — Get a complete tree of all documentation pages in a single request
- **Reduce Noise** — Eliminate heavy HTML, JS, and UI elements (sidebars, footers)
- **Save Tokens** — Direct access to clean content prevents "token burn" from repeated browser rendering

## 🚀 Quick Start

```bash
# Probe a documentation site
python3 sniffer.py https://docs.example.com

# Output (JSON)
{
  "target_url": "https://docs.example.com",
  "found_index": "https://docs.example.com/llms.txt",
  "type": "llms.txt",
  "content_preview": "..."
}
```

## 📖 Discovery Strategy

### Stage 1: Quick Jump
Rapid checks without running tools:
```bash
curl -I https://docs.example.com/llms.txt
curl -I https://example.com/llms.txt
```

### Stage 2: Advanced Sniffing
For complex sub-directory structures (Mintlify, etc.):
```bash
python3 sniffer.py <URL>
```

Handles:
- Mintlify documentation structures
- Breadcrumb upward probing
- Sitemap.xml extraction as fallback

## 🎯 When to Use

Use this skill when:
1. **Documentation URLs** — Link contains `/docs/`, `/api-reference/`, `/guides/`, or `platform.` subdomain
2. **"Map the Site" Requests** — "What features does this platform have?"
3. **Scraping Failures** — Standard fetch returns heavy JS or blocked content
4. **Token Efficiency** — Large documentation sets where individual scraping is too slow or expensive

## 📜 Behavioral Rules

- **High-Speed Mode** — Once `llms.txt` is found, read index links over individual HTML scraping
- **Index Summary** — Always present detected structure overview
- **Resourceful Fallback** — If `llms.txt` missing, parse `sitemap.xml`

## 🛠️ Requirements

- Python 3
- curl

No external Python dependencies required.

## 📦 Install

```bash
# Clone the repo
git clone https://github.com/JDChi/llmx-txt-sniffer.git
cd llmx-txt-sniffer

# Run
python3 sniffer.py <URL>
```

Or install via [ClawHub](https://clawhub.com/skills/llms-txt-sniffer):
```bash
clawhub install llms-txt-sniffer
```

## 📄 License

MIT
