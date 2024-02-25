# Copyright 202 Navarmedia - Miguel Subiran
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Contratos Electricidad y Gas - CRM",
    "version": "1.0.0",
    "category": "Contratos Electricidad",
    "licence": "AGPL-3",
    "author": "Navarmedia, Odoo Community Association (OCA)",
    "website": "https://github.cm/OCA/electricity_contract",
    "depends": ["base", "account"],
    "development_status": "pruebas",
    "data": [
        'security/ir.model.access.csv',
        'views/electricity_contract_menu.xml',
        'views/contract_views.xml',
    ],
}