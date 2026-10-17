#!/usr/bin/env python3
"""Generates every flag's textures, models, item definitions, lang, loot, recipes, tags and Java list.

Flags are defined in tools/flags_*.py. Run from anywhere:  python3 tools/generate.py   (requires Pillow)
Pass --sheet <path> to also write a contact sheet of every flag for review.
"""
import json
import shutil
import sys
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))

import flags_pride_peoples  # noqa: E402,F401  (registers flags)
import flags_countries  # noqa: E402,F401
import flags_regions  # noqa: E402,F401
from canvas import Canvas  # noqa: E402
from registry import CATEGORIES, FLAGS  # noqa: E402

MOD_ID = "proud"
ROOT = Path(__file__).resolve().parent.parent
RES = ROOT / "src" / "main" / "resources"
ASSETS = RES / "assets" / MOD_ID
DATA = RES / "data" / MOD_ID
JAVA_OUT = ROOT / "src" / "main" / "java" / "com" / "proud" / "registry" / "FlagList.java"

# Countries and regions read "Flag of X"; pride and peoples' flags read "X Flag".
NAMED_AFTER = {"pride", "indigenous", "peoples"}

FLAG_MODEL = {
    "textures": {"particle": "#flag", "pole": "minecraft:block/stripped_birch_log"},
    "elements": [
        {"from": [7.25, 0, 7.25], "to": [8.75, 31, 8.75],
         "faces": {d: {"uv": [7, 0, 9, 16], "texture": "#pole"} for d in ("north", "south", "east", "west")}
         | {"up": {"uv": [7, 7, 9, 9], "texture": "#pole"}, "down": {"uv": [7, 7, 9, 9], "texture": "#pole"}}},
        {"from": [8.75, 18, 7.75], "to": [26.75, 30, 8.25],
         "faces": {
             "south": {"uv": [0, 0, 16, 16], "texture": "#flag"},
             "north": {"uv": [16, 0, 0, 16], "texture": "#flag"},
             "up": {"uv": [0, 0, 16, 1], "texture": "#flag"},
             "down": {"uv": [0, 15, 16, 16], "texture": "#flag"},
             "east": {"uv": [15, 0, 16, 16], "texture": "#flag"},
         }},
    ],
    "display": {
        "thirdperson_righthand": {"rotation": [0, 90, 0], "translation": [0, -2, 1], "scale": [0.45, 0.45, 0.45]},
        "thirdperson_lefthand": {"rotation": [0, 90, 0], "translation": [0, -2, 1], "scale": [0.45, 0.45, 0.45]},
        "firstperson_righthand": {"rotation": [0, 90, 0], "translation": [1, -3, 0], "scale": [0.35, 0.35, 0.35]},
        "firstperson_lefthand": {"rotation": [0, 90, 0], "translation": [1, -3, 0], "scale": [0.35, 0.35, 0.35]},
        "head": {"rotation": [0, 90, 0], "translation": [0, 9, 0], "scale": [0.55, 0.55, 0.55]},
    },
}


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rid(path: str) -> str:
    return f"{MOD_ID}:{path}"


def render(draw):
    c = Canvas()
    draw(c)
    return c.render()


def icon(texture: Image.Image) -> Image.Image:
    """A 16x16 inventory icon: the flag on a little pole."""
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(1, 16):
        img.putpixel((1, y), (226, 210, 168, 255))
        img.putpixel((2, y), (176, 156, 112, 255))
    img.putpixel((1, 0), (240, 200, 80, 255))
    img.putpixel((2, 0), (240, 200, 80, 255))
    cloth = texture.resize((13, 9), Image.LANCZOS)
    px = cloth.load()
    for y in range(9):
        for x in range(13):
            r, g, b, a = px[x, y]
            px[x, y] = (r, g, b, 255 if a >= 128 else 0)
    img.alpha_composite(cloth, (3, 1))
    return img


def item_definition(block_id):
    """Inventory, ground and item frames use the flat icon; hands and heads use the 3D flag."""
    return {"model": {
        "type": "minecraft:select",
        "property": "minecraft:display_context",
        "cases": [{"when": ["gui", "ground", "fixed"],
                   "model": {"type": "minecraft:model", "model": rid(f"item/{block_id}")}}],
        "fallback": {"type": "minecraft:model", "model": rid(f"block/{block_id}")},
    }}


def java_source(entries):
    lines = ",\n".join(f'        new FlagEntry("{fid}", "{cat}")' for fid, cat in entries)
    cats = ", ".join(f'"{c}"' for c in CATEGORIES)
    return f"""// GENERATED FILE - do not edit by hand.
// Edit tools/flags_*.py and run `python3 tools/generate.py` instead.
package com.proud.registry;

import java.util.List;

public final class FlagList {{
    /** Creative tab order. */
    public static final List<String> CATEGORIES = List.of({cats});

    public static final List<FlagEntry> FLAGS = List.of(
{lines}
    );

    public record FlagEntry(String id, String category) {{
    }}

    private FlagList() {{
    }}
}}
"""


def main():
    sheet_path = sys.argv[sys.argv.index("--sheet") + 1] if "--sheet" in sys.argv else None
    ids = [f[0] for f in FLAGS]
    assert len(ids) == len(set(ids)), "duplicate flag ids: " + str({i for i in ids if ids.count(i) > 1})

    for d in [ASSETS / "textures", ASSETS / "models", ASSETS / "items", ASSETS / "blockstates", ASSETS / "lang",
              DATA, RES / "data" / "minecraft"]:
        shutil.rmtree(d, ignore_errors=True)

    tex_block, tex_item = ASSETS / "textures" / "block", ASSETS / "textures" / "item"
    tex_block.mkdir(parents=True)
    tex_item.mkdir(parents=True)
    write_json(ASSETS / "models" / "block" / "flag_template.json", FLAG_MODEL)

    lang = {f"itemGroup.{MOD_ID}.{cat}": f"Proud: {name}" for cat, name in CATEGORIES.items()}
    lang[f"block.{MOD_ID}.blank_flag"] = "Blank Flag"
    entries, block_ids, rendered = [], [], []

    all_flags = [("blank", "Blank", None, lambda c: c.fill("#f4f4f4"))] + FLAGS
    for fid, name, cat, draw in all_flags:
        block_id = f"{fid}_flag"
        texture = render(draw)
        texture.save(tex_block / f"{block_id}.png")
        icon(texture).save(tex_item / f"{block_id}.png")
        rendered.append((name, texture))

        write_json(ASSETS / "models" / "block" / f"{block_id}.json",
                   {"parent": rid("block/flag_template"), "textures": {"flag": rid(f"block/{block_id}")}})
        write_json(ASSETS / "models" / "item" / f"{block_id}.json",
                   {"parent": "minecraft:item/generated", "textures": {"layer0": rid(f"item/{block_id}")}})
        write_json(ASSETS / "blockstates" / f"{block_id}.json", {"variants": {
            f"facing={facing}": {"model": rid(f"block/{block_id}"), **({"y": rot} if rot else {})}
            for facing, rot in (("south", 0), ("west", 90), ("north", 180), ("east", 270))}})
        write_json(ASSETS / "items" / f"{block_id}.json", item_definition(block_id))
        write_json(DATA / "loot_table" / "blocks" / f"{block_id}.json", {
            "type": "minecraft:block",
            "pools": [{"rolls": 1, "entries": [{"type": "minecraft:item", "name": rid(block_id)}],
                       "conditions": [{"condition": "minecraft:survives_explosion"}]}],
            "random_sequence": rid(f"blocks/{block_id}"),
        })
        block_ids.append(rid(block_id))
        if cat is None:
            continue
        lang[f"block.{MOD_ID}.{block_id}"] = f"{name} Flag" if cat in NAMED_AFTER else f"Flag of {name}"
        entries.append((fid, cat))
        write_json(DATA / "recipe" / f"{block_id}.json", {
            "type": "minecraft:stonecutting",
            "ingredient": f"#{MOD_ID}:flags",
            "result": {"id": rid(block_id), "count": 1},
        })

    write_json(DATA / "recipe" / "blank_flag.json", {
        "type": "minecraft:crafting_shaped",
        "category": "decorations",
        "pattern": ["SWW", "SWW", "S  "],
        "key": {"S": "minecraft:stick", "W": "#minecraft:wool"},
        "result": {"id": rid("blank_flag"), "count": 1},
    })
    write_json(DATA / "advancement" / "recipes" / "blank_flag.json", {
        "parent": "minecraft:recipes/root",
        "criteria": {
            "has_the_recipe": {"trigger": "minecraft:recipe_unlocked", "conditions": {"recipe": rid("blank_flag")}},
            "has_wool": {"trigger": "minecraft:inventory_changed",
                         "conditions": {"items": [{"items": "#minecraft:wool"}]}},
        },
        "requirements": [["has_the_recipe", "has_wool"]],
        "rewards": {"recipes": [rid("blank_flag")]},
    })
    write_json(DATA / "tags" / "item" / "flags.json", {"values": block_ids})
    write_json(RES / "data" / "minecraft" / "tags" / "block" / "mineable" / "axe.json",
               {"replace": False, "values": block_ids})
    write_json(ASSETS / "lang" / "en_us.json", lang)

    # mod icon: a 4x3 grid of flags
    pick = ["rainbow_pride", "aboriginal_australian", "torres_strait_islander", "wales", "ohio", "transgender",
            "sami", "quebec", "progress_pride", "metis", "scotland", "texas"]
    by_id = {f[0]: f for f in FLAGS}
    grid = Image.new("RGBA", (4 * 32, 3 * 32 + 16), (0, 0, 0, 0))
    for i, fid in enumerate(pick):
        tex = render(by_id[fid][3]).resize((30, 20), Image.LANCZOS)
        grid.alpha_composite(tex, ((i % 4) * 32 + 1, (i // 4) * 37 + 6))
    grid.save(ASSETS / "icon.png")

    JAVA_OUT.parent.mkdir(parents=True, exist_ok=True)
    JAVA_OUT.write_text(java_source(entries), encoding="utf-8")

    if sheet_path:
        cols, scale = 10, 3
        cell_w, cell_h = 48 * scale + 8, 32 * scale + 8
        rows = (len(rendered) + cols - 1) // cols
        sheet = Image.new("RGBA", (cols * cell_w, rows * cell_h), (90, 90, 100, 255))
        for i, (_, tex) in enumerate(rendered):
            sheet.alpha_composite(tex.resize((48 * scale, 32 * scale), Image.NEAREST),
                                  ((i % cols) * cell_w + 4, (i // cols) * cell_h + 4))
        sheet.save(sheet_path)

    counts = {cat: sum(1 for _, c in entries if c == cat) for cat in CATEGORIES}
    print(f"Generated {len(entries)} flags: {counts}")


if __name__ == "__main__":
    main()
