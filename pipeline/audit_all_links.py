import os
import re

def audit_links():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    broken_links = []
    total_links = 0
    checked_files = 0

    for root, dirs, files in os.walk(base_dir):
        # Skip node_modules or .git if any
        if any(skip in root for skip in [".git", "node_modules"]):
            continue
        for f in files:
            if f.endswith('.html'):
                checked_files += 1
                fpath = os.path.join(root, f)
                with open(fpath, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                
                # Find all href and src
                matches = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
                for target in matches:
                    total_links += 1
                    if target.startswith(('http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:', '#')):
                        continue
                    clean_target = target.split('?')[0].split('#')[0]
                    if not clean_target:
                        continue
                    # Handle absolute paths if any (e.g. /css/style.css)
                    if clean_target.startswith('/'):
                        target_path = os.path.normpath(os.path.join(base_dir, clean_target.lstrip('/\\')))
                    else:
                        target_path = os.path.normpath(os.path.join(root, clean_target))
                    
                    if not os.path.exists(target_path):
                        broken_links.append((os.path.relpath(fpath, base_dir), target, os.path.relpath(target_path, base_dir) if os.path.exists(os.path.dirname(target_path)) else target_path))

    print(f"Checked {checked_files} HTML files, {total_links} links.")
    print(f"Broken local links count: {len(broken_links)}")
    for src, t, resolved in broken_links:
        print(f"  IN {src}: href/src='{t}' -> NOT FOUND ({resolved})")

if __name__ == "__main__":
    audit_links()
