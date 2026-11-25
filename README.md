# Pozitiv – web stranica

Stranica za Pozitiv (fotopozitiv.net). Izgled je složen po uzoru na bevkperovic.com: naslovnica s izmjenjivim fotografijama, mreža radova s filterima po kategorijama, stranica rada s jednom fotografijom po ekranu i info stranica.

## Kako dodati fotografije i radove

1. Otvori **app.pagescms.org** i prijavi se GitHubom.
2. Odaberi repozitorij **pozitiv**.
3. **Radovi** → otvori rad (ili *Add an entry* za novi) → kod **Fotografije** dodaj slike → **Save**.
4. Za minutu-dvije promjena je na stranici.

Savjeti:
- Prva fotografija u radu je naslovna u mreži radova.
- Fotografije izvezi za web: oko 2500 px po dužoj strani i do 1–2 MB po fotografiji. Stranica se tako brže učitava, a GitHub ima ograničenje veličine.
- **Naslovnica i info**: tekstovi, kontakt, rubrike (about, clients…) i fotografije za naslovnicu. Ako je popis fotografija za naslovnicu prazan, naslovnica sama vrti prve fotografije svih radova.

## Što je gdje

- `index.html` – izgled i ponašanje stranice
- `data/projects.json` – radovi (uređuje se kroz admin)
- `data/site.json` – naslovnica, kontakt, info rubrike (uređuje se kroz admin)
- `images/` – fotografije
- `.pages.yml` – postavke admina (Pages CMS)
