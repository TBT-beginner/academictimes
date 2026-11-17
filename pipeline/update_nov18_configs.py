# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-11-18 edition."""

import os

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_EDITION = {
    "2026-11-18": {
        "dateStr": "Wednesday November 18 2026",
        "editionLabel": "2026年11月18日 (水) 号 【本日・最新・全12記事】",
        "tagline": "特集：米「麻疹排除国」認定喪失・露サウジ豪CO2輸出トップ3・英俳優AIデジタル複製権利合意・フアン氏米議会証言・極渦反転と寒波",
        "topLeadSlug": "us-measles-outbreak-elimination-status",
        "subLeadSlugs": [
            "russia-saudi-arabia-and-australia-named-as-biggest-co2-exporters-in-history",
            "actors-uk-rights-digital-replicas-ai-protections",
            "jensen-huang-testify-congress-nvidia-affair-spy",
        ],
        "leftDispatches": [
            "polar-vortex-flipped-uk-snow-explainer",
            "the-guardian-view-on-climate-debt-a-vicious-cycle-the-world-must-break-at-cop31",
            "australia-gender-pay-gap-falls-below-20-percent-for-first-time",
            "uk-unemployment-wage-growth-milburn-report",
        ],
        "rightDigestSlugs": [
            "paul-kelly-albanese-ai-copyright-protections-creatives-campaign",
            "birmingham-university-shakespeare-institute-stratford-upon-avon",
            "would-more-hands-on-dads-create-a-more-peaceful-world-this-pioneering-scientist-thinks-so",
            "tiger-woods-return-hero-world-challenge-golf",
        ],
    }
}


def format_editions_block(indent: int) -> str:
    pad = " " * indent
    pad1 = " " * (indent + 4)
    pad2 = " " * (indent + 8)
    lines = []
    for date_key, cfg in NEW_EDITION.items():
        lines.append(f'{pad}"{date_key}": {{')
        lines.append(f'{pad1}"dateStr": "{cfg["dateStr"]}",')
        lines.append(f'{pad1}"editionLabel": "{cfg["editionLabel"]}",')
        lines.append(f'{pad1}"tagline": "{cfg["tagline"]}",')
        lines.append(f'{pad1}"topLeadSlug": "{cfg["topLeadSlug"]}",')
        for list_key in ["subLeadSlugs", "leftDispatches", "rightDigestSlugs"]:
            lines.append(f'{pad1}"{list_key}": [')
            items = cfg[list_key]
            for idx, slug in enumerate(items):
                comma = "," if idx < len(items) - 1 else ""
                lines.append(f'{pad2}"{slug}"{comma}')
            trailing = "," if list_key != "rightDigestSlugs" else ""
            lines.append(f'{pad1}]{trailing}')
        lines.append(f'{pad}}},')
    return "\n".join(lines)


def patch_file(filename: str, anchor: str, indent: int):
    path = os.path.join(PIPELINE_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    if '"2026-11-18":' in text:
        print(f"Skipping {filename}: 2026-11-18 already present.")
        return

    assert anchor in text, f"Anchor not found in {filename}"
    new_block = format_editions_block(indent)
    text = text.replace(anchor, f"{anchor}\n{new_block}", 1)
    text = text.replace(
        '"2026年11月17日 (火) 号 【本日・最新・全12記事】"',
        '"2026年11月17日 (火) 号 【全12記事・アーカイブ】"',
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Updated {filename} successfully.")


if __name__ == "__main__":
    patch_file("build_portal_data_js.py", "    editions_dict = {", 8)
    patch_file("build_junior_data_js.py", "EDITIONS_DATA = {", 4)
