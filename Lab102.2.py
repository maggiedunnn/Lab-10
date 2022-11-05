names = {"Brown" : "Cody",
"Bub" : "Julia",
"Doherty" : "Catherine",
"Dunn" : "Margaret",
"Greene" : "Haley",
"Guthrie Beckstrom" : "Isabela",
"Hongell" : "Danielle",
"Hurley" : "Camryn",
"Kevin" : "Ellen",
"Kieft" : "Brenna",
"Miloserny" : "Amanda",
"Nyhuis" : "Kaylen",
"Reger" : "Cadyn",
"Rusch" : "Emily",
"Salazar" : "Britney",
"Schutz": "Julia",
"Shadid" : "Christina",
"Skrip" : "Holly",
"Sullivan" : "Anna",
"Verstraete": "Adrianne",
"Wardlow" : "Sarah"}

def count_first_names(d, name):
    total = 0
    for key in d:
        if d[key] == name:
            total += 1
    return total
