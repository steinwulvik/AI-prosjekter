# Kystdagens kontrollrom

En læringsapp som kombinerer Kartverkets vannstand med METs værvarsel for norske kyststeder.

## Start lokalt

Installer Python 3. Åpne en terminal i denne mappen, og kjør:

```powershell
python -m pip install -r requirements.txt
python server.py
```

Åpne http://127.0.0.1:8000. Hold terminalvinduet åpent mens appen kjører. Stopp serveren med Ctrl+C.

Appen bruker Kartverkets vannstands-API, MET Locationforecast API og OpenStreetMap-kartfliser. Kystnotatet er en enkel regelbasert oppsummering, ikke en AI-modell.

## Publisering

Legg filene i denne mappen i GitHub. I Render velger du denne mappen som Root Directory, `pip install -r requirements.txt` som Build Command og `python server.py` som Start Command.
