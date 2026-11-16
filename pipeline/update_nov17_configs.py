# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-11-17 edition."""

import os

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_EDITION = {
    "2026-11-17": {
        "dateStr": "Tuesday November 17 2026",
        "editionLabel": "2026年11月17日 (火) 号 【本日・最新・全12記事】",
        "tagline": "特集：豪米AI供給網協定とQuad・国連AI気候誤情報警告・米DC排出量デンマーク並・新ボンドにロバート・パティンソン・EUルワンダ送還ハブ",
        "topLeadSlug": "albanese-treads-tightrope-in-upcoming-trump-meeting-wanting-indo-pacific-engagement-and-end-to-iran-and-ukraine-wars",
        "subLeadSlugs": [
            "ai-models-fallible-denial-climate-science-unesco-cop31",
            "datacenter-emissions-study",
            "new-james-bond-announced-and-the-names-pattinson-robert-pattinson",
        ],
        "leftDispatches": [
            "eu-states-immigration-return-hubs-rwanda",
            "microsoft-global-outage-cause",
            "home-insurance-premiums-inflation-unaffordable-australia-natural-disasters",
            "europes-wadden-sea-is-a-natural-wonder-so-why-might-it-join-the-world-heritage-in-danger-list",
        ],
        "rightDigestSlugs": [
            "ministers-to-end-palantir-contract-nhs-england-2029",
            "uk-blood-services-urgent-appeal-donations-winter",
            "near-philistine-fury-shakespeare-institute-plan-leave-stratford-upon-avon-edgbaston",
            "grammy-nominations-2027-female-artists",
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

    if '"2026-11-17":' in text:
        print(f"Skipping {filename}: 2026-11-17 already present.")
        return

    assert anchor in text, f"Anchor not found in {filename}"
    new_block = format_editions_block(indent)
    text = text.replace(anchor, f"{anchor}\n{new_block}", 1)
    text = text.replace(
        '"2026年11月16日 (月) 号 【本日・最新・全12記事】"',
        '"2026年11月16日 (月) 号 【全12記事・アーカイブ】"',
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Updated {filename} successfully.")


if __name__ == "__main__":
    patch_file("build_portal_data_js.py", "    editions_dict = {", 8)
    patch_file("build_junior_data_js.py", "EDITIONS_DATA = {", 4)
