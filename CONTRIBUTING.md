# Contributing to GuardTowarr

Thanks for taking a look. Bug reports, fixes, and new service integrations are all
welcome.

## How it's built

GuardTowarr is two files and the Python standard library:

- `monitor.py`: the backend. A stdlib-only HTTP server, the poller, all service
  checks, notifications, and config.
- `webpage.html`: the frontend. Plain HTML, CSS, and vanilla JavaScript in one
  file, no framework and no build step.

There is no database (state lives in flat JSON files) and no required pip
packages for the core. Please keep it that way. Optional extras (`pystray`,
`pillow` for the desktop tray icon) must degrade gracefully when absent.

## Running from source

```
python monitor.py
```

Then open `http://localhost:9595`. Config, dismissed issues, and history are
written to the working directory (or `GUARDTOWARR_CONFIG_DIR` if set). Those files
are gitignored; do not commit them, they contain your credentials.

## Before you open a PR

- Syntax-check the backend: `python -c "import ast; ast.parse(open('monitor.py').read())"`
- If you touched the frontend, check the inline script: extract the last
  `<script>` block and run `node --check` on it. A passing parse is the minimum;
  run the path you changed where you can.
- Keep changes focused. Explain what changed and why in the PR description.
- Match the existing style: small functions, comments that explain *why*, no new
  dependencies.

## Adding a service

The whole app is driven by one registry, so adding a monitored service is two
steps (a check function plus a registry entry). See
[docs/adding-a-service.md](docs/adding-a-service.md) for the walkthrough.

## Reporting bugs

Open an issue with what you ran (Docker or the Windows build), which services you
monitor, what you expected, and what happened. Console/log output helps.

## Security

Found a vulnerability? Please report it privately rather than in a public issue.
See [SECURITY.md](SECURITY.md).
