from pathlib import Path

RESOURCES = Path(__file__).parent / "resources"
ICON = RESOURCES / "icon"
FONT = RESOURCES / "font"
CHARACTER_MAP_RESOURCES = RESOURCES / "character_map"
MONSTER_MAP_RESOURCES = RESOURCES / "monster_map"
# SourceHanSansCN-Bold.otf 思源黑体
# SourceHanSerifCN-Bold.otf 思源宋体

MATERIALS = RESOURCES / "material"
TALENT = RESOURCES / "talent"
GACHA_IMG = RESOURCES / "splash"

DATA = Path(__file__).parent / "data"
RAW = DATA / "raw"
AVATAR_RAW = RAW / "avatar"
MATERIAL_RAW = RAW / "material"
ARTIFACT_RAW = RAW / "artifact"
WEAPON_RAW = RAW / "weapon"
MONSTER_RAW = RAW / "monster"


RESULTS = Path(__file__).parent / "results"
CHARACTER_MAP_RESULT_RAW = RESULTS / "raw" / "character_map"


# 角色
CHARACTER_MAP_RESULT = RESULTS / "character_map"
CHARACTER_MAP_RESULT.mkdir(parents=True, exist_ok=True)

# 原魔
MONSTER_MAP_RESULT = RESULTS / "monster_map"
MONSTER_MAP_RESULT.mkdir(parents=True, exist_ok=True)