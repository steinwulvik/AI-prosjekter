# Bank Resilience Map
## Førsteutkast til kravspesifikasjon og prosjektplan

**Versjon:** 0.10 · **Status:** MVP bygget og testet, med språkvelger · **Dato:** 6. november 2026

## 1. Kort om konseptet

Bank Resilience Map er en interaktiv demonstrator for å forstå hvordan bankens viktige tjenester avhenger av interne systemer og eksterne IT-leverandører. Brukeren kan simulere en driftsforstyrrelse og se hvilke tjenester som kan bli påvirket, hvilke avhengigheter som må undersøkes, og hvilke oppfølgingsoppgaver som bør vurderes.

Demonstratoren bruker oppdiktede banker, systemer, leverandører og hendelser. Den skal vise en arbeidsflyt og et produktkonsept, ikke gi en formell risikovurdering eller dokumentere faktisk DORA-etterlevelse.

## 2. Målbilde for sluttproduktet

Bank Resilience Map skal være et arbeidsverktøy som gir bankens ansatte et oppdatert, etterprøvbart bilde av hvordan kritiske tjenester avhenger av teknologi, interne team og eksterne leverandører. Når en forstyrrelse oppstår – eller når banken planlegger en endring – skal brukeren kunne gå fra et forretningsmessig spørsmål til en forståelig konsekvensanalyse og videre til koordinert oppfølging.

Sluttproduktet skal gi brukeren denne sammenhengende opplevelsen:

1. **Forstå utgangspunktet:** Se kritiske banktjenester, eiere, driftsstatus, gjenopprettingsmål og datadekning i en samlet oversikt.
2. **Utforske avhengigheter:** Følge en tjeneste gjennom applikasjoner, infrastruktur, dataflyt, interne team og leverandører. Hver relasjon skal ha kilde, eier og sist bekreftet dato.
3. **Vurdere endring eller hendelse:** Velge en faktisk hendelse eller planlagt endring og angi omfang, varighet, område og berørte komponenter.
4. **Se konsekvenser og usikkerhet:** Se direkte og indirekte påvirkning på tjenester, kanaler og kundereiser. Resultatet skal vise hva som støtter vurderingen, hva som er antatt, og hvor bildet er ufullstendig.
5. **Koordinere respons:** Følge opp oppgaver med ansvarlig rolle, frist og status, og føre en tidsstemplet beslutningslogg.
6. **Dokumentere og lære:** Eksportere en sporbar oppsummering og registrere forbedringstiltak etter hendelsen.

Et produksjonsprodukt skal kunne hente informasjon fra bankens autoritative kilder for tjenestekatalog, system- og ressursdata, leverandørregister, overvåking og hendelseshåndtering. Integrasjoner skal vise dataeier, oppdateringsstatus, tilgang og feilhåndtering. Manglende eller utdaterte data skal aldri se ut som et komplett risikobilde.

Dette er målbildet for et mulig sluttprodukt. Første demonstrator er et avgrenset, syntetisk uttrykk for dette målbildet; den skal ikke forveksles med et produksjonsklart produkt.

### 2.1 Offentlig CV-produkt og selvbetjent presentasjon

Sluttproduktet skal publiseres som en offentlig webapp med en stabil lenke som kan stå i CV-en. Hiring Manager skal kunne åpne lenken og forstå verdien uten at utvikleren er til stede for å demonstrere appen. Førsteinntrykket og hovedflyten må derfor fungere som en selvbetjent produktpresentasjon:

- Forklar kort hvilket bankproblem appen belyser, hvem den er laget for, og hva demonstrasjonen viser.
- Tilby en synlig «Gå til demoen»-knapp nederst på introsiden, som starter eksempelbank-flyten med syntetiske data, uten krav om konto eller personlig informasjon.
- Introsiden er en ren presentasjon av problemet, målgruppen og demoen, uten menyfaner. Demoen starter i Scenario.
- Det finnes ingen fanerekke. Hovedflyten navigeres med trinnene 1–4: Scenario, Påvirkning, Hendelsesrom og Rapport.
- Avhengighetskartet ligger i Påvirkning, med Kart som standardvisning og Liste som alternativ. Objektene i kartet kan klikkes, og detaljene vises under kartet.
- «Tjenesteoversikt» og «Om demoen» er oppslag og ligger som lenker øverst til høyre ved «Nullstill demo». Tjenesteoversikten beholdes fordi den er det eneste stedet som viser alle tjenestene i normal drift og datadekningen samlet (målbilde 1, §12).
- Sider utenfor trinnene (tjenesteoversikt, om demoen) har en lenke tilbake til flyten.
- Gi en guidet, men hoppbar start som leder brukeren gjennom scenario → påvirkning → respons → rapport.
- La brukeren nullstille scenarioet og komme tilbake til en forståelig standardvisning.
- Vis tydelig at det er en uavhengig konseptdemo, ikke et kommersielt produkt eller laget på oppdrag fra noen bank eller leverandør. Appen skal ikke nevne navngitte selskaper (se §17). Banneret øverst på alle sider sier «Demonstrasjon med syntetiske data · Uavhengig konseptdemo». Forfatter og kontaktopplysninger står nederst på «Om demoen».
- Grensesnittet er på norsk, med språkvelger for norsk og engelsk (P-16).
- Sørg for at appen er responsiv, tilgjengelig og tåler direkte åpning av lenke og oppfrisking av siden.
- Ikke samle inn besøksdata eller tilby ekte bankintegrasjoner i offentlig demo uten særskilt behov, personvernvurdering og tydelig informasjon.

Offentlig tilgjengelighet gjelder demonstratoren. Eventuelle reelle bankdata, integrasjoner, brukeradministrasjon eller interne arbeidsflyter krever separat tilgangsstyring og sikkerhetsdesign før produksjonsbruk.

### 2.2 Foreløpig white-label-merkevare

Demonstratoren bruker den fiktive banken **Morild Bank** som white-label-kunde. Bankens merkevare skal være synlig i produktgrensesnittet, mens Bank Resilience Map beskriver konseptet/produktforslaget bak løsningen. Morild Bank er oppdiktet og må ikke framstilles som en faktisk bank eller kunde av noen leverandør.

Logoen nedenfor er godkjent som foreløpig designretning. Den består av tre blågrønne bølger med samme farge, et ravgult lyspunkt og ordmerket «MORILD BANK», der «MORILD» har bølgenes blågrønne farge og «BANK» er ravgult. Den er ikke endelig merkevaregodkjent; videre endringer skal følge brukerens tilbakemelding.

![Foreløpig Morild Bank-logo](morild-bank-wordmark-color.png)

Logoressurs: [`morild-bank-wordmark-color.png`](morild-bank-wordmark-color.png).

## 3. Problem og begrunnelse

Banker driver stadig flere kritiske tjenester gjennom digitale systemer og eksterne leverandører. Det kan være krevende å få ett samlet bilde av avhengigheter, konsekvenser og gjenopprettingsarbeid når en komponent svikter. ECBs tilsynsprioriteringer peker blant annet på tredjeparts- og skyrisiko, hendelseshåndtering, cybersikkerhet, endringsstyring og svakheter i risikodata og rapportering.

Konseptet undersøker om et visuelt avhengighetskart kombinert med scenarioanalyse kan gjøre dette arbeidet mer oversiktlig. Det er en hypotese som demonstratoren skal gjøre konkret og mulig å diskutere med brukere.

Kilder:

- [ECB – Supervisory priorities 2026–28](https://www.bankingsupervision.europa.eu/framework/priorities/html/ssm.supervisory_priorities202511.en.html)
- [ECB – Supervisory priorities 2025–27](https://www.bankingsupervision.europa.eu/framework/priorities/html/ssm.supervisory_priorities202412~6f69ad032f.en.html)

## 4. Produktmål

Demonstratoren skal:

1. Gjøre avhengigheter mellom banktjenester, systemer og leverandører forståelige.
2. La brukeren velge en simulert hendelse og se mulige konsekvenser på tvers av avhengighetskjeden.
3. Samle hendelsesstatus, beslutninger, ansvar og oppgaver i én kortfattet, oversiktlig, konkret og lesbar arbeidsflate.
4. Vise hvor datagrunnlag eller dokumentasjon mangler, uten å late som usikkerhet er bekreftet risiko.
5. Være egnet til en kort, selvforklarende produktpresentasjon i en jobbsøkerprosess.

## 5. Ikke-mål for første demonstrator

Førsteutkastet skal ikke:

- kobles til reelle banker, kontoer, produksjonssystemer eller leverandør-API-er
- inneholde ekte kunde-, transaksjons-, sikkerhets- eller personopplysninger
- foreta automatisk risikoklassifisering eller hevde DORA-etterlevelse
- erstatte bankens beredskaps-, CMDB-, GRC-, overvåkings- eller hendelsessystemer
- utføre endringer, omstart eller failover i faktiske systemer

## 6. Brukere og hovedoppgaver

**Primær bruker:** Operativ risiko- eller teknologimedarbeider som undersøker en mulig driftsforstyrrelse.

**Sekundære brukere:** Beredskapsleder, tjenesteeier, leverandøransvarlig eller leder som trenger et raskt konsekvensbilde.

Hovedoppgaver:

- finne en kritisk tjeneste og forstå hva den er avhengig av
- velge en hendelse, for eksempel bortfall hos skyleverandør eller feil etter systemendring
- undersøke hvilke tjenester og kanaler som kan rammes
- følge anbefalte kontrollspørsmål og registrere beslutninger
- se hvem som har ansvar for oppfølging, og hva som gjenstår
- lage en kort rapport med scenario, antakelser, påvirkning og tiltak

## 7. Foreslått demonstratorflyt

1. Brukeren åpner introsiden og går til demoen.
2. Brukeren velger scenario: **Svikt hos leverandør** eller **Feil etter systemendring**, og hvilken leverandør eller hvilket system som feiler. Berørte land er forhåndsbestemt av leverandøren.
3. Brukeren velger alvorlighet og varighet og beregner påvirkningen.
4. Påvirkning viser sammendrag og kartet, der direkte og indirekte avhengigheter er farget etter tilstand. Påvirkningen forklares som en beregnet demonstrasjon basert på oppgitte relasjoner.
5. Brukeren åpner et objekt for å se avhengighetskjede, eier, gjenopprettingsmål og datamangler.
6. Hendelsesrommet viser status, oppgaver, beslutningslogg, konsekvenser, kontrollspørsmål og tidslinje.
7. Brukeren kan vise og skrive ut en demonstrasjonsrapport.

## 8. Krav utledet fra målbildet

Kravene nedenfor beskriver hva sluttproduktet må kunne. «Målbilde» viser hvilken del av brukeropplevelsen kravet støtter. «Demonstrator» avgrenser hva første prototype faktisk skal vise.

| ID | Sluttproduktkrav | Målbilde | Demonstratorens bevis | Prioritet |
|---|---|---|---|---|
| P-01 | Tjenester, systemer, team og leverandører skal ha synlig eier og kritikalitet | 1–2 | Syntetisk tjeneste- og avhengighetsregister | Må |
| P-02 | Avhengigheter skal kunne utforskes begge veier og vise kilde og aktualitet | 2 | Navigerbart kart med relasjonsmetadata | Må |
| P-03 | Analyse skal vise direkte og indirekte påvirkning på tjenester og kanaler | 3–4 | Forklarbar grafberegning for to scenarioer | Må |
| P-04 | Resultatet skal skille fakta fra antakelser, mangler og usikre relasjoner | 4 | Merking av syntetiske, antatte og manglende data | Må |
| P-05 | Hendelser og planlagte endringer skal kunne følges gjennom status og tidslinje | 3, 5 | Simulert hendelsesrom | Må |
| P-06 | Oppfølging skal ha ansvarlig rolle, frist, status og beslutningsgrunnlag | 5 | Oppgaver i demoen, uten ekstern arbeidsflytintegrasjon | Bør |
| P-07 | Beslutninger og endringer i vurderingen skal kunne etterprøves | 5–6 | Tidsstemplet demonstrasjonslogg | Bør |
| P-08 | Rapport skal oppsummere omfang, påvirkning, datagrunnlag, usikkerhet og tiltak | 6 | Utskrivbar rapport | Bør |
| P-09 | Data skal komme fra autoritative kilder med eierskap, tilgang og oppdateringsstatus | Sluttproduktfundament | Arkitekturkrav; ikke ekte integrasjon i demoen | Senere |
| P-10 | Tilgang til informasjon og handlinger skal styres etter rolle og minste privilegium | Alle | Ikke nødvendig i syntetisk demo; krav før produksjonsbruk | Senere |
| P-11 | Brukeren skal kunne sammenligne scenarioer og tiltak | 4, 6 | Enkel scenario-sammenligning | Kan |
| P-12 | Offentlig besøkende skal kunne forstå og fullføre hoveddemoen uten presentatør eller konto | 2.1 | Selvforklarende start og guidet scenarioflyt | Må |
| P-13 | Offentlig demo skal tydelig vise at konseptet er selvstendig, uten å nevne navngitte selskaper, og bruke bare syntetiske data | 2.1 | Synlig konsept-/syntetisk-data-merking | Må |
| P-14 | Offentlig lenke skal fungere ved direkte åpning, oppfrisking og mobilvisning | 2.1 | Publiseringsklar responsiv demonstrator | Må |
| P-15 | Besøksdata skal ikke samles inn uten nødvendig formål og synlig informasjon | 2.1 | Ingen analyse-/sporingsverktøy som standard | Må |
| P-16 | Grensesnitt og innhold skal kunne tilbys på flere språk (norsk og engelsk) | 2.1 | Språkvelger for norsk og engelsk, med all tekst i språkfiler og oversatte tekstfelt i datasettet | Bør |

### 8.1 Krav til første demonstrator

Disse kravene er utledet fra sluttproduktkravene over:

| ID | Demonstratorkrav | Knytning |
|---|---|---|
| D-01 | Bruke kun syntetiske bank-, system-, leverandør- og hendelsesdata | P-01, P-04 |
| D-02 | Vise minst 6 tjenester, 10 systemer og 4 leverandører | P-01, P-02 |
| D-03 | La brukeren følge relasjoner fra tjeneste til underliggende systemer og leverandører | P-02 |
| D-04 | Tilby scenario for leverandørsvikt og mislykket systemendring | P-03 |
| D-05 | Forklare påvirkning med relasjonssti, antakelser og datamangler | P-03, P-04 |
| D-06 | Vise hendelsesstatus, tidslinje og oppgaver samlet | P-05, P-06, P-07 |
| D-07 | Lage utskrivbar oppsummering av scenarioet | P-08 |
| D-08 | Merke alle data og beregninger som demonstrasjonsinnhold | P-04 |
| D-09 | Starte uten konto og tilby en synlig eksempelbank og scenarioflyt | P-12 |
| D-10 | Ha en kort selvforklarende introduksjon og kunne nullstille demonstrasjonen | P-12 |
| D-11 | Merke løsningen som selvstendig konsept og data som syntetiske | P-13 |
| D-12 | Unngå unødvendig innsamling av besøksdata | P-15 |
| D-13 | Vise grensesnittet på norsk og engelsk via språkvelger, med tekst samlet i språkfiler og datasettets tekstfelt strukturert per språk (`{ no: "…", en: "…" }`) | P-16 |

## 9. Funksjonelle krav

| ID | Krav | Prioritet |
|---|---|---|
| F-01 | Vise fiktive kritiske banktjenester, interne systemer og eksterne leverandører | Må |
| F-02 | Vise relasjoner som et navigerbart avhengighetskart | Må |
| F-03 | Tilby minst to scenarioer: leverandør-/skysvikt og mislykket systemendring | Må |
| F-04 | Beregne og forklare direkte og indirekte påvirkning ut fra registrerte relasjoner | Må |
| F-05 | Skille tydelig mellom bekreftede demo-inputs, antakelser og manglende informasjon | Må |
| F-06 | Vise hendelsesstatus, tidslinje, ansvarlig rolle og oppgaver | Må |
| F-07 | Tillate justering av scenarioets omfang og varighet | Bør |
| F-08 | Eksportere en kort rapport med scenario, påvirkning, antakelser og tiltak | Bør |
| F-09 | Filtrere kartet etter tjeneste, leverandør, kritikalitet og status | Bør |
| F-10 | Vise sammenligning mellom to scenarioer | Kan |

## 10. Ikke-funksjonelle krav

- **Sikkerhet:** Ingen hemmeligheter eller sensitive opplysninger i klientkode eller demo-data.
- **Personvern:** Ingen innlogging nødvendig i prototypen; ingen brukerdata samles inn. Valg lagres bare i nettleserfanen (sessionStorage).
- **Tilgjengelighet:** Tastaturnavigasjon, synlige fokusmarkører (også på knapper med skygge), kontrast minst 4.5:1 for tekst og tekstalternativer til fargekoding.
- **Responsivitet:** Brukbar fra 360 px mobil til stor skjerm uten at siden ruller sideveis; kartet har en alternativ liste-/detaljvisning på små skjermer, og brede tabeller ruller inne i kortet.
- **Inndata:** Alle fritekstfelt har grenser og tegnfilter. Søk i kartet: maks 60 tegn, bokstaver, tall, mellomrom og enkle skilletegn. Beslutning: 3–500 tegn, bokstaver (alle språk), tall, linjeskift og vanlig tegnsetting; kontrolltegn, emoji og markup fjernes også ved innliming. Tekst vises alltid som ren tekst. Lagret tilstand valideres felt for felt ved innlasting, slik at gammel eller ødelagt lagring aldri krasjer appen.
- **Bufring:** Produksjonsbygget gir filnavn med innholdshash, slik at nye versjoner alltid lastes etter publisering. Biblioteker ligger i egne filer som kan gjenbrukes fra nettleserens cache når bare appkoden endres.
- **Sporbarhet:** Påvirkningsberegningen skal kunne forklares gjennom synlige relasjoner og regler.
- **Forståelighet:** Scenario og alle verdier skal være merket som syntetiske, også på utskrift av rapporten. Samme begreper brukes på alle sider (Bortfall, Redusert, Mulig bortfall, Over gjenopprettingsmål).
- **Språk:** Ingen brukerrettet tekst skrives direkte i komponentkoden; datoer og tall formateres etter valgt språk.
- **Robusthet:** Tomme, manglende eller motstridende relasjoner skal vises som datamangler, ikke skjules. Ukjente lenker og objekter gir en forståelig side, ikke en feil.

## 11. Data og demonstrasjonsmodell

Foreslåtte objekter:

- **Tjeneste:** navn, kritikalitet, tjenesteeier, kanaler, gjenopprettingsmål
- **System:** navn, miljø, driftsstatus, teknisk eier
- **Leverandør:** navn, tjenestetype, land/regioner, kritikalitet, alternativer
- **Avhengighet:** fra-objekt, til-objekt, type, kritikalitet, datakilde/gyldighetsstatus, regioner
- **Scenario:** feiltype, starttid, omfang, varighet, berørte komponenter
- **Hendelse:** status, tidslinje, beslutninger, oppgaver og ansvarlig rolle

Alle poster merkes `synthetic: true`. Brukerrettede tekstfelt (navn, beskrivelser, scenario- og oppgavetekster) lagres per språk (`no` og `en`). En demonstrasjonsrapport skal gjenta at dataene er oppdiktede.

## 12. Skisserte skjermer

1. **Tjenesteoversikt:** tjenestestatus og indikatorer for datakvalitet.
2. **Scenario:** valg av feiltype, komponent, alvorlighet og varighet.
3. **Påvirkning:** sammendrag, avhengighetskart med filter og søk (eller liste), detaljer og usikkerheter i datagrunnlaget.
4. **Hendelsesrom:** status, oppgaver, beslutningslogg, konsekvenser, kontrollspørsmål og tidslinje.
5. **Rapport:** kort, utskrivbar oppsummering av simuleringen.

## 13. Forslag til teknisk retning

Første versjon er en statisk webapp med et lite JSON-datasett og beregning av påvirkning i nettleseren. Dette holder demonstratoren enkel å kjøre og dele.

Valgt retning:

- **Rammeverk:** React, Vite og TypeScript.
- **Graf:** React Flow (`@xyflow/react`) med et eget båndoppsett: én kolonne per objekttype (leverandører → systemer → tjenester → kanaler). Rekkefølgen velges for å gi færrest kryssende piler, oppsettet strekkes til kartrammens høyde, og hver boks flyttes dit færrest mulig streker går gjennom bokser. Nodene er vanlige React-/DOM-elementer, noe som gir tastaturfokus, skjermleserstøtte, språkfiler og egen styling. Cytoscape.js ble vurdert, men tegner på canvas og gjør tilgjengelighetskravene i §10 vanskeligere.
- **Ruting:** Hash-baserte URL-er, slik at direkte lenker og oppfrisking fungerer på statisk hosting.
- **Språk:** i18n-oppsett med norsk og engelsk språkfil.
- **Hosting:** GitHub Pages fra mappen «Bank Resilience Map» i det offentlige repoet `steinwulvik/AI-prosjekter`, med stabil lenke til CV-en: https://steinwulvik.github.io/AI-prosjekter/bank-resilience-map/. Publisering skjer først når forfatteren sier fra.

Hvis konseptet senere valideres, kan det utvides med API, database, tilgangsstyring, import av kundens tjeneste- og leverandørregistre, revisjonsspor og integrasjoner. Dette ligger utenfor demonstratorens første leveranse.

## 14. Prosjektplan

| Fase | Arbeid | Leveranse |
|---|---|---|
| 1. Avgrensing | Velge scenario, brukerreise og syntetisk eksempelbank | Godkjent MVP-scope |
| 2. Innholdsmodell | Definere tjenester, systemer, leverandører, relasjoner og scenario | JSON-datamodell og datasett |
| 3. UX-utkast | Skissere oversikt, kart, scenario og hendelsesrom | Klikkbar prototype |
| 4. Bygg MVP | Implementere graf, påvirkningsregler, tidslinje og detaljer | Kjørbar webdemo |
| 5. Gjennomgang | Kontrollere forståelighet, mobilvisning, tilgjengelighet og merking av syntetiske data | Forbedret demo og kjente begrensninger |
| 6. Presentasjon | Lage kort demo-manus og prosjektforklaring | 3–5 minutters presentasjon |

### 14.1 Status (6. november 2026)

| Fase | Status |
|---|---|
| 1. Avgrensing | Ferdig (se §17) |
| 2. Innholdsmodell | Ferdig: datamodell og syntetisk datasett for Morild Bank (4 kanaler, 8 tjenester, 13 systemer, 6 leverandører, 45 relasjoner, 2 scenarioer) |
| 3. UX-utkast | Gått direkte til kjørbar prototype i stedet for egne skisser |
| 4. Bygg MVP | Ferdig: alle skjermer i §12 pluss intro og «Om demoen» |
| 5. Gjennomgang | Ferdig 6. november 2026, se §14.2. Gjenstår: test med ekte skjermleser og på iOS/Safari |
| 6. Presentasjon | Ikke startet |

Gjenstår før publisering: laste opp mappen til repoet `steinwulvik/AI-prosjekter`, legge workflowen `bank-resilience-map.yml` i `.github/workflows/` i roten av repoet og slå på GitHub Pages med kilden «GitHub Actions».

### 14.2 Testrapport (6. november 2026)

Produksjonsbygget ble testet servert fra en undermappe, slik GitHub Pages gjør det.

- **Typesjekk, tester og bygg:** `tsc -b` uten feil etter én rettelse (ubrukt variabel som ville stoppet bygget). 12 av 12 tester består.
- **Bufring:** Alle skript og stiler har innholdshash i filnavnet. Biblioteker er delt i egne filer (React og React Flow), og ubrukt avhengighet (dagre) er fjernet.
- **Lagring og robusthet:** Ødelagt JSON, feil form på lagrede felter, ukjent scenario, ukjent målsystem, ukjent objekt i lenken og ukjent side gir ingen feil. Oppfrisking med valgt objekt og tilbake-knappen virker.
- **Inndata:** Grenser og tegnfilter lagt til (§10). Testet med for lang tekst, HTML-kode, emoji, kontrolltegn og innliming.
- **Skjermbredder:** 360, 768, 994, 1280 og 1600 px på alle sider. Rettet sideveis rulling i Tjenesteoversikt (768–994 px), i oppgavelisten på mobil og lange ord i lister og beslutninger.
- **Tilgjengelighet (axe):** Rettet kontrast på grå hjelpetekst og overtekst, manglende landemerke for banneret, ugyldig definisjonsliste i detaljpanelet og manglende fokusmarkering på knapper. Ingen gjenstående funn.
- **Utskrift:** Rapporten skrives ut på tre A4-sider uten tom halvside, og ansvarsfraskrivelsen om syntetiske data er med.
- **Konsistens:** Tallene i sammendrag, kart, liste, hendelsesrom og rapport stemmer for begge scenarioer. Gruppenavn i listevisningen er endret fra «Nede/Usikkert» til «Bortfall/Mulig bortfall», som ellers i appen.

## 15. Foreslått demonstratoravgrensing

For å få en tydelig første demonstrasjon anbefales:

- én fiktiv bank
- 6–8 tjenester, 10–15 systemer og 4–6 leverandører
- ett hovedscenario: svikt hos en kritisk leverandør
- ett alternativt scenario: feil etter en systemendring
- påvirkningsstier med synlig forklaring, ikke svart-boks-score
- hendelsesrom med tidslinje, oppgaver og rapportvisning

## 16. Akseptansekriterier for demonstratoren

Demonstratoren kan regnes som klar når:

1. Brukeren kan gå fra scenario til berørte tjenester uten hjelp.
2. Hver markert påvirkning kan spores gjennom synlige avhengigheter.
3. Manglende data og antakelser er synlige og påvirker ikke resultatet stilltiende.
4. Brukeren kan følge hendelsens tidslinje og se ansvar/oppgaver.
5. Rapporten viser scenario, påvirkede tjenester, antakelser og syntetisk datamerking.
6. Hovedflyten fungerer på mobil og med tastatur.

## 17. Risikoer og åpne spørsmål

- **Forenklet modell:** Et avhengighetskart kan gi falsk trygghet hvis det ser komplett ut. Vis derfor datadekning og usikkerhet tydelig.
- **For bredt scope:** DORA, cyber, leverandørstyring og katastrofegjenoppretting kan bli et helt produktspekter. Første demo bør begrenses til ett scenario.
- **Produktpåstander:** Konseptet må presenteres som et eget forslag, ikke som et eksisterende produkt eller et uttrykk for noen virksomhets interne planer.
- **Navngitte selskaper:** Ingen virkelige selskaper skal nevnes, verken i appen eller i prosjektfilene (grensesnitt, data, README, spesifikasjon, sidemetadata). Uavhengigheten uttrykkes generelt. Besluttet 6. november 2026.
- **Innhold i offentlig repo:** Mappene «Claude outputs» og «OLD» er arbeidsfiler og skal ikke ligge i det offentlige repoet.
- **Kontaktopplysninger:** E-post, mobilnummer og LinkedIn står offentlig på «Om demoen» etter forfatterens ønske.
- **Brukerbehov:** Før videreutvikling bør målgruppen gi tilbakemelding på om kartet faktisk hjelper dem å forstå avhengigheter og koordinere respons.
- **Overlapp med eksisterende tilbud (undersøkt 6. november 2026):** Et søk i offentlig materiale fra nordiske leverandører av bankprogramvare og driftstjenester fant ingen produkter for avhengighetskart, konsekvensanalyse, scenariotesting eller registeret over IKT-leverandører som DORA krever. Slike verktøy selges i dag mest av GRC-leverandører og rådgivere. Søket dekker bare publisert materiale; interne eller upubliserte løsninger er ukjente. Konseptet presenteres som et selvstendig forslag.

Avklart før byggestart (6. november 2026):

1. **Målgruppe:** Demonstrasjonen er primært for operasjonell risiko, i tråd med primærbrukeren i §6.
2. **Scenario:** Svikt hos en kritisk leverandør er hovedscenario; feil etter systemendring er alternativt scenario (jf. §15).
3. **Redigering:** Brukeren utforsker et ferdig datasett og kan ikke endre avhengighetskartet i første versjon.
4. **Språk:** Norsk og engelsk med språkvelger.
5. **Hosting:** GitHub Pages.
6. **Grafbibliotek:** React Flow med eget båndoppsett (se §13). Dagre er erstattet.

## 18. Kort presentasjonspitch

> Bank Resilience Map er en konseptdemo som viser hvordan en bank kan forstå følgevirkningene av en IT- eller leverandørforstyrrelse. Den kobler kritiske tjenester til systemer og leverandører, synliggjør påvirkningsstier og samler scenario, usikkerhet og oppfølging i ett hendelsesrom. Demoen bruker kun syntetiske data og viser hvordan sporbarhet og forklarbarhet kan bygges inn fra starten.

## 19. Endringslogg

- **1.0, faglig rettelse (7. november 2026):** Etter gjennomgang mot primærkilder: kjernebanksystemet leveres og driftes av en kjernebankleverandør (Kjernedrift Nord) i stedet for i bankens eget datasenter, slik det er vanlig i norske banker. Innlogging går via en felles eID-løsning (Bankfelles eID), som Finanstilsynet beskriver som et tydelig enkeltpunkt for svikt. Oppgaven om rapportering bruker DORA-begrepet «alvorlig IKT-relatert hendelse». «Om demoen» viser til DORA og Finanstilsynets risiko- og sårbarhetsanalyse 2026 i tillegg til ECB. Resultatene i de to scenarioene er uendret.
- **0.10 (6. november 2026):** Fjernet alle navn på virkelige selskaper fra spesifikasjonen. Overlappsanalysen i §17 er gjort generell.
- **0.9 (6. november 2026):** Omfattende test (§14.2) med rettelser. Nye krav til inndata og bufring (§10). Kartet ligger i Påvirkning med båndoppsett i stedet for dagre (§2.1, §13). Språkvelger for norsk og engelsk vedtatt (P-16, D-13). Lagt til åpent spørsmål om hva som skal ligge i det offentlige repoet (§17).
- **0.8 (6. november 2026):** Lagt til funn om overlapp med eksisterende tilbud under §17.
- **0.7 (6. november 2026):** Fjernet fanerekken. Trinnene 1–4 er navigasjonen, kartet nås fra påvirkningsanalysen, og Tjenesteoversikt og Om demoen er lenker øverst til høyre. Rettet museklikk på objekter i kartet.
- **0.6 (6. november 2026):** Introsiden er gjort til en ren presentasjon uten menyfaner, med «Gå til demoen» nederst. Demoen starter i Scenario, og fanene følger avviksprosessen (§2.1).
- **0.5 (6. november 2026):** Fjernet navngitte selskaper fra appen; P-13 og §2.1 krever nå en generell uavhengighetsmerking uten navngitte selskaper (§17).
- **0.4 (6. november 2026):** MVP bygget og verifisert. Lagt til statusoversikt (§14.1).
- **0.3 (6. november 2026):** Valgt React Flow med dagre som grafbibliotek; ingen åpne spørsmål gjenstår før byggestart.
- **0.2 (6. november 2026):** Rettet dobbel seksjon 9 (funksjonelle krav har nå eget nummer) og nummerert påfølgende seksjoner. Lukket åpne spørsmål om målgruppe, scenario og redigering. Lagt til språkkrav (P-16, D-13), teknisk retning og hosting på GitHub Pages.
- **0.1 (6. november 2026):** Første konseptutkast.
