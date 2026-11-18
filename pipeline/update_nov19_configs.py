# -*- coding: utf-8 -*-
"""Update build_portal_data_js.py and build_junior_data_js.py with 2026-11-19 edition."""

import os

PIPELINE_DIR = os.path.dirname(os.path.abspath(__file__))

NEW_EDITION = {
    "2026-11-19": {
        "dateStr": "Thursday November 19 2026",
        "editionLabel": "2026年11月19日 (木) 号 【本日・最新・全12記事】",
        "tagline": "特集：米中露3首脳会談社説・ボイジャー1号1光日到達・若年大腸がんと腸内毒素・ICJ判事制裁懸念・日米ポテト戦争",
        "topLeadSlug": "the-guardian-view-on-the-trump-xi-and-putin-meeting-it-may-be-a-first-but-its-not-progress",
        "subLeadSlugs": [
            "nasa-voyager-1-pale-blue-dot",
            "bacterial-toxin-e-coli-bowel-cancer-under-50s",
            "us-sanctions-icj-judges-myanmar-genocide-ruling-israel-gaza-court",
        ],
        "leftDispatches": [
            "phantom-forests-in-australian-arid-outback-used-to-create-carbon-credits-meant-to-offset-emissions-report-claims",
            "offshore-wind-farms-artificial-reef-experiment-fishing-industry",
            "social-media-ban-once-in-a-generation-study",
            "potato-war-japan-76-year-ban-american-imported-potatoes",
        ],
        "rightDigestSlugs": [
            "nhs-england-staff-snooping-patients-records",
            "cambridge-word-of-the-year-human",
            "waymo-pulls-driverless-taxis-us-freeways",
            "sam-fender-harry-styles-and-billie-eilish-to-be-youngest-glastonbury-headliners-of-21st-century",
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

    if '"2026-11-19":' in text:
        print(f"Skipping {filename}: 2026-11-19 already present.")
        return

    assert anchor in text, f"Anchor not found in {filename}"
    new_block = format_editions_block(indent)
    text = text.replace(anchor, f"{anchor}\n{new_block}", 1)
    text = text.replace(
        '"2026年11月18日 (水) 号 【本日・最新・全12記事】"',
        '"2026年11月18日 (水) 号 【全12記事・アーカイブ】"',
    )
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"Updated {filename} successfully.")


if __name__ == "__main__":
    patch_file("build_portal_data_js.py", "    editions_dict = {", 8)
    patch_file("build_junior_data_js.py", "EDITIONS_DATA = {", 4)
