# python-ping

Ein einfaches, plattformübergreifendes Ping-Skript in Python (ohne externe Abhängigkeiten).

## Verwendung

```bash
python3 ping.py 8.8.8.8
```

Mit Optionen:

```bash
python3 ping.py google.com -c 5 -t 2
```

Ohne Argument fragt das Skript interaktiv nach dem Host oder der IP-Adresse:

```bash
python3 ping.py
```

### Optionen

| Option | Beschreibung | Standard |
| --- | --- | --- |
| `host` | Hostname oder IP-Adresse | Interaktive Eingabe |
| `-c`, `--count` | Anzahl der Ping-Pakete | `4` |
| `-t`, `--timeout` | Timeout pro Paket in Sekunden | `2` |
