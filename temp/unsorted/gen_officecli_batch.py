# Generate OfficeCLI batch JSON for all replacements
import json

# Read the commands from operations we need
# Structure: op="set", path, props
commands = []

def set_text(path, text, bold=None):
    cmd = {"op": "set", "path": path}
    props = {}
    if text is not None:
        props["text"] = text
    if bold is not None:
        props["bold"] = bold
    cmd["props"] = props
    commands.append(cmd)

# Key replacements based on paragraph index paths
# Format: /body/p[N] where N is 1-based paragraph index

# Cover page
set_text("/body/p[3]", "\u201cICC COMPANION\u201d")  # Project title
set_text("/body/p[1]", "A PROJECT REPORT ON")

# Table 0 row 1 (guide info) - need to navigate tables differently
# With OfficeCLI, table cells are addressed as /body/tbl[N]/tr[M]/tc[K]

# Actually, let me use a different approach - use OfficeCLI's merge command
# or do simpler targeted replacements

# For now, let me just do the core text changes

commands_json = json.dumps(commands, indent=2)
with open(r'C:\xampp\htdocs\ICC_Companion\temp\officecli_batch.json', 'w') as f:
    f.write(commands_json)

print(f"Generated {len(commands)} operations")
