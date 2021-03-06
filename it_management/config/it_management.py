from __future__ import unicode_literals
from frappe import _


def get_data():
	return [
        {	
        "label": _("Transaksi"),
		"items":[
				{
					"type": "doctype",
					"label": "Master Brand",
					"name": "Master Brand",
					"description": _("Imput masukan barang Beacukai."),
				},
				{
					"type": "doctype",
					"label": "Master User",
					"name": "Master User",
					"description": _("Opening for a Job."),
				},
				{
					"type": "doctype",
                                        "label": "Master Vendor IT",
                                        "name": "Master Vendor IT",
                                        "description": _("Opening for a Job."),
                                },

				{
					"type": "doctype",
					"label": "Hardware Asset",
					"name": "Hardware Asset",
					"description": _("Monthly salary statement."),
				},
				{
					"type": "doctype",
					"label": "Software Instance",
					"name": "Software Instance",
					"description": _("Monthly salary statement."),
				},
 				 {
                                        "type": "doctype",
                                        "label": "IT Maintenance Cheklist",
                                        "name": "IT Maintenance Cheklist",
                                        "description": _("Monthly salary statement."),
                                },
{
                                        "type": "doctype",
                                        "label": "Incident and problem",
                                        "name": "Incident and problem",
                                        "description": _("Monthly salary statement."),
                                },


				]
		},
		{
        "label": _("Laporan"),
        "items": 
            [
				{
					"type": "report",
					"name": "Laporan Pengeluaran Barang Per Dokumen Pabean",
					"doctype": "Pengeluaran Barang",
					"description": _("Employee records."),
					"is_query_report": True,
				},

				
			]
        },
	]
