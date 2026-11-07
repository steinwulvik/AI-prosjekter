# Bank Resilience Map
## Kravspesifikasjon og prosjektplan – versjon 2.0 «fra hendelse til forebygging»

**Versjon:** 2.0-utkast · **Status:** Planlegging av versjon 2.0. Versjon 1.0 er publisert og låst. · **Dato:** 7. november 2026

## 1. Kort om konseptet

Bank Resilience Map er en interaktiv demonstrator for å forstå hvordan bankens viktige tjenester avhenger av interne systemer og eksterne IT-leverandører. Brukeren kan simulere en driftsforstyrrelse og se hvilke tjenester som kan bli påvirket, hvilke avhengigheter som må undersøkes, og hvilke oppfølgingsoppgaver som bør vurderes.

Demonstratoren bruker oppdiktede banker, systemer, leverandører og hendelser. Den skal vise en arbeidsflyt og et produktkonsept, ikke gi en formell risikovurdering eller dokumentere faktisk DORA-etterlevelse.

### 1.1 Versjoner

| Versjon | Status | Innhold |
|---|---|---|
| 1.0 | Publisert 6. november 2026, låst. Ligger på https://bank-resilience-map.pages.dev (Cloudflare Pages) og heter «Bank Resilience Map 1.0» i appen | Hendelsesflyten: Scenario → Påvirkning → Hendelsesrom → Rapport, Tjenesteoversikt, Om demoen, norsk og engelsk |
| 2.0 «fra hendelse til forebygging» | Publisert 7. november 2026. Ligger på https://bank-resilience-map-2.pages.dev (Cloudflare Pages, prosjekt `bank-resilience-map-2`, mappen «Bank Resilience Map 2.0») og heter «Bank Resilience Map 2.0» i appen | Alt i 1.0, pluss Leverandører, Endringer og Øvelser og funn (§2.3, §8.2, §14.3) |

Versjon 1.0 og 2.0 ligger på nett hver for seg, med hver sin mappe i repoet og hvert sitt Cloudflare-prosjekt. 1.0 endres ikke. Kravene for 1.0 nedenfor gjelder fortsatt i 2.0 med mindre en 2.0-del sier noe annet.

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
- Sider utenfor trinnene (tjenesteoversikt, leverandører, endringer, øvelser og funn, om demoen) har en lenke tilbake til flyten.
- I 2.0 kommer tre nye oppslagssider øverst til høyre: «Leverandører», «Endringer» og «Øvelser og funn» (§2.3). Trinnene 1–4 er uendret.
- Gi en guidet, men hoppbar start som leder brukeren gjennom scenario → påvirkning → respons → rapport.
- La brukeren nullstille scenarioet og komme tilbake til en forståelig standardvisning.
- Vis tydelig at det er en uavhengig konseptdemo, ikke et kommersielt produkt eller laget på oppdrag fra noen bank eller leverandør. Appen skal ikke nevne navngitte selskaper (se §17). Banneret øverst på alle sider sier «Demonstrasjon med syntetiske data · Uavhengig konseptdemo». Forfatter og kontaktopplysninger står nederst på «Om demoen».
- Grensesnittet er på norsk, med språkvelger for norsk og engelsk (P-16).
- Sørg for at appen er responsiv, tilgjengelig og tåler direkte åpning av lenke og oppfrisking av siden.
- Ikke samle inn besøksdata eller tilby ekte bankintegrasjoner i offentlig demo uten særskilt behov, personvernvurdering og tydelig informasjon.

Offentlig tilgjengelighet gjelder demonstratoren. Eventuelle reelle bankdata, integrasjoner, brukeradministrasjon eller interne arbeidsflyter krever separat tilgangsstyring og sikkerhetsdesign før produksjonsbruk.

### 2.3 Versjon 2.0: fra hendelse til forebygging

Versjon 1.0 hjelper banken når noe allerede har gått galt. Versjon 2.0 skal også hjelpe banken med å unngå at det skjer, og svarer direkte på svakhetene Finanstilsynet peker på i risiko- og sårbarhetsanalysen for 2026: leverandør- og verdikjederisiko og konsentrasjon hos få leverandører og fellesløsninger, mangler i endringshåndteringen, beredskapstester som ikke alltid bygger på realistiske scenarioer, og funn som ikke alltid følges opp systematisk. Alle nye deler bruker samme datasett, avhengighetskart og påvirkningsberegning som 1.0.

| Side | Hva den gjør | Krav og funn den svarer på |
|---|---|---|
| Leverandører | Register over leverandører og underleverandører i flere ledd, med kritikalitet, tjenestene de understøtter, land, kilde, sist bekreftet, exit-plan og hvor lett leverandøren kan byttes ut. Eksport av registeret i et forenklet format, merket som demo. Klikk på en leverandør åpner kartet med den valgt. | DORAs register over IKT-leverandører og exit-planer; konsentrasjonsrisiko |
| Endringer | Vurdering av en planlagt endring før driftssetting: velg system, tidspunkt og risiko, se forventet påvirkning i kartet, gå gjennom en sjekkliste og godkjenn eller avvis med begrunnelse i loggen. | Mangler i endringshåndteringen funnet ved tilsyn |
| Øvelser og funn | Et scenario kan startes som øvelse i stedet for hendelse. Hendelsesrommet og rapporten merkes «Øvelse». Funn registreres med ansvarlig, frist og status, og siden samler alle funn og viser hvilke som er åpne. | DORAs krav til testing; lite helhetlige øvelser og svak oppfølging av funn |

«Om demoen» i 2.0 består av innholdet fra 1.0 (beregningsregler, begrensninger, personvern, teknologi, kilder) pluss nye deler om hvorfor området er valgt, hvem som kan tilby en slik tjeneste og hva som er nytt i 2.0. Teksten står i §20.

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

### 8.2 Nye krav i versjon 2.0

| ID | Sluttproduktkrav | Målbilde | Demonstratorens bevis | Prioritet |
|---|---|---|---|---|
| P-17 | Leverandører og underleverandører i flere ledd skal kunne vises som et register med kritikalitet, understøttede tjenester, land, kilde og aktualitet | 1–2 | Siden «Leverandører» bygget på datasettet | Må |
| P-18 | Hver kritisk leverandør skal ha en exit-plan med status og en vurdering av hvor lett den kan byttes ut | 2, 4 | Exit-status og alternativer i leverandørregisteret | Må |
| P-19 | En planlagt endring skal kunne vurderes mot avhengighetskartet før driftssetting, med sporbar beslutning | 3–5 | Siden «Endringer» med forventet påvirkning, sjekkliste og godkjenning | Må |
| P-20 | Scenarioer skal kunne kjøres som øvelser, og funn skal følges opp til de er lukket | 5–6 | Øvelsesmodus og siden «Øvelser og funn» | Må |
| P-21 | Leverandørregisteret skal kunne eksporteres i et maskinlesbart format | 6 | Forenklet CSV-eksport merket som demo, ikke et offisielt tilsynsformat | Bør |

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
| D-14 | Vise alle leverandører i datasettet, med underleverandørkjeder og exit-status | P-17, P-18 |
| D-15 | Vise minst tre planlagte endringer i datasettet, der minst én bør avvises fordi den rammer kritiske tjenester uten reserveløsning | P-19 |
| D-16 | Kjøre begge scenarioene som øvelse, med forhåndsutfylte funn og mulighet til å legge til egne | P-20 |
| D-17 | Lagre nye endringsvurderinger og funn bare i nettleserfanen, som resten av demoen | P-15, P-19, P-20 |
| D-18 | Eksportere leverandørregisteret som CSV | P-21 |

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
| F-11 | Vise et leverandørregister med underleverandører i flere ledd (2.0) | Må |
| F-12 | Vise exit-plan, status og byttbarhet per leverandør (2.0) | Må |
| F-13 | Vurdere en planlagt endring mot kartet og registrere beslutning med begrunnelse (2.0) | Må |
| F-14 | Starte et scenario som øvelse og merke hendelsesrom og rapport deretter (2.0) | Må |
| F-15 | Registrere funn med ansvarlig, frist og status, og vise alle åpne funn samlet (2.0) | Må |
| F-16 | Eksportere leverandørregisteret som CSV (2.0) | Bør |

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
- **Leverandør (utvidet i 2.0):** direkte avtale (ja/nei), kontraktseier, exit-plan (finnes, under arbeid, mangler), byttbarhet (lett, krevende, ikke mulig), sist vurdert, exit-plan sist testet. Ledd i leverandørkjeden (1 = direkte avtale, 2 = underleverandør osv.) beregnes fra underleverandørkoblingene, slik DORA-registeret krever for tjenester som støtter kritiske eller viktige funksjoner
- **Planlagt endring (2.0):** id, system som endres, planlagt tidspunkt, risiko, tilbakerulling testet, sjekkpunkter, beslutning og begrunnelse
- **Øvelse (2.0):** scenario, dato, deltakere (roller), leverandører som deltok, funn
- **Funn (2.0):** tittel, kilde (øvelse eller hendelse), ansvarlig rolle, frist, status (åpen, under arbeid, lukket)

Innhold i datasettet for 2.0 (fase 2.0-2, 7. november 2026):

- **Leverandører:** Seks leverandører med direkte avtale har kontraktseier, exit-plan, byttbarhet og dato for siste vurdering. To nye underleverandører uten avtale med banken (fjerdeparter) viser kjeder i flere ledd: Datahall Vest (under KortNord Prosessering) og Nordnett Mobil (under SMS-Linje). Koblingene til dem er «myke», fordi leverandørene over har andre plattformer eller land i reserve. Én vurdering er utdatert (Saksflyt AS), og én er aldri gjort (SMS-Linje). Exit-planene er testet for to leverandører; de andre er aldri testet.
- **Planlagte endringer:** Fire endringer. CHG-2026-118 er godkjent som eksempel. CHG-2026-121 (integrasjonsplattformen, høy risiko, tilbakerulling ikke testet) bør avvises. CHG-2026-124 og CHG-2026-127 venter på vurdering. Forventet påvirkning beregnes med samme motor som scenarioene.
- **Øvelser og funn:** To bordøvelser, én per scenario, og åtte funn. Sju kommer fra øvelsene og ett fra hendelsen etter endring CHG-2026-114. Ett funn gjelder at skyleverandøren ikke deltok i øvelsen. Funnene har status åpen, under arbeid eller lukket, og peker på objekter i kartet.
- To leverandører er lagt til i både 1.0 og 2.0 etter faktasjekken: kjernebankleverandøren Kjernedrift Nord (kjernebanksystemet driftes ikke lenger i bankens eget datasenter) og den felles eID-løsningen Bankfelles eID (innlogging).
- Scenarioene fra 1.0 gir de samme resultatene som før.

Alle poster merkes `synthetic: true`. Brukerrettede tekstfelt (navn, beskrivelser, scenario- og oppgavetekster) lagres per språk (`no` og `en`). En demonstrasjonsrapport skal gjenta at dataene er oppdiktede.

## 12. Skisserte skjermer

1. **Tjenesteoversikt:** tjenestestatus og indikatorer for datakvalitet.
2. **Scenario:** valg av feiltype, komponent, alvorlighet og varighet.
3. **Påvirkning:** sammendrag, avhengighetskart med filter og søk (eller liste), detaljer og usikkerheter i datagrunnlaget.
4. **Hendelsesrom:** status, oppgaver, beslutningslogg, konsekvenser, kontrollspørsmål og tidslinje.
5. **Rapport:** kort, utskrivbar oppsummering av simuleringen.
6. **Leverandører (2.0):** register med underleverandørkjeder, exit-status og eksport.
7. **Endringer (2.0):** liste over planlagte endringer, vurdering med forventet påvirkning og beslutning.
8. **Øvelser og funn (2.0):** øvelser som er kjørt, og alle funn med status.

## 13. Forslag til teknisk retning

Første versjon er en statisk webapp med et lite JSON-datasett og beregning av påvirkning i nettleseren. Dette holder demonstratoren enkel å kjøre og dele.

Valgt retning:

- **Rammeverk:** React, Vite og TypeScript.
- **Graf:** React Flow (`@xyflow/react`) med et eget båndoppsett: én kolonne per objekttype (leverandører → systemer → tjenester → kanaler). Rekkefølgen velges for å gi færrest kryssende piler, oppsettet strekkes til kartrammens høyde, og hver boks flyttes dit færrest mulig streker går gjennom bokser. Nodene er vanlige React-/DOM-elementer, noe som gir tastaturfokus, skjermleserstøtte, språkfiler og egen styling. Cytoscape.js ble vurdert, men tegner på canvas og gjør tilgjengelighetskravene i §10 vanskeligere.
- **Ruting:** Hash-baserte URL-er, slik at direkte lenker og oppfrisking fungerer på statisk hosting.
- **Språk:** i18n-oppsett med norsk og engelsk språkfil.
- **Hosting:** Cloudflare Pages (gratis), bygget automatisk fra mappen «Bank Resilience Map 1.0» i repoet `steinwulvik/AI-prosjekter`: https://bank-resilience-map.pages.dev. Cloudflare kan bygge fra et privat repo, slik at koden kan skjules uten at lenken slutter å virke. Oppsettet for GitHub Pages er fjernet fra repoet; den gamle github.io-lenken viser siste publiserte kopi til GitHub Pages skrus av eller repoet blir privat. Versjon 2.0 legges i en egen mappe, «Bank Resilience Map 2.0», med eget Cloudflare-prosjekt. Publisering skjer først når forfatteren sier fra.

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

### 14.3 Plan for versjon 2.0

| Fase | Arbeid | Leveranse |
|---|---|---|
| 2.0-1 Grunnlag | Ny SPEC og skill, «Om demoen» for 2.0, versjonsmerking | Godkjent plan (denne versjonen av SPEC) |
| 2.0-2 Datamodell | Utvide datasettet med exit-felt, planlagte endringer, øvelser og funn, på norsk og engelsk | Oppdatert datasett og typer |
| 2.0-3 Leverandører | Siden «Leverandører» med register, underleverandørkjeder, exit-status og CSV-eksport | Ferdig side, testet |
| 2.0-4 Endringer | Siden «Endringer» med forventet påvirkning, sjekkliste og beslutning | Ferdig side, testet |
| 2.0-5 Øvelser og funn | Øvelsesmodus i Scenario, Hendelsesrom og Rapport, og siden «Øvelser og funn» | Ferdig side og flyt, testet |
| 2.0-6 Navigasjon og helhet | Toppmeny som tåler fem lenker på mobil, veiledning og intro oppdatert for 2.0 | Sammenhengende app |
| 2.0-7 Test og publisering | Samme testløp som i §14.2 for hele appen, deretter publisering når forfatteren sier fra | Versjon 2.0 på nett |

Rekkefølgen følger nytte mot innsats: Leverandører og Endringer gjenbruker mest av det som finnes. Hver fase avsluttes med syntakssjekk og visning i nettleseren.

### 14.4 Testrapport for 2.0 (7. november 2026)

Produksjonsbygget ble testet servert fra en undermappe, med samme punkter som for 1.0 (§14.2), nå for alle ti sider.

- **Typesjekk, tester og bygg:** `tsc -b` uten feil, 17 av 17 tester består, bygget lykkes. Datasettet genereres uten manglende oversettelser.
- **Skjermbredder:** 360, 768, 994, 1280 og 1600 px på alle sider uten sideveis rulling. Rettet: faktaboksen i vurderingen på «Endringer» står i én kolonne på mobil, så lange systemnavn ikke deles midt i ordet.
- **Tilgjengelighet (axe):** Ingen funn på 1280 og 360 px etter én rettelse: tabellene i rapporten kan rulles sideveis på mobil og kan nå nås med tastaturet.
- **Plassering:** «Syntetiske data» står på nøyaktig samme sted på alle ni sider etter introsiden.
- **Konsistens:** Nøkkeltallene stemmer med listene: Leverandører (8 med avtale, 3 mangler exit-plan, 6 aldri testet), Endringer (3 venter), Øvelser og funn (4 åpne + 3 under arbeid = 7 rader). Scenarioene gir samme resultat som i 1.0.
- **Lagring og robusthet:** Ødelagt JSON, manipulerte felter, ukjent side og ukjent endring i adressen gir ingen feil.
- **Inndata:** Begrunnelse (maks 500 tegn) og funn (maks 120 tegn) fjerner HTML-tegn og emoji.
- **Øvelse:** Hele flyten fra «Start en øvelse» til «Øvelsesrapport» virker. Menyen på mobil åpnes med Enter og lukkes med Esc.
- **Språk:** Ingen norske rester i den engelske versjonen. Ingen feil i konsollen.
- **Utskrift:** Rapporten skrives ut på tre A4-sider.

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

Versjon 2.0 kan i tillegg regnes som klar når:

7. Alle leverandører i datasettet vises i registeret, med underleverandørkjede, exit-status og byttbarhet, og registeret kan eksporteres som CSV.
8. Brukeren kan vurdere en planlagt endring, se forventet påvirkning i kartet og registrere en beslutning med begrunnelse.
9. Brukeren kan kjøre et scenario som øvelse, registrere funn og se alle åpne funn samlet.
10. Tallene og begrepene i de nye sidene stemmer med kart, sammendrag og rapport.
11. Alt nytt finnes på norsk og engelsk og består samme testløp som 1.0 (§14.2).

## 17. Risikoer og åpne spørsmål

- **Forenklet modell:** Et avhengighetskart kan gi falsk trygghet hvis det ser komplett ut. Vis derfor datadekning og usikkerhet tydelig.
- **For bredt scope:** DORA, cyber, leverandørstyring og katastrofegjenoppretting kan bli et helt produktspekter. Første demo bør begrenses til ett scenario.
- **Produktpåstander:** Konseptet må presenteres som et eget forslag, ikke som et eksisterende produkt eller et uttrykk for noen virksomhets interne planer.
- **Navngitte selskaper:** Ingen virkelige selskaper skal nevnes, verken i appen eller i prosjektfilene (grensesnitt, data, README, spesifikasjon, sidemetadata). Uavhengigheten uttrykkes generelt. Besluttet 6. november 2026.
- **Innhold i offentlig repo:** Mappene «Claude outputs», «OLD» og «publisering» er arbeidsfiler og skal ikke ligge i det offentlige repoet.
- **Toppmenyen (besluttet 7. november 2026):** På skjermer smalere enn 1100 px samles oppslagslenkene og «Nullstill demo» bak knappen «Meny», som åpner en liste under toppfeltet. Listen lukkes ved navigasjon, med Esc og ved klikk utenfor. Språkvelgeren står alltid synlig. På bredere skjermer er menyen som i 1.0.
- **Eksportformat (besluttet 7. november 2026):** Leverandørregisteret eksporteres som forenklet CSV med semikolon som skilletegn og UTF-8 med BOM, så fila åpnes riktig i regneark med norske innstillinger. Kolonnene følger registeret (leverandør, ledd, leverandør i leddet over, kritikalitet, tjenestetype, land, tjenester som avhenger, kontraktseier, exit-plan, byttbarhet, sist vurdert, exit-plan sist testet, syntetiske data). Fila er merket som demo i filnavnet og med kolonnen «Syntetiske data». Exit-feltene fylles bare ut i ledd 1, der avtalen er; en leverandør som også står lavere i en kjede, henviser til ledd 1.
- **Versjonsmerking (besluttet 7. november 2026):** Versjonsnummeret vises i appnavnet: «Bank Resilience Map 1.0» og «Bank Resilience Map 2.0». Navnet forkortes ikke i appen, i repoet eller i dokumentasjonen.
- **Kontaktopplysninger:** E-post, mobilnummer og LinkedIn står offentlig på «Om demoen» etter forfatterens ønske.
- **Brukerbehov:** Før videreutvikling bør målgruppen gi tilbakemelding på om kartet faktisk hjelper dem å forstå avhengigheter og koordinere respons.
- **Overlapp med eksisterende tilbud (undersøkt 6. og 7. november 2026):** Ingen nordiske leverandører av bankprogramvare og driftstjenester omtaler i offentlig materiale produkter for avhengighetskart, konsekvensanalyse, scenariotesting eller DORA-registeret. Slike verktøy selges av internasjonale leverandører av programvare for risikostyring og kontinuitet (avhengighetskart, scenariotesting) og av en norsk leverandør av programvare for kontrakts- og leverandørstyring (DORA-register). Ingen av dem driver bankenes systemer. Det som skiller konseptet, er at leverandøren som driver systemene, også kan levere dataene. Søket dekker bare publisert materiale. Konseptet presenteres som et selvstendig forslag.
- **Faktagrunnlag (kontrollert 7. november 2026):** Påstander om myndighetskrav i appen skal holde seg innenfor det primærkildene sier. Finanstilsynets ROS 2026 (29. april 2026) omtaler leverandør- og verdikjederisiko blant de mest kritiske sårbarhetene, konsentrasjon hos få leverandører og fellesløsninger, mangler i endringshåndtering funnet ved tilsyn, beredskapstester som ikke alltid bygger på realistiske scenarioer, funn som ikke er fulgt opp systematisk, og at exit-planer skal testes. Analysen oppgir ikke hvor stor andel av hendelsene som skyldes endringer. Den beskriver den felles eID-løsningen bankene bruker til innlogging og signering som et tydelig enkeltpunkt for svikt, med utilstrekkelig robusthet ved langvarig bortfall. Norske banker får som regel kjernebanksystemet levert og driftet av én av noen få eksterne leverandører. DORA-begrepet for hendelser som skal rapporteres, er «alvorlige IKT-relaterte hendelser». Ingen nordiske leverandører er blant de 19 leverandørene EU utpekte som kritiske IKT-tjenesteleverandører 18. november 2025. Registeret over IKT-tjenesteavtaler rapporteres første gang til Finanstilsynet innen 15. mars 2027.

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

- **2.0-utkast, rettelse (7. november 2026):** Versjon 1.0 flyttet til Cloudflare Pages og har fått «1.0» i appnavnet. Versjonsmerking besluttet (§17).
- **2.0 publisert (7. november 2026):** Lagt i mappen «Bank Resilience Map 2.0» i repoet og publisert med Cloudflare Pages til https://bank-resilience-map-2.pages.dev (prosjekt `bank-resilience-map-2`, bygg `npm run build`, utdata `dist`, NODE_VERSION=22). Alle filene på GitHub er kontrollert mot den testede versjonen. 1.0 er uendret.
- **2.0, fase 2.0-7 testrunde (7. november 2026):** Full testrunde gjennomført (§14.4). To rettelser: tastaturtilgang til tabellene i rapporten på mobil og faktaboksen på «Endringer» i én kolonne på mobil. Klar til publisering når forfatteren sier fra.
- **2.0-utkast, fase 2.0-6 (7. november 2026):** Appen heter «Bank Resilience Map 2.0» (tittel, sidetittel og fanetittel). Toppmenyen har menyknapp på smale skjermer (§17). Introsiden har kortet «Forebygging» med lenker til Leverandører, Endringer og Øvelser og funn. Veiledningen nevner valget mellom hendelse og øvelse, og siste steg peker til de nye sidene.
- **2.0-utkast, fase 2.0-5 (7. november 2026):** Øvelser og funn er bygget. Scenarioskjemaet har valget «Kjøres som: Hendelse / Øvelse» (forhåndsvalgt «Øvelse» fra knappen «Start en øvelse»). En øvelse merkes «Øvelse» i hendelsesrommet, med lenke for å registrere funn, og rapporten heter «Øvelsesrapport» med «Kjørt som: Øvelse». Hver øvelse som startes, legges til i øvelseslisten. Siden «Øvelser og funn» viser nøkkeltall (gjennomførte øvelser, åpne funn, funn under arbeid, lukkede funn), øvelsene med scenario, dato, deltakere (roller), leverandører som deltok og antall funn, alle funn med kilde, ansvarlig, frist og status (filter «Ikke lukket» / «Alle», status endres i listen) og et skjema for å registrere funn med ansvarlig og frist. Statusendringer gjelder også funnene som vises på «Endringer». Alt lagres i fanen og nullstilles med «Nullstill demo». To nye tester for lagringen (17 av 17 består).
- **2.0-utkast, fase 2.0-4 (7. november 2026):** Siden «Endringer» er bygget: nøkkeltall (planlagte, venter på beslutning, godkjent, avvist), tabell over planlagte endringer med risiko, tilbakerulling, tjenester som kan rammes og status, og vurdering av valgt endring (valg ligger i adressen). Vurderingen viser fakta, hva som rammes hvis endringen feiler (bortfall i systemet gjennom hele vedlikeholdsvinduet, samme beregning og sammendrag som «Påvirkning»), det samme kartet, sjekkliste, åpne funn for systemet og beslutningslogg. En endring kan bare godkjennes når alle sjekkpunkter er kontrollert; avvisning kan alltid registreres. Utfall er ikke forhåndsvalgt. Sjekkliste og beslutninger lagres i fanen og nullstilles med «Nullstill demo», men ikke når scenarioet byttes. §2.3 er justert til ordlyden i faktagrunnlaget.
- **2.0-utkast, felles oppsett (7. november 2026):** «Syntetiske data» står på samme sted på alle sider, øverst til høyre rett under språkvelgeren. På oppslagssidene står merket på linje med tilbakelenken, og i flyten på linje med tittelen. Knapper på siden (utskrift, CSV) står under merket. «Om demoen» har samme venstrekant som de andre sidene.
- **2.0-utkast, fase 2.0-3 (7. november 2026):** Siden «Leverandører» er bygget: nøkkeltall (leverandører med avtale, underleverandører uten avtale, mangler exit-plan, exit-plan aldri testet), register med ledd 1 og 2 der underleverandører står rett under leddet over, tjenester som avhenger (beregnet med påvirkningsmotoren), exit-plan, byttbarhet, sist vurdert (merket utdatert etter ett år) og sist testet, og CSV-eksport. Exit-data vises bare i ledd 1, så tallene i listen stemmer med nøkkeltallene; Nimbus Sky under Saksflyt AS viser «Se ledd 1». Navnet åpner samme detaljvindu som i Tjenesteoversikt, og detaljpanelet viser nå ledd, kontraktseier og exit-feltene også i kartet. Lenken «Leverandører» ligger i toppmenyen.
- **2.0-utkast og 1.0, faglig rettelse (7. november 2026):** Kjernebanksystemet leveres og driftes av en kjernebankleverandør, innlogging går via en felles eID-løsning, og rapporteringsoppgaven bruker DORA-begrepet «alvorlig IKT-relatert hendelse». Samme rettelse er gjort i 1.0. Kildene i «Om demoen» står med de norske først.
- **2.0-utkast, faktasjekk (7. november 2026):** Ny gjennomgang av primærkilder. Teksten i «Om demoen» (§20) er justert slik at den bare sier det kildene sier, og lenken til analysen går til Finanstilsynets egen side. Leverandørene har fått dato for siste test av exit-planen, øvelsene har fått feltet for leverandører som deltok, og ledd i leverandørkjeden beregnes (§11). Overlappsvurderingen og faktagrunnlaget er oppdatert (§17).
- **2.0-utkast, fase 2.0-2 (7. november 2026):** Datamodellen er utvidet med exit-felt på leverandører, to underleverandører, planlagte endringer, øvelser og funn (§11). Alle nye tekster finnes på norsk og engelsk.
- **2.0-utkast (7. november 2026):** Startet versjon 2.0 «fra hendelse til forebygging». Lagt til versjonsoversikt (§1.1), de nye sidene Leverandører, Endringer og Øvelser og funn (§2.3), nye krav P-17–P-21, D-14–D-18 og F-11–F-16, utvidet datamodell (§11), nye skjermer (§12), faseplan (§14.3), akseptansekriterier for 2.0 (§16), åpne spørsmål (§17) og tekst for «Om demoen» (§20). Versjon 1.0 er låst.
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

## 20. Tekst for «Om demoen» i versjon 2.0

Siden består av innholdet fra 1.0 pluss nye deler. Teksten ligger i språkfilene (`no.ts` og `en.ts`); den norske versjonen står her.

**Hva er dette?** Bank Resilience Map er en uavhengig konseptdemo som viser hvordan en bank raskt kan forstå følgene når en IT-leverandør eller et system svikter, og hvordan den kan forebygge at det skjer. Den kobler bankens kritiske tjenester og kundekanaler til systemene og leverandørene de er avhengige av, og viser hvordan en feil sprer seg gjennom kjeden.

**Slik er demoen bygget opp**

1. **Scenario:** Velg svikt hos en leverandør eller feil etter en systemendring, med alvorlighet og varighet.
2. **Påvirkning:** Se hvilke tjenester og kanaler som rammes, hvorfor, og hvilke som er nede lenger enn gjenopprettingsmålet. Usikre og utdaterte avhengighetsdata merkes tydelig i stedet for å bli skjult.
3. **Hendelsesrom:** Følg status, oppgaver med ansvarlig rolle, beslutningslogg og tidslinje på ett sted.
4. **Rapport:** Få en utskrivbar oppsummering med antakelser, datamangler og tiltak.

**Hvorfor dette området?** Bankene må kunne dokumentere hvordan de tåler svikt hos IKT-leverandører, og mange mangler verktøy for å se sammenhengene.

- **Krav fra myndighetene.** DORA, EUs forordning om digital operasjonell motstandsdyktighet, har gjeldt i Norge siden 1. juli 2025. Bankene skal blant annet føre et register over IKT-leverandører og underleverandørene deres, ha exit-planer og teste beredskapen. Registeret skal første gang rapporteres til Finanstilsynet innen 15. mars 2027.
- **Finanstilsynets funn.** I risiko- og sårbarhetsanalysen for 2026 trekker Finanstilsynet fram leverandør- og verdikjederisiko blant de mest kritiske sårbarhetene, og peker på konsentrasjon hos få leverandører og fellesløsninger. Den felles løsningen for elektronisk identifisering beskrives som et tydelig enkeltpunkt for svikt. Tilsyn har avdekket mangler i endringshåndteringen. Beredskapstester bygger ikke alltid på realistiske scenarioer, og funn fra tester og øvelser er ikke alltid fulgt opp systematisk.
- **Behovet i bankene.** Når noe svikter, må ledelsen raskt vite hvilke kunder og tjenester som rammes, og hvor sikkert bildet er. Den informasjonen ligger ofte spredt i ulike registre og hos enkeltpersoner.

Konseptet er derfor ikke et nytt rapporteringskrav, men et arbeidsverktøy som gjør dataene bankene uansett må samle inn etter DORA, nyttige i en reell hendelse.

**Hvem kan tilby dette?**

- Leverandører av kjernebank, betaling og driftstjenester støtter ofte bankenes kritiske funksjoner og må derfor med i bankenes leverandørregister. De kjenner allerede kundenes systemlandskap.
- Bankene må hente opplysninger om underleverandørene fra leverandørene sine. En slik leverandør kan levere disse opplysningene ferdig strukturert, rett inn i bankenes register, i stedet for at hver bank samler dem inn for hånd.
- Konseptet kan leveres som en felles tjeneste for mange banker, på samme måte som andre delte banktjenester.

**Nytt i versjon 2.0 – fra hendelse til forebygging.** Versjon 1.0 hjelper banken når noe allerede har gått galt. Versjon 2.0 skal også hjelpe banken med å unngå at det skjer. Tre nye deler bygger på samme avhengighetskart og beregning:

- **Leverandører:** Register over leverandører og underleverandører i flere ledd, med exit-plan, når planen sist ble testet, og hvor lett leverandøren kan byttes ut.
- **Endringer:** Viser hvilke tjenester og kunder en planlagt endring kan ramme, før den settes i drift, med sjekkliste og godkjenning.
- **Øvelser og funn:** Kjør scenarioer som øvelser og følg opp funnene til de er lukket.

Fra 1.0 beholdes: Slik beregnes påvirkningen, Begrensninger, Personvern, Teknologi og Bakgrunn (kilder: ECB-prioriteringer 2025–27 og 2026–28, DORA-forordningen og Finanstilsynets risiko- og sårbarhetsanalyse 2026). Forfatter og kontaktopplysninger står i bunnteksten.
