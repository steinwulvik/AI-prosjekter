# Den trygge sykkelturen

Læringsapp som viser sykkelrute, trafikkmålepunkter med historisk trafikkmengde og vær ved start, midtveis og mål.

## Start lokalt

Installer Python 3. Åpne en terminal i denne mappen, og kjør:

```powershell
python -m pip install -r requirements.txt
python server.py
```

Åpne http://127.0.0.1:8001. Hold terminalvinduet åpent mens appen kjører. Stopp serveren med Ctrl+C.

Appen bruker Statens vegvesens Trafikkdata-API, MET Locationforecast API, BRouter for sykkelruter og OpenStreetMap-kartfliser. Trafikktall er historiske gjennomsnitt ved målepunkter, ikke sanntidskøer eller en fullstendig vurdering av sykkelsikkerhet. Ruteinnsikten er regelbasert, ikke AI-generert.

## Publisering

Legg filene i denne mappen i GitHub. I Render velger du denne mappen som Root Directory, `pip install -r requirements.txt` som Build Command og `python server.py` som Start Command.
