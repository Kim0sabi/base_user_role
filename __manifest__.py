# Copyright 2014 ABF OSIELL <http://osiell.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


{
    "name": "User roles",
    "version": "18.0.1.0.3",
    "category": "Tools",
    "author": "ABF OSIELL, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "development_status": "Production/Stable",
    "maintainers": ["sebalix", "jcdrubay", "novawish"],
    "website": "https://github.com/OCA/server-backend",
    "depends": ["base"],
    "data": [
        "data/ir_module_category.xml",       # categorías de módulos, opcional
        "views/role.xml",
        "views/user.xml",
        "views/group.xml",
        "wizards/create_from_user.xml",
        "wizards/wizard_groups_into_role.xml",
        "security/ir.model.access.csv",     # permisos de acceso **después** de los modelos
        "data/ir_cron.xml", 
        
    ],
    "installable": True,
}
