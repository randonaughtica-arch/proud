# Proud

A Fabric mod for Minecraft **26.2** with **377 flags** you can fly, hold and wear.

| Category | Flags |
|---|---|
| Pride | 23 (Rainbow, Progress, Transgender, Bisexual, Lesbian, Nonbinary, Intersex and more) |
| Indigenous Peoples | 10 (Australian Aboriginal, Torres Strait Islander, Tino Rangatiratanga, Sámi, Wiphala, Métis, Haudenosaunee and more) |
| Peoples & Nations | 8 (Romani, Kurdistan, Breton, Acadian, Pan-African and more) |
| Countries | 198 (every UN member state, plus Vatican City, Palestine, Kosovo, Taiwan and the European Union) |
| US States & Territories | 56 (all 50 states, DC, Puerto Rico, Guam, the US Virgin Islands, American Samoa and the Northern Mariana Islands) |
| Canadian Provinces & Territories | 13 |
| Australian States & Territories | 8 |
| UK Nations & Crown Dependencies | 12 (England, Scotland, Wales, Cornwall, the Isle of Man and more) |
| German States | 16 |
| Spanish Autonomous Communities | 17 (Catalonia, the Basque Country, Galicia and more) |
| Other Regions | 16 (Greenland, the Faroe Islands, Sardinia, Flanders and more) |

## Using flags

- **Place** a flag to plant it on a pole. The flag faces you.
- **Wear** a flag by putting it in your helmet slot.
- **Hold** a flag to carry it in your hand.
- **Get** flags in survival by crafting a **Blank Flag** (3 sticks down the left, 4 wool to the right), then picking any flag at a **stonecutter**. Any flag can be turned into any other flag at a stonecutter.

Each category has its own creative tab.

## About the artwork

Every flag is drawn by `tools/generate.py` from a small geometric description in `tools/flags_*.py`. The final textures are 48x32 pixels, so detailed coats of arms, seals and emblems are simplified, and very detailed flags will look approximate.

The Australian Aboriginal Flag was designed by Harold Thomas, and the Torres Strait Islander Flag by the late Bernard Namok. Both are official flags of Australia. If you plan to distribute this mod commercially, check the current usage guidelines for these and other Indigenous flags with their custodians first.

Spotted a flag that's wrong, or one that's missing? Edit or add it in `tools/flags_*.py`, then rerun the generator.

## Building

Requires JDK 25 and Pillow (`pip install pillow`).

```sh
python3 tools/generate.py   # regenerate flags after editing tools/flags_*.py
./gradlew build             # jar goes to build/libs/
```

## License

MIT
