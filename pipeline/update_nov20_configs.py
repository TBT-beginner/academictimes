# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-11-20 edition."""

import os

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_EDITION = {
    "2026-11-20": {
        "dateStr": "Friday November 20 2026",
        "editionLabel": "2026年11月20日 (金) 号 【本日・最新・全12記事】",
        "tagline": "特集：ICJロヒンギャ・ジェノサイド認定・米中露平和宣言の盲点・IEAデータセンター排出70%増警告・重力通信実験・アンソロピック1.3兆ドルIPO",
        "topLeadSlug": "genocide-rohingya-international-court-of-justice-ruling-myanmar",
        "subLeadSlugs": [
            "china-russia-us-agree-peace-statement-no-mention-ukraine-iran-wars",
            "datacentres-to-create-70-more-carbon-emissions-by-2030-iea-report-warns",
            "scientists-communicate-using-gravity-elevator-brick-wall-bathroom-experiment",
        ],
        "leftDispatches": [
            "anthropic-public-trading-ipo",
            "potatoes-moon-base-nasa",
            "ipcc-report-delay-climate-crisis-scientist",
            "london-swiss-cottage-school-worlds-best-school-awards",
        ],
        "rightDigestSlugs": [
            "covid-inquiry-uk-report-lack-of-early-border-controls-virus-spread",
            "un-warns-misuse-security-laws-uk-palestine-action-ban",
            "abandoning-a-cat-by-haruki-murakami-review-an-intimate-meditation-on-family-and-memory",
            "welsh-cymraeg-dub-star-wars-cardiff",
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

    if '"2026-11-20":' in text:
        print(f"Skipping {filename}: 2026-11-20 already present.")
        return

    assert anchor in text, f"Anchor not found in {filename}"
    new_block = format_editions_block(indent)
    text = text.replace(anchor, f"{anchor}\n{new_block}", 1)
    text = text.replace(
        '"2026年11月19日 (木) 号 【本日・最新・全12記事】"',
        '"2026年11月19日 (木) 号 【全12記事・アーカイブ】"',
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Updated {filename} successfully.")


if __name__ == "__main__":
    patch_file("build_portal_data_js.py", "    editions_dict = {", 8)
    patch_file("build_junior_data_js.py", "EDITIONS_DATA = {", 4)
