import bpy
from ..sollumz_properties import MaterialType
from typing import NamedTuple
from .. import logger
from ..tools.blenderhelper import find_bsdf_and_material_output


class CollisionMaterial(NamedTuple):
    name: str
    ui_name: str
    color: tuple[int, int, int, int]
    density: float


collisionmats = [
    # fmt: off
    CollisionMaterial("DEFAULT",                    "Default",                    (255,   0, 255, 255),  1750.0),
    CollisionMaterial("CONCRETE",                   "Concrete",                   (145, 145, 145, 255),  7850.5),
    CollisionMaterial("CONCRETE_POTHOLE",           "Concrete Pothole",           (145, 145, 145, 255),  4900.0),
    CollisionMaterial("CONCRETE_DUSTY",             "Concrete Dusty",             (145, 140, 130, 255),  7850.5),
    CollisionMaterial("TARMAC",                     "Tarmac",                     ( 90,  90,  90, 255),  6300.0),
    CollisionMaterial("TARMAC_PAINTED",             "Tarmac Painted",             ( 90,  90,  90, 255),  6300.0),
    CollisionMaterial("TARMAC_POTHOLE",             "Tarmac Pothole",             ( 70,  70,  70, 255),  4900.0),
    CollisionMaterial("RUMBLE_STRIP",               "Rumble Strip",               ( 90,  90,  90, 255),  6300.0),
    CollisionMaterial("BREEZE_BLOCK",               "Breeze Block",               (145, 145, 145, 255),  7000.0),
    CollisionMaterial("ROCK",                       "Rock",                       (185, 185, 185, 255),  7000.0),
    CollisionMaterial("ROCK_MOSSY",                 "Rock Mossy",                 (185, 185, 185, 255),  7000.0),
    CollisionMaterial("STONE",                      "Stone",                      (185, 185, 185, 255),  7000.0),
    CollisionMaterial("COBBLESTONE",                "Cobblestone",                (185, 185, 185, 255),  7000.0),
    CollisionMaterial("BRICK",                      "Brick",                      (195,  95,  30, 255),  7000.0),
    CollisionMaterial("MARBLE",                     "Marble",                     (195, 155, 145, 255),  8970.5),
    CollisionMaterial("PAVING_SLAB",                "Paving Slab",                (200, 165, 130, 255),  7000.0),
    CollisionMaterial("SANDSTONE_SOLID",            "Sandstone Solid",            (215, 195, 150, 255),  8130.5),
    CollisionMaterial("SANDSTONE_BRITTLE",          "Sandstone Brittle",          (205, 180, 120, 255),  5075.0),
    CollisionMaterial("SAND_LOOSE",                 "Sand Loose",                 (235, 220, 190, 255),  5047.0),
    CollisionMaterial("SAND_COMPACT",               "Sand Compact",               (250, 240, 220, 255),  5950.0),
    CollisionMaterial("SAND_WET",                   "Sand Wet",                   (190, 185, 165, 255),  6727.0),
    CollisionMaterial("SAND_TRACK",                 "Sand Track",                 (250, 240, 220, 255),  5775.0),
    CollisionMaterial("SAND_UNDERWATER",            "Sand Underwater",            (135, 130, 120, 255),  5775.0),
    CollisionMaterial("SAND_DRY_DEEP",              "Sand Dry Deep",              (110, 100,  85, 255),  5047.0),
    CollisionMaterial("SAND_WET_DEEP",              "Sand Wet Deep",              (110, 100,  85, 255),  6727.0),
    CollisionMaterial("ICE",                        "Ice",                        (200, 250, 255, 255),  3216.5),
    CollisionMaterial("ICE_TARMAC",                 "Ice Tarmac",                 (200, 250, 255, 255),  3216.5),
    CollisionMaterial("SNOW_LOOSE",                 "Snow Loose",                 (255, 255, 255, 255),   560.0),
    CollisionMaterial("SNOW_COMPACT",               "Snow Compact",               (255, 255, 255, 255),  1683.5),
    CollisionMaterial("SNOW_DEEP",                  "Snow Deep",                  (255, 255, 255, 255),   560.0),
    CollisionMaterial("SNOW_TARMAC",                "Snow Tarmac",                (255, 255, 255, 255),  6300.0),
    CollisionMaterial("GRAVEL_SMALL",               "Gravel Small",               (255, 255, 255, 255),  6727.0),
    CollisionMaterial("GRAVEL_LARGE",               "Gravel Large",               (255, 255, 255, 255),  5887.0),
    CollisionMaterial("GRAVEL_DEEP",                "Gravel Deep",                (255, 255, 255, 255),  6727.0),
    CollisionMaterial("GRAVEL_TRAIN_TRACK",         "Gravel Train Track",         (145, 140, 130, 255),  6727.0),
    CollisionMaterial("DIRT_TRACK",                 "Dirt Track",                 (175, 160, 140, 255),  4550.0),
    CollisionMaterial("MUD_HARD",                   "Mud Hard",                   (175, 160, 140, 255),  5327.0),
    CollisionMaterial("MUD_POTHOLE",                "Mud Pothole",                (105,  95,  75, 255),  4200.0),
    CollisionMaterial("MUD_SOFT",                   "Mud Soft",                   (105,  95,  75, 255),  6055.0),
    CollisionMaterial("MUD_UNDERWATER",             "Mud Underwater",             ( 75,  65,  50, 255),  6055.0),
    CollisionMaterial("MUD_DEEP",                   "Mud Deep",                   (105,  95,  75, 255),  6055.0),
    CollisionMaterial("MARSH",                      "Marsh",                      (105,  95,  75, 255),  6055.0),
    CollisionMaterial("MARSH_DEEP",                 "Marsh Deep",                 (105,  95,  75, 255),  6055.0),
    CollisionMaterial("SOIL",                       "Soil",                       (105,  95,  75, 255),  5047.0),
    CollisionMaterial("CLAY_HARD",                  "Clay Hard",                  (160, 160, 160, 255),  6111.0),
    CollisionMaterial("CLAY_SOFT",                  "Clay Soft",                  (160, 160, 160, 255),  3755.5),
    CollisionMaterial("GRASS_LONG",                 "Grass Long",                 (130, 205,  75, 255),  4900.0),
    CollisionMaterial("GRASS",                      "Grass",                      (130, 205,  75, 255),  5600.0),
    CollisionMaterial("GRASS_SHORT",                "Grass Short",                (130, 205,  75, 255),  5950.0),
    CollisionMaterial("HAY",                        "Hay",                        (240, 205, 125, 255),  5950.0),
    CollisionMaterial("BUSHES",                     "Bushes",                     ( 85, 160,  30, 255),   525.0),
    CollisionMaterial("TWIGS",                      "Twigs",                      (115, 100,  70, 255),   700.0),
    CollisionMaterial("LEAVES",                     "Leaves",                     ( 70, 100,  50, 255),   350.0),
    CollisionMaterial("WOODCHIPS",                  "Woodchips",                  (115, 100,  70, 255),  1820.0),
    CollisionMaterial("TREE_BARK",                  "Tree Bark",                  (115, 100,  70, 255),   840.0),
    CollisionMaterial("METAL_SOLID_SMALL",          "Metal Solid Small",          (155, 180, 190, 255), 24500.0),
    CollisionMaterial("METAL_SOLID_MEDIUM",         "Metal Solid Medium",         (155, 180, 190, 255), 28000.0),
    CollisionMaterial("METAL_SOLID_LARGE",          "Metal Solid Large",          (155, 180, 190, 255), 31500.0),
    CollisionMaterial("METAL_HOLLOW_SMALL",         "Metal Hollow Small",         (155, 180, 190, 255),  1750.0),
    CollisionMaterial("METAL_HOLLOW_MEDIUM",        "Metal Hollow Medium",        (155, 180, 190, 255),  2100.0),
    CollisionMaterial("METAL_HOLLOW_LARGE",         "Metal Hollow Large",         (155, 180, 190, 255),  2450.0),
    CollisionMaterial("METAL_CHAINLINK_SMALL",      "Metal Chainlink Small",      (155, 180, 190, 255),  3500.0),
    CollisionMaterial("METAL_CHAINLINK_LARGE",      "Metal Chainlink Large",      (155, 180, 190, 255),  3850.0),
    CollisionMaterial("METAL_CORRUGATED_IRON",      "Metal Corrugated Iron",      (155, 180, 190, 255), 21000.0),
    CollisionMaterial("METAL_GRILLE",               "Metal Grille",               (155, 180, 190, 255),  3500.0),
    CollisionMaterial("METAL_RAILING",              "Metal Railing",              (155, 180, 190, 255),  4200.0),
    CollisionMaterial("METAL_DUCT",                 "Metal Duct",                 (155, 180, 190, 255),  1750.0),
    CollisionMaterial("METAL_GARAGE_DOOR",          "Metal Garage Door",          (155, 180, 190, 255), 31500.0),
    CollisionMaterial("METAL_MANHOLE",              "Metal Manhole",              (155, 180, 190, 255), 31500.0),
    CollisionMaterial("WOOD_SOLID_SMALL",           "Wood Solid Small",           (155, 130,  95, 255),  1400.0),
    CollisionMaterial("WOOD_SOLID_MEDIUM",          "Wood Solid Medium",          (155, 130,  95, 255),  2100.0),
    CollisionMaterial("WOOD_SOLID_LARGE",           "Wood Solid Large",           (155, 130,  95, 255),  2852.5),
    CollisionMaterial("WOOD_SOLID_POLISHED",        "Wood Solid Polished",        (155, 130,  95, 255),  2800.0),
    CollisionMaterial("WOOD_FLOOR_DUSTY",           "Wood Floor Dusty",           (165, 145, 110, 255),  2100.0),
    CollisionMaterial("WOOD_HOLLOW_SMALL",          "Wood Hollow Small",          (170, 150, 125, 255),   350.0),
    CollisionMaterial("WOOD_HOLLOW_MEDIUM",         "Wood Hollow Medium",         (170, 150, 125, 255),   700.0),
    CollisionMaterial("WOOD_HOLLOW_LARGE",          "Wood Hollow Large",          (170, 150, 125, 255),  1050.0),
    CollisionMaterial("WOOD_CHIPBOARD",             "Wood Chipboard",             (170, 150, 125, 255),   595.0),
    CollisionMaterial("WOOD_OLD_CREAKY",            "Wood Old Creaky",            (155, 130,  95, 255),  2100.0),
    CollisionMaterial("WOOD_HIGH_DENSITY",          "Wood High Density",          (155, 130,  95, 255), 21000.0),
    CollisionMaterial("WOOD_LATTICE",               "Wood Lattice",               (155, 130,  95, 255),  1400.0),
    CollisionMaterial("CERAMIC",                    "Ceramic",                    (220, 210, 195, 255),  9695.0),
    CollisionMaterial("ROOF_TILE",                  "Roof Tile",                  (220, 210, 195, 255),  7000.0),
    CollisionMaterial("ROOF_FELT",                  "Roof Felt",                  (165, 145, 110, 255),  5250.0),
    CollisionMaterial("FIBREGLASS",                 "Fibreglass",                 (255, 250, 210, 255),  1750.0),
    CollisionMaterial("TARPAULIN",                  "Tarpaulin",                  (255, 250, 210, 255),  2800.0),
    CollisionMaterial("PLASTIC",                    "Plastic",                    (255, 250, 210, 255),  3500.0),
    CollisionMaterial("PLASTIC_HOLLOW",             "Plastic Hollow",             (240, 230, 185, 255),   875.0),
    CollisionMaterial("PLASTIC_HIGH_DENSITY",       "Plastic High Density",       (255, 250, 210, 255), 21000.0),
    CollisionMaterial("PLASTIC_CLEAR",              "Plastic Clear",              (255, 250, 210, 255),  3500.0),
    CollisionMaterial("PLASTIC_HOLLOW_CLEAR",       "Plastic Hollow Clear",       (240, 230, 185, 255),   875.0),
    CollisionMaterial("PLASTIC_HIGH_DENSITY_CLEAR", "Plastic High Density Clear", (255, 250, 210, 255), 21000.0),
    CollisionMaterial("FIBREGLASS_HOLLOW",          "Fibreglass Hollow",          (240, 230, 185, 255),   126.0),
    CollisionMaterial("RUBBER",                     "Rubber",                     ( 70,  70,  70, 255),  4200.0),
    CollisionMaterial("RUBBER_HOLLOW",              "Rubber Hollow",              ( 70,  70,  70, 255),   875.0),
    CollisionMaterial("LINOLEUM",                   "Linoleum",                   (205, 150,  80, 255),  1925.0),
    CollisionMaterial("LAMINATE",                   "Laminate",                   (170, 150, 125, 255),  2800.0),
    CollisionMaterial("CARPET_SOLID",               "Carpet Solid",               (250, 100, 100, 255),  1050.0),
    CollisionMaterial("CARPET_SOLID_DUSTY",         "Carpet Solid Dusty",         (255, 135, 135, 255),  1050.0),
    CollisionMaterial("CARPET_FLOORBOARD",          "Carpet Floorboard",          (250, 100, 100, 255),  1750.0),
    CollisionMaterial("CLOTH",                      "Cloth",                      (250, 100, 100, 255),   875.0),
    CollisionMaterial("PLASTER_SOLID",              "Plaster Solid",              (145, 145, 145, 255),  2971.5),
    CollisionMaterial("PLASTER_BRITTLE",            "Plaster Brittle",            (225, 225, 225, 255),  2971.5),
    CollisionMaterial("CARDBOARD_SHEET",            "Cardboard Sheet",            (120, 115,  95, 255),   400.0),
    CollisionMaterial("CARDBOARD_BOX",              "Cardboard Box",              (120, 115,  95, 255),   200.0),
    CollisionMaterial("PAPER",                      "Paper",                      (230, 225, 220, 255),  4203.5),
    CollisionMaterial("FOAM",                       "Foam",                       (230, 235, 240, 255),   175.0),
    CollisionMaterial("FEATHER_PILLOW",             "Feather Pillow",             (230, 230, 230, 255),   192.5),
    CollisionMaterial("POLYSTYRENE",                "Polystyrene",                (255, 250, 210, 255),   157.5),
    CollisionMaterial("LEATHER",                    "Leather",                    (250, 100, 100, 255),  3307.5),
    CollisionMaterial("TVSCREEN",                   "Tvscreen",                   (115, 125, 125, 255),  9026.5),
    CollisionMaterial("SLATTED_BLINDS",             "Slatted Blinds",             (255, 250, 210, 255),  8750.0),
    CollisionMaterial("GLASS_SHOOT_THROUGH",        "Glass Shoot Through",        (205, 240, 255, 255),  8750.0),
    CollisionMaterial("GLASS_BULLETPROOF",          "Glass Bulletproof",          (115, 125, 125, 255),  8750.0),
    CollisionMaterial("GLASS_OPAQUE",               "Glass Opaque",               (205, 240, 255, 255),  8750.0),
    CollisionMaterial("PERSPEX",                    "Perspex",                    (205, 240, 255, 255),  4130.0),
    CollisionMaterial("CAR_METAL",                  "Car Metal",                  (255, 255, 255, 255),  3363.5),
    CollisionMaterial("CAR_PLASTIC",                "Car Plastic",                (255, 255, 255, 255),  1750.0),
    CollisionMaterial("CAR_SOFTTOP",                "Car Softtop",                (250, 100, 100, 255),  1750.0),
    CollisionMaterial("CAR_SOFTTOP_CLEAR",          "Car Softtop Clear",          (250, 100, 100, 255),  1750.0),
    CollisionMaterial("CAR_GLASS_WEAK",             "Car Glass Weak",             (210, 245, 245, 255),  8750.0),
    CollisionMaterial("CAR_GLASS_MEDIUM",           "Car Glass Medium",           (210, 245, 245, 255),  8750.0),
    CollisionMaterial("CAR_GLASS_STRONG",           "Car Glass Strong",           (210, 245, 245, 255),  8750.0),
    CollisionMaterial("CAR_GLASS_BULLETPROOF",      "Car Glass Bulletproof",      (210, 245, 245, 255),  8750.0),
    CollisionMaterial("CAR_GLASS_OPAQUE",           "Car Glass Opaque",           (210, 245, 245, 255),  8750.0),
    CollisionMaterial("WATER",                      "Water",                      ( 55, 145, 230, 255),  3573.5),
    CollisionMaterial("BLOOD",                      "Blood",                      (205,   5,   5, 255),  3573.5),
    CollisionMaterial("OIL",                        "Oil",                        ( 80,  65,  65, 255),  3573.5),
    CollisionMaterial("PETROL",                     "Petrol",                     ( 70, 100, 120, 255),  3573.5),
    CollisionMaterial("FRESH_MEAT",                 "Fresh Meat",                 (255,  55,  20, 255),  4200.0),
    CollisionMaterial("DRIED_MEAT",                 "Dried Meat",                 (185, 100,  85, 255),  4200.0),
    CollisionMaterial("EMISSIVE_GLASS",             "Emissive Glass",             (205, 240, 255, 255),  8750.0),
    CollisionMaterial("EMISSIVE_PLASTIC",           "Emissive Plastic",           (255, 250, 210, 255),  3500.0),
    CollisionMaterial("VFX_METAL_ELECTRIFIED",      "Vfx Metal Electrified",      (155, 180, 190, 255),  2100.0),
    CollisionMaterial("VFX_METAL_WATER_TOWER",      "Vfx Metal Water Tower",      (155, 180, 190, 255),  2100.0),
    CollisionMaterial("VFX_METAL_STEAM",            "Vfx Metal Steam",            (155, 180, 190, 255),  2100.0),
    CollisionMaterial("VFX_METAL_FLAME",            "Vfx Metal Flame",            (155, 180, 190, 255),  2100.0),
    CollisionMaterial("PHYS_NO_FRICTION",           "Phys No Friction",           (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_GOLF_BALL",             "Phys Golf Ball",             (  0,   0,   0, 255),   577.5),
    CollisionMaterial("PHYS_TENNIS_BALL",           "Phys Tennis Ball",           (  0,   0,   0, 255),   350.0),
    CollisionMaterial("PHYS_CASTER",                "Phys Caster",                (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_CASTER_RUSTY",          "Phys Caster Rusty",          (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_CAR_VOID",              "Phys Car Void",              (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_PED_CAPSULE",           "Phys Ped Capsule",           (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_ELECTRIC_FENCE",        "Phys Electric Fence",        (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_ELECTRIC_METAL",        "Phys Electric Metal",        (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_BARBED_WIRE",           "Phys Barbed Wire",           (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("PHYS_POOLTABLE_SURFACE",     "Phys Pooltable Surface",     (155, 130,  95, 255),  8750.0),
    CollisionMaterial("PHYS_POOLTABLE_CUSHION",     "Phys Pooltable Cushion",     (155, 130,  95, 255),  8750.0),
    CollisionMaterial("PHYS_POOLTABLE_BALL",        "Phys Pooltable Ball",        (255, 250, 210, 255),  8750.0),
    CollisionMaterial("BUTTOCKS",                   "Buttocks",                   (  0,   0,   0, 255),   350.0),
    CollisionMaterial("THIGH_LEFT",                 "Thigh Left",                 (  0,   0,   0, 255),   350.0),
    CollisionMaterial("SHIN_LEFT",                  "Shin Left",                  (  0,   0,   0, 255),   350.0),
    CollisionMaterial("FOOT_LEFT",                  "Foot Left",                  (  0,   0,   0, 255),   350.0),
    CollisionMaterial("THIGH_RIGHT",                "Thigh Right",                (  0,   0,   0, 255),   350.0),
    CollisionMaterial("SHIN_RIGHT",                 "Shin Right",                 (  0,   0,   0, 255),   350.0),
    CollisionMaterial("FOOT_RIGHT",                 "Foot Right",                 (  0,   0,   0, 255),   350.0),
    CollisionMaterial("SPINE0",                     "Spine0",                     (  0,   0,   0, 255),   350.0),
    CollisionMaterial("SPINE1",                     "Spine1",                     (  0,   0,   0, 255),   350.0),
    CollisionMaterial("SPINE2",                     "Spine2",                     (  0,   0,   0, 255),   350.0),
    CollisionMaterial("SPINE3",                     "Spine3",                     (  0,   0,   0, 255),   350.0),
    CollisionMaterial("CLAVICLE_LEFT",              "Clavicle Left",              (  0,   0,   0, 255),   350.0),
    CollisionMaterial("UPPER_ARM_LEFT",             "Upper Arm Left",             (  0,   0,   0, 255),   350.0),
    CollisionMaterial("LOWER_ARM_LEFT",             "Lower Arm Left",             (  0,   0,   0, 255),   350.0),
    CollisionMaterial("HAND_LEFT",                  "Hand Left",                  (  0,   0,   0, 255),   350.0),
    CollisionMaterial("CLAVICLE_RIGHT",             "Clavicle Right",             (  0,   0,   0, 255),   350.0),
    CollisionMaterial("UPPER_ARM_RIGHT",            "Upper Arm Right",            (  0,   0,   0, 255),   350.0),
    CollisionMaterial("LOWER_ARM_RIGHT",            "Lower Arm Right",            (  0,   0,   0, 255),   350.0),
    CollisionMaterial("HAND_RIGHT",                 "Hand Right",                 (  0,   0,   0, 255),   350.0),
    CollisionMaterial("NECK",                       "Neck",                       (  0,   0,   0, 255),   350.0),
    CollisionMaterial("HEAD",                       "Head",                       (  0,   0,   0, 255),   350.0),
    CollisionMaterial("ANIMAL_DEFAULT",             "Animal Default",             (  0,   0,   0, 255),   350.0),
    CollisionMaterial("CAR_ENGINE",                 "Car Engine",                 (255, 255, 255, 255),  3363.5),
    CollisionMaterial("PUDDLE",                     "Puddle",                     ( 55, 145, 230, 255),  3573.5),
    CollisionMaterial("CONCRETE_PAVEMENT",          "Concrete Pavement",          (145, 145, 145, 255),  7850.5),
    CollisionMaterial("BRICK_PAVEMENT",             "Brick Pavement",             (195,  95,  30, 255),  7000.0),
    CollisionMaterial("PHYS_DYNAMIC_COVER_BOUND",   "Phys Dynamic Cover Bound",   (  0,   0,   0, 255),  1750.0),
    CollisionMaterial("VFX_WOOD_BEER_BARREL",       "Vfx Wood Beer Barrel",       (155, 130,  95, 255),  1400.0),
    CollisionMaterial("WOOD_HIGH_FRICTION",         "Wood High Friction",         (155, 130,  95, 255),  1400.0),
    CollisionMaterial("ROCK_NOINST",                "Rock Noinst",                (185, 185, 185, 255),  7000.0),
    CollisionMaterial("BUSHES_NOINST",              "Bushes Noinst",              ( 85, 160,  30, 255),   525.0),
    CollisionMaterial("METAL_SOLID_ROAD_SURFACE",   "Metal Solid Road Surface",   (155, 180, 190, 255), 28000.0),
    CollisionMaterial("STUNT_RAMP_SURFACE",         "Stunt Ramp Surface",         (155, 180, 190, 255), 28000.0),
    CollisionMaterial("TEMP_01",                    "Temp 01",                    (255,   0, 255, 255),  5950.0),
    CollisionMaterial("TEMP_02",                    "Temp 02",                    (255,   0, 255, 255),  5950.0),
    # fmt: on
]


def create_collision_material_from_index(index: int):
    matinfo = collisionmats[0]

    try:
        matinfo = collisionmats[index]
    except IndexError:
        logger.warning(f"Invalid material index '{index}'! Setting to default...")

    mat = bpy.data.materials.new(matinfo.name)
    mat.sollum_type = MaterialType.COLLISION
    mat.collision_properties.collision_index = index
    mat.use_nodes = True
    bsdf, _ = find_bsdf_and_material_output(mat)
    r = matinfo.color[0] / 255
    g = matinfo.color[1] / 255
    b = matinfo.color[2] / 255
    bsdf.inputs[0].default_value = (r, g, b, 1)

    return mat
