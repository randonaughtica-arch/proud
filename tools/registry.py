"""Collects flag definitions from the flags_*.py modules."""

CATEGORIES = {
    "pride": "Pride",
    "indigenous": "Indigenous Peoples",
    "peoples": "Peoples & Nations",
    "countries": "Countries",
    "us_states": "US States & Territories",
    "canada": "Canadian Provinces & Territories",
    "australia": "Australian States & Territories",
    "uk": "UK Nations & Crown Dependencies",
    "germany": "German States",
    "spain": "Spanish Autonomous Communities",
    "regions": "Other Regions",
}

FLAGS = []


def flag(flag_id, name, category):
    assert category in CATEGORIES, category

    def register(draw):
        FLAGS.append((flag_id, name, category, draw))
        return draw

    return register
