# Kuvaus

## Tilanne tällä hetkellä

Sovellusta voi testata Herokussa: https://tsoha-vauvanhoitosovellus.herokuapp.com/ Perusversion tarjoama toiminnallisuus on toteutettu.

## Sovelluksen tarkoitus

Sovelluksen tarkoitus on kirjata vauvanhoitoa koskevia tietoja. Sovellusta voi käyttää rekisteröitynyt käyttäjä, joka voi myös antaa muille käyttäjille mahdollisuuden katsoa tai muuttaa vauvan tietoja. Lisäksi käyttäjä voi jättää kommentteja vauvanhoitoon liittyen.

## Käyttäjät

Sovelluksessa on vain yksi käyttäjärooli.

## Käyttöliittymäluonnos

Seuraavat sivut:
* Kirjautumissivu: kirjaudu tai rekisteröidy
  * -> rekisteröitymissivu
  * -> toimintosivu
* Toimintosivu: Valitse tietojen katseleminen, tietojen tallennus, oikeuksen antaminen tai uloskirjautuminen
  * -> Katseleminen
  * -> Tallentaminen
  * -> Oikeuksien antaminen
  * -> uloskirjautuminen: Kirjautumissivulle
* Katselemissivu: Kirjatut tiedot
* Tallentamissivu: Valitse tietotyyppi, lisää tiedot ja tallenna. 
* Oikeuksien antamissivu: Anna käyttäjätunnus, valitse annettavat oikeudet (tietojen katseleminen, tietojen tallentaminen, kommentin tallentaminen)

## Perusversion tarjoama toiminnallisuus

* rekisteröityminen ja sisäänkirjautuminen
* salasana
* seuraavien tietojen kirjaus vauvakohtaisesti: imetyksen ajankohta ja kesto, korvikkeen antamisen ajankohta ja määrä, kiinteän ruuan antamisen ajankohta ja määrä, vaihdettujen vaippojen määrä ja sisältö, ja painoseuranta
* tietojen katseleminen
* kommentin jättäminen
* uloskirjautuminen
* antaa muille yksittäisille käyttäjille oikeus vauvan tietojen katsomiseen, lisäämiseen tai kommentoimiseen sekä oikeuksien poistainen


## Jatkokehitysideoita

* tietojen poistaminen
* käyttäjätilin poistaminen
* tilastojen sekä visualisointien hakeminen tallennetuista tiedoista
* tietojen lähettäminen muille sähköpostitse


