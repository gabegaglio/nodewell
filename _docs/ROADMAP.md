# Nodewell Roadmap

Future plans and architectural notes for Nodewell. This is a personal Python CLI
for container / infrastructure monitoring.

## Current status

- [x] **Inventory** — list all configured hosts
- [x] **Ping** — check host reachability (UP / DOWN)

## Next milestones (in order)

Get these working cleanly before touching anything else. Inventory → Ping →
Rich Tables is the foundation everything else builds on.

- [ ] **Rich tables** — render inventory/ping output with `rich` (colored UP/DOWN)
- [ ] **Reports** — `nodewell report` writes timestamped output files
- [ ] **Services** — service status checks
- [ ] **Status** — aggregate command that runs everything

**Not yet:** Docker, SSH collection, and web UIs. Don't start these until the
foundation above is solid.

---

## 1. Command registry

Replace the growing `if/elif` chain in `main.py`:

```python
if command == "inventory":
    ...
elif command == "ping":
    ...
elif command == "services":
    ...
```

With a `commands/` package where each command is its own module:

```
commands/
├── inventory.py
├── ping.py
├── services.py
└── docker.py
```

Each command module exposes a single entry point:

```python
def run(config):
    ...
```

`main.py` then just looks up the command and calls `run(config)`. This keeps
`main.py` tiny and makes adding commands trivial.

## 2. Config validation

Validate `config.yaml` before doing any work. Fail early with clear messages.

Check:
- Does `config.yaml` exist?
- Does every host have a `name`?
- Does every host have an `ip`?

Bad (cryptic):

```
KeyError: 'ip'
```

Good (actionable):

```
Host 'pihole' missing IP address
```

## 3. Result objects

Currently results are plain dicts:

```python
{
    "name": "router",
    "status": "UP",
}
```

Later, consider typed result objects for clarity and editor support:

```python
from dataclasses import dataclass

@dataclass
class PingResult:
    name: str
    ip: str
    status: str
```

Not now — keep it in mind as the result shapes stabilize.

## 4. Logging

Add a `logs/` directory and write to `nodewell.log`. Log meaningful events:

- Ping started
- Host failed
- Report generated

This makes the tool feel NOC-like and aids debugging.

## 5. Reports

A future `nodewell report` command that writes a timestamped report:

```
reports/
└── 2026-05-28_20-51.txt
```

Great beginner feature — builds on existing inventory/ping output.

## 6. Status command

Eventually the "main" command. `nodewell status` runs everything and displays a
combined view:

- inventory
- ping
- services
- docker

## 7. Inventory metadata

Don't stop at `name` / `ip`. Enrich host definitions so Nodewell understands the
infrastructure:

```yaml
hosts:
  - name: pihole
    ip: 192.168.0.200
    type: dns
    location: ct300

  - name: dashboard
    ip: 10.10.20.10
    type: web
    location: ct100
```

## 8. Future SSH collection

Where the project becomes genuinely useful. `nodewell collect` SSHes into hosts
and gathers:

- `uptime`
- `hostname`
- `df -h`
- `free -h`
- `docker ps`

Save the results. This mirrors what network/systems engineers actually automate.
Defer until the foundation milestones are done.
