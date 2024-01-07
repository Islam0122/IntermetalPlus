JAZZMIN_SETTINGS = {
    "show_sidebar": True,
    "navigation_expanded": False,
    "changeform_format": "horizontal_tabs",
    "related_modal_active": True,
    "show_ui_builder": False,
    "show_fieldsets": True,
    "theme": "default",  # или другая тема на ваш выбор
    "iconset": "fontawesome5",
    "ui_builder": {
        "theme": "default",
        "scale": "compact",
        "layout": "vertical",
        "language": "en",
        "menu": "icons",
        "topnav": {
            "order": ("object-tools", "app_list", "model_list", "recent_actions"),
            "object-tools": ("history",),
            "app_list": ("auth", "auth.Group", "appname",),
            "model_list": ("auth.User",),
            "recent_actions": ("auth.User",),
        },
        "usermenu": {
            "order": ("user", "theme", "logout",),
            "user": ("auth.User",),
            "theme": (),
            "logout": (),
        },
    },
}