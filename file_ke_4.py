import json


class LatihanKeTiga:
	def on_get(self, req, resp):

		kelompok = {"buah": {"nama": "Pisang",
			    	    "warna": "kuning"}, 
			    "hewan": {"nama": "cacing",
				    "klas": "molusca"}}

		json.dumps(kelompok)
