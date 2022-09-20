def setup_defaults(_) -> dict:
    return {
        "mill": {
            "fast_move_z": {
                "default": 5.0,
                "type": "float",
                "min": 0.0,
                "max": 999.0,
                "title": _("Fast-Move Z"),
                "tooltip": _("the Z-Position for fast moves"),
            },
            "G64": {
                "default": 0.020000,
                "type": "float",
                "min": 0.0,
                "max": 0.1,
                "title": _("G64-Value"),
                "tooltip": _("value for the G64 command"),
            },
            "depth": {
                "default": -9.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Depth"),
                "tooltip": _("the end depth for milling"),
            },
            "step": {
                "default": -9.0,
                "type": "float",
                "min": -999.0,
                "max": 0.0,
                "per_object": True,
                "title": _("Step"),
                "tooltip": _("the maximum depth in one move"),
            },
            "active": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("Active"),
                "tooltip": _("enable/disable this object"),
            },
            "helix_mode": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Helix"),
                "tooltip": _("Helix"),
            },
            "reverse": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Reverse"),
                "tooltip": _("Reverse"),
            },
            "back_home": {
                "default": True,
                "type": "bool",
                "title": _("Back-Home"),
                "tooltip": _("move tool back to Zero-Possition after milling"),
            },
            "small_circles": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Small-Circles"),
                "tooltip": _("milling small circles even if the tool is bigger"),
            },
            "overcut": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Overcut"),
                "tooltip": _("Overcuting edges"),
            },
            "offset": {
                "default": "auto",
                "type": "select",
                "per_object": True,
                "options": (
                    ("auto", _("auto")),
                    ("inside", _("inside")),
                    ("outside", _("outside")),
                    ("none", _("none")),
                ),
                "title": _("Offset"),
                "tooltip": _("tool offset"),
            },
        },
        "tool": {
            "rate_h": {
                "default": 1000,
                "type": "int",
                "min": 1,
                "max": 10000,
                "title": _("Feed-Rate(Horizontal)"),
                "tooltip": _("the Horizotal Feetrate"),
            },
            "rate_v": {
                "default": 100,
                "type": "int",
                "min": 1,
                "max": 10000,
                "title": _("Feed-Rate(Vertical)"),
                "tooltip": _("the Vertical Feetrate"),
            },
            "number": {
                "default": 1,
                "type": "int",
                "min": 1,
                "max": 99,
                "title": _("Number"),
                "tooltip": _("setting the Tool-Number to load in gcode"),
            },
            "diameter": {
                "default": 4.0,
                "type": "float",
                "step": 0.1,
                "min": 0.0,
                "max": 999.0,
                "title": _("Diameter"),
                "tooltip": _("setting the Tool-Diameter to calculate the Offsets"),
            },
            "speed": {
                "default": 10000,
                "type": "int",
                "min": 100,
                "max": 100000,
                "title": _("Speed"),
                "tooltip": _("setting the Tool-Speed in RPM"),
            },
            "tooltable": {
                "type": "table",
                "selectable": True,
                "default": [
                    {
                        "name": "Holz-Fräser (klein)",
                        "number": 1,
                        "diameter": 2.5,
                        "lenght": 10.0,
                        "blades": 3,
                    },
                    {
                        "name": "Holz-Fräser (groß)",
                        "number": 3,
                        "diameter": 4.0,
                        "lenght": 12.0,
                        "blades": 2,
                    },
                    {
                        "name": "Alu-Fräser (groß)",
                        "number": 4,
                        "diameter": 6.0,
                        "lenght": 12.0,
                        "blades": 1,
                    },
                    {
                        "name": "Laser",
                        "number": 1,
                        "diameter": 0.1,
                        "lenght": 10.0,
                        "blades": 0,
                    },
                ],
                "columns": {
                    "name": "str",
                    "number": "int",
                    "diameter": "float",
                    "lenght": "float",
                    "blades": "int",
                },
                "column_defaults": {
                    "name": "",
                    "number": 99,
                    "diameter": 1.0,
                    "lenght": 1.0,
                    "blades": 1,
                },
                "title": _("Tools"),
                "tooltip": _("tooltable"),
            },
            "materialtable": {
                "type": "table",
                "selectable": True,
                "default": [
                    {
                        "name": "Aluminium(Langsp.)",
                        "vc": 200,
                        "fz4": 0.04,
                        "fz8": 0.05,
                        "fz12": 0.10,
                    },
                    {
                        "name": "Aluminium(Kurzsp.)",
                        "vc": 150,
                        "fz4": 0.04,
                        "fz8": 0.05,
                        "fz12": 0.10,
                    },
                    {
                        "name": "NE-Metalle",
                        "vc": 150,
                        "fz4": 0.04,
                        "fz8": 0.05,
                        "fz12": 0.10,
                    },
                    {
                        "name": "VA-Stahl",
                        "vc": 100,
                        "fz4": 0.05,
                        "fz8": 0.06,
                        "fz12": 0.07,
                    },
                    {
                        "name": "Duroplaste",
                        "vc": 125,
                        "fz4": 0.04,
                        "fz8": 0.08,
                        "fz12": 0.10,
                    },
                    {
                        "name": "Plexiglass",
                        "vc": 250,
                        "fz4": 0.1,
                        "fz8": 0.2,
                        "fz12": 0.3,
                    },
                    {"name": "GFK", "vc": 125, "fz4": 0.04, "fz8": 0.08, "fz12": 0.10},
                    {"name": "CFK", "vc": 125, "fz4": 0.04, "fz8": 0.08, "fz12": 0.10},
                    {
                        "name": "Holz",
                        "vc": 2000,
                        "fz4": 0.04,
                        "fz8": 0.08,
                        "fz12": 0.10,
                    },
                ],
                "columns": {
                    "name": "str",
                    "vc": "int",
                    "fz4": "float",
                    "fz8": "float",
                    "fz12": "float",
                },
                "column_defaults": {
                    "name": "",
                    "vc": 100,
                    "fz4": 0.05,
                    "fz8": 0.05,
                    "fz12": 0.05,
                },
                "title": _("Materials"),
                "tooltip": _("materialtable"),
            },
        },
        "workpiece": {
            "zero": {
                "default": "bottomLeft",
                "type": "select",
                "options": (
                    ("original", _("original")),
                    ("bottomLeft", _("bottomLeft")),
                    ("center", _("center")),
                    ("bottomRight", _("bottomRight")),
                    ("topLeft", _("topLeft")),
                    ("topRight", _("topRight")),
                ),
                "title": _("Zero-Position"),
                "tooltip": _("setting the Zero-Postition of the Workpiece"),
            },
            "offset_x": {
                "default": 0.0,
                "type": "float",
                "min": -100000.0,
                "max": 100000.0,
                "title": _("Offset X"),
                "tooltip": _("Offset X (G54)"),
            },
            "offset_y": {
                "default": 0.0,
                "type": "float",
                "min": -100000.0,
                "max": 100000.0,
                "title": _("Offset Y"),
                "tooltip": _("Offset Y (G54)"),
            },
            "offset_z": {
                "default": 0.0,
                "type": "float",
                "min": -100000.0,
                "max": 100000.0,
                "title": _("Offset Z"),
                "tooltip": _("Offset Z (G54)"),
            },
        },
        "pockets": {
            "active": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Pocket"),
                "tooltip": _("do pocket operation on this object"),
            },
            "zigzag": {
                "default": False,
                "type": "bool",
                "per_object": True,
                "title": _("Zickzack"),
                "tooltip": _("Zickzack"),
            },
            "islands": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("Islands"),
                "tooltip": _("keep islands"),
            },
            "insideout": {
                "default": True,
                "type": "bool",
                "per_object": True,
                "title": _("insideout"),
                "tooltip": _("from inside to out"),
            },
        },
        "tabs": {
            "active": {
                "default": True,
                "type": "bool",
                "title": _("active"),
                "tooltip": _("activate tabs"),
                "per_object": True,
            },
            "width": {
                "default": 10,
                "type": "float",
                "min": 0.1,
                "max": 20,
                "title": _("Width"),
                "tooltip": _("width of the tabs"),
                "per_object": True,
            },
            "height": {
                "default": 2,
                "type": "float",
                "min": 0.1,
                "max": 10000,
                "title": _("Height"),
                "tooltip": _("height of the tabs"),
                "per_object": True,
            },
            "type": {
                "default": "rectangle",
                "type": "select",
                "options": (
                    ("rectangle", _("rectangle")),
                    ("triangle", _("triangle")),
                ),
                "title": _("Type"),
                "tooltip": _("type of the tab"),
            },
        },
        "leads": {
            "active": {
                "default": False,
                "type": "bool",
                "title": _("activate leads"),
                "tooltip": _("activate lead-in/lead-out support"),
                "per_object": True,
            },
            "radius": {
                "default": 3.0,
                "type": "float",
                "min": 0.1,
                "max": 10000,
                "title": _("Radius"),
                "tooltip": _("radius of the leads"),
                "per_object": True,
            },
        },
        "machine": {
            "feedrate": {
                "default": 1000,
                "type": "int",
                "min": 10,
                "max": 10000,
                "title": _("Feedrate"),
                "tooltip": _("maximum feedrate while milling"),
            },
            "tool_speed": {
                "default": 15000,
                "type": "int",
                "min": 100,
                "max": 100000,
                "title": _("Tool-Speed"),
                "tooltip": _("maximum tool-speed"),
            },
            "plugin": {
                "default": "gcode_linuxcnc",
                "type": "select",
                "options": (
                    ("gcode_linuxcnc", _("gcode_linuxcnc")),
                    ("hpgl", _("hpgl")),
                ),
                "title": _("Plugin"),
                "tooltip": _("output plugin selection"),
            },
            "mode": {
                "default": "mill",
                "type": "select",
                "options": (
                    ("mill", _("mode")),
                    ("laser", _("laser")),
                    ("laser_z", _("laser+z")),
                ),
                "title": _("Tool-Mode"),
                "tooltip": _("Tool-Mode"),
            },
            "unit": {
                "default": "mm",
                "type": "select",
                "options": (
                    ("mm", _("mm")),
                    ("inch", _("inch")),
                ),
                "title": _("Unit"),
                "tooltip": _("Unit of the machine"),
            },
            "g54": {
                "default": False,
                "type": "bool",
                "title": _("machine supports g54"),
                "tooltip": _("machine supports g54"),
            },
            "comments": {
                "default": True,
                "type": "bool",
                "title": _("Comments in output"),
                "tooltip": _("add comments to output"),
            },
            "postcommand": {
                "default": "",
                "type": "str",
                "title": _("Post-Command"),
                "tooltip": _("Post-Command to do things after save like upload to cnc"),
            },
        },
        "view": {
            "path": {
                "default": "simple",
                "type": "select",
                "options": (
                    ("minimal", _("minimal")),
                    ("simple", _("simple")),
                    ("full", _("full")),
                ),
                "title": _("Path"),
                "tooltip": _("how to show the gcode path in the 3d-View"),
            },
            "ruler_show": {
                "default": True,
                "type": "bool",
                "title": _("Ruler-Show"),
                "tooltip": _("showing ruler in 3D preview"),
            },
            "grid_show": {
                "default": True,
                "type": "bool",
                "title": _("Grid-Show"),
                "tooltip": _("showing grid in 3D preview"),
            },
            "grid_size": {
                "default": 10,
                "type": "int",
                "min": 1,
                "max": 1000,
                "title": _("Grid-Size"),
                "tooltip": _("size of the grid"),
            },
            "polygon_show": {
                "default": True,
                "type": "bool",
                "title": _("Show as Polygon"),
                "tooltip": _("showing as polygon in 3D preview"),
            },
            "object_ids": {
                "default": True,
                "type": "bool",
                "title": _("Show Object-ID's"),
                "tooltip": _("shows id of each object"),
            },
            "arcs": {
                "default": True,
                "type": "bool",
                "title": _("arcs"),
                "tooltip": _("draw arcs / Interpolation"),
            },
            "3d_show": {
                "default": False,
                "type": "bool",
                "title": _("Show inputfile in 3d"),
                "tooltip": _("Show inputfile in 3d if possible"),
            },
            "color": {
                "default": (0.5, 0.5, 0.5),
                "type": "color",
                "title": _("color"),
                "tooltip": _("color of the workpeace in 3d view"),
            },
            "alpha": {
                "default": 0.6,
                "type": "float",
                "step": 0.1,
                "decimals": 1,
                "min": 0,
                "max": 1.0,
                "title": _("transparency"),
                "tooltip": _("transparency of the workpeace in 3d view"),
            },
        },
    }
