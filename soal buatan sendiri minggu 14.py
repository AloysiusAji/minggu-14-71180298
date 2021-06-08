# Aloysius Gonzaga Ardhian Krisna Aji
# 71180298

# claude adalah orang yang senggang waktu, karena bosan ia membuat program pengambilan angka awal menggunakan regex,
# tetapi ia nampak kesulitan, sebagai temannya yang baik kamu wajib membantunya

# input : 555. lorem ipsum

# output: 555

import re
def angkaDepan(string):
    patt = re.compile(r"\d+")
    rest = patt.match(string)
    if rest:
        return rest.group()
    return "Tidak ada"
print(angkaDepan("555 lorem ipsum"))
