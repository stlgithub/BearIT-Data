# Pop-Up Joulumyymälä -dataprojekti - [in English](README_eng.md)

## Sisällysluettelo

1. [Ryhmän Jäsenet](#ryhmän_jäsenet)
2. [Projektin Yleiskatsaus](#projektin_yleiskatsaus)
   - [Tiivistelmä](#tiivistelmä)
   - [Työskentelytavat ja Teknologiat](#työskentelytavat_ja_teknologiat)
   - [Suunnittelu](#suunnittelu)
   - [Sprint 1](#sprint-1)
   - [Sprint 2](#sprint-2)
3. [Käyttöohjeet](#käyttöohjeet)

---

## Ryhmän Jäsenet

- **Kari-Matti Sillanpää**
  - Pilvitietokannan suunnittelu ja toteutus
  - [Linkedin](https://linkedin.com/in/kari-matti-sillanpaa) / [GitHub](https://github.com/sillaka1)
- **Maarit Ahlgren**
  - Paikallisen tietokannan suunnittelu ja toteutus, PowerBI data-analyysi
  - [Linkedin](https://linkedin.com/in/maarit-a-7a20b8197) / [GitHub](https://github.com/ahlanmaa)
- **Ville Naumanen**
  - Paikallisen tietokannan suunnittelu ja toteutus, PowerBI data-analyysi
  - [Linkedin](https://linkedin.com/in/villenaumanen) / [GitHub](https://github.com/NaumVi)
- **Sami Lappalainen**
  - Scrum Master/Project Manager, Streamlit ja Nettisivu
  - [Linkedin](https://linkedin.com/in/sami-lappalainen) / [GitHub](https://github.com/stlgithub)

## Projektin Yleiskatsaus

### Tiivistelmä

BearIT:n ICT-Campissa toteutettu harjoitusprojekti, jonka tarkoituksena oli datan käsittelyn opettelu ja harjoittelu. Projektin päätavoitteena oli luoda erilaisia tietokantoja ja toteuttaa monipuolisia data-analyysejä, samalla tutustuen ketteriin kehitysmenetelmiin.

Projekti kesti neljä viikkoa, jotka oli jaettu kahteen sprinttiin. Näiden viikkojen aikana opiskeltiin myös laajemmin IT-alaan liittyviä aiheita BearIT tarjoamien kurssien kautta ja alan ammattilaisten pitämillä luennoilla.

### Työskentelytavat ja Teknologiat

Projektissa käytettiin Scrum-menetelmää projektinhallintaan, mikä auttoi hallitsemaan työskentelyä sprinttien aikana. Versiohallinta hoidettiin Githubin avulla, ja Github Projects toimi kanban-/sprint-tauluna.Tiimityöskentelyyn käytettiin Googlen työkaluja, kuten Google Meet ja Google Docs.

Paikallinen palvelin rakennettiin käyttäen MySQL:ä ja data-analyysit toteutettiin PowerBI:llä. Pilvipalvelin luotiin AWS:n avulla ja verkkopohjainen datanäkymä, sekä sen CRUD-toiminnot toteutettiin Pythonin Streamlit-kirjastoa hyödyntäen. Projektin dokumentaatiota varten koottiin myös verkkosivu, joka luotiin HTML:n ja CSS:n avulla.

### Suunnittelu

Ennen ensimmäistä Sprinttiä, luotiin projektin suunnitelma ja siihen pohjautuvat käyttäjätarinat, sekä sprint-taulu. Projektin suunnitelmana oli luoda kuvitteelliselle pop-up joulumyymälälle paikallinen tietokanta, joka kerää tietoa kanta-asiakkaista, tuotteista, tuotekategorioista ja ostotapahtumista.

Paikallisen tietokannan lisäksi myymälälle suunniteltaisiin pilvitietokanta, johon paikallinen data siirretään. Pilvitietokantaan ei kuitenkaan siirretä asiakkaiden sensitiivistä dataa, jotta tietoturva säilyisi korkealla tasolla. Data luotaisiin tekoälyä käyttäen.

Kun tietokannat valmistuvat, projektin seuraava vaihe olisi luoda datasta dashboardeja. Näiden dashboardien avulla voitiin visualisoida ja analysoida myymälän keräämää dataa. Lisäksi kehitettäisiin verkkopohjainen näkymä, joka mahdollistaisi datan analysoinnin ja esittelyn helppokäyttöisessä, sekä visuaalisesti miellyttävässä muodossa. Verkkokäyttöliittymä mahdollistaisi myös datan poiston, muokkauksen ja syötön.

Projektille luotaisiin myös oma verkkosivu, sekä muu dokumentaatio.

### Sprint 1

Ensimmäisessä sprintissä suunnitelmana oli luoda tietokannat, niiden data, sekä opiskella Sprint 2 liittyviä asioita ja projektityöskentelyn käytänteitä. Ensiksi, ne tiimin jäsenet, joille Github ja Git olivat entuudestaan tuntemattomia, opettelivat niiden käytön perusteet.

Paikallisen tietokannan suunnitteli ja loi kahden hengen tiimi, joista kumpikin otti vastuulleen kaksi taulua. Näitä tauluja testattiin huolellisesti, sisältäen datan lisäyksen, poiston ja muokkauksen. Myös taulujen väliset riippuvuudet testattiin, jotta varmistettiin tietokannan eheys ja toimivuus. Samat suunnittelu-, luonti- ja testausprosessit toteutettiin myös pilvitietokannan osalta.

Streamlitin ja Dashin käyttöä opiskelitiin ja vertailitiin datan visualisointiin. Vertailun perusteella päädyimme käyttämään Streamlitiä sen helppokäyttöisyyden ja monipuolisuuden vuoksi.

Sprintin aikana myös opiskeltiin yleisesti ottaen kaikkia yllä mainittuihin osa-alueita.

Ainoat asiat joita emme ehtineet toteuttaa ensimmäisessä sprintissä olivat sääntö, joka varmisti, että asiakkailta pyydettäessä joko sähköpostiosoite tai puhelinnumero on annettava ja toinen kenttä voi jäädä tyhjäksi. Tämän lisäksi asiakas- ja myyntitaulujen datan generointia jouduttiin myös jatkamaan seuraavassa sprintissä.

Kaiken kaikkiaan sprintti tarjosi hyvän pohjan projektin jatkolle ja auttoi tiimiä syventämään osaamistaan käytetyissä teknologioissa ja menetelmissä.

### Sprint 2

Sprint 2 aikana viimeistelimme edellisen sprintin jäljelle jääneet tehtävät. Tämän jälkeen pääasiallisena tehtävänämme oli opetella PowerBI:n käyttöä ja luoda sillä data-analyysiin tarkoitetut dashboardit käyttäen viime sprintillä luotua dataa.

Data-analyysi tehtiin kahden hengen ryhmässä. He suunnittelivat ensin, mitä dataa analysoidaan ja miksi, sekä määrittelivät, kuka analysoi mitä. Tämän jälkeen ryhmä harjoitteli PowerBI:n käyttöä ja loi dashboardit.

Pilvipuolella viimeistelimme menetelmän, jolla varmistimme, että sensitiivinen data pysyi paikallisessa tietokannassa sen sijaan, että se siirtyisi pilvitietokantaan. Lisäksi tutkittiin muita pilvitietokantaan liittyviä ominaisuuksia, kuten snapshotien luominen tietoturvan ja tiedon eheyden varmistamiseksi.

Datasta luotiin suunniteltu Streamlit-verkkokäyttöliittymä, joka pystyi näyttämään analyysit asiakas- ja myyntidatasta. Tämän käyttöliittymän avulla oli myös mahdollista lukea koko tietokannan sisältö, sekä suorittaa CRUD-toimintoja jokaiselle taululle. Lisäksi käyttöliittymästä tehtiin offline-versio, joka käyttää CSV-tiedostoja tietokantayhteyden sijaan.

Projektista luotiin myös verkkosivu, joka antaa yleiskuvauksen projektista, esittelee projektitiimin ja linkittää tarpeellisiin dokumentaatioihin, Github-repositoryyn sekä Streamlit-sovellukseen.

## Käyttöohjeet

---
