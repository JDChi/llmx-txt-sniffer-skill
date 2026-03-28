import sys
import json
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def sniff_llms_txt(url):
    parsed = urlparse(url)
    domain = f"{parsed.scheme}://{parsed.netloc}"

    # 1. Infer common doc root paths
    # Ensure URL ends with / to fix urljoin behavior
    url_with_slash = url if url.endswith('/') else url + '/'
    paths_to_try = [url_with_slash]
    path_parts = parsed.path.strip('/').split('/')
    for i in range(len(path_parts)):
        sub_path = '/' + '/'.join(path_parts[:i+1]) + '/'
        paths_to_try.append(urljoin(domain, sub_path))
        paths_to_try.append(domain + '/')

    roots = list(dict.fromkeys(paths_to_try))
    results = {"target_url": url, "found_index": None, "type": None, "content_preview": ""}

    # 2. Probe for llms.txt
    for root in roots:
        for filename in ["llms.txt", "llms-full.txt"]:
            probe_url = urljoin(root, filename)
            try:
                response = urlopen(probe_url, timeout=5)
                if response.status == 200:
                    content = response.read().decode('utf-8', errors='ignore')
                    if "# " in content or "- [" in content:
                        results["found_index"] = probe_url
                        results["type"] = "llms.txt"
                        results["content_preview"] = content[:2000]
                        return results
            except (URLError, HTTPError):
                continue

    # 3. Fallback to Sitemap
    for root in roots:
        sitemap_url = urljoin(root, "sitemap.xml")
        try:
            response = urlopen(sitemap_url, timeout=5)
            if response.status == 200:
                results["found_index"] = sitemap_url
                results["type"] = "sitemap.xml"
                results["content_preview"] = "Sitemap found."
                return results
        except (URLError, HTTPError):
            continue

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
        sys.exit(1)
    target_url = sys.argv[1]
    print(json.dumps(sniff_llms_txt(target_url), indent=2, ensure_ascii=False))
