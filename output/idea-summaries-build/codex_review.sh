#!/usr/bin/env bash
# Two Codex review modes used for proposals 05 to 08.
#
# 1) Visual figure review (Codex looks at rendered PNGs):
#    output/idea-summaries-build/codex_review.sh figures OUT.md "focus text" a.png b.png ...
# 2) Adversarial review of the working tree through the codex plugin (reads files, including untracked):
#    output/idea-summaries-build/codex_review.sh adversarial OUT.md "focus text"
set -euo pipefail
mode="$1"; out="$2"; focus="$3"; shift 3
ROOT=/Users/theodoremui/dev/bioharness
cd "$ROOT"
mkdir -p "$(dirname "$out")"
if [ "$mode" = figures ]; then
  args=()
  for f in "$@"; do args+=("--image=$f"); done
  prompt="You are an adversarial reviewer of scientific figures for a research proposal. The attached PNGs are rendered at 2x from SVG and will be displayed about 850 px wide. Try hard to find reasons each figure should not ship. For EACH image, by file order, report: (a) overlapping or colliding text, (b) lines or arrows that cross text or other arrows confusingly, (c) arrows whose direction or endpoints are ambiguous, (d) text too small to read at display size, (e) excess text that belongs in a caption, (f) the one main point and whether a reader gets it in 5 seconds, (g) concrete fixes with coordinates or element names. Then give a verdict per figure: ship / fix / redraw. Focus: ${focus}. Do not run commands or modify files."
  echo "$prompt" | timeout 570 codex exec -s read-only "${args[@]}" - > "$out.raw" 2>&1 || true
  # keep only the final answer after the last 'codex' marker
  awk '/^codex$/{buf=""; keep=1; next} keep{buf=buf $0 "\n"} END{printf "%s", buf}' "$out.raw" > "$out"
  [ -s "$out" ] || cp "$out.raw" "$out"
elif [ "$mode" = adversarial ]; then
  timeout 570 node ~/.claude/plugins/cache/openai-codex/codex/1.0.6/scripts/codex-companion.mjs adversarial-review --wait --scope working-tree "$focus" > "$out" 2>&1 || true
  # The plugin sends the whole working-tree diff; when that exceeds Codex's input limit (or the run
  # produced nothing), rerun the plugin's own adversarial-review prompt through codex exec, scoped to
  # the files named in the focus text, which Codex reads from disk itself.
  if grep -q "Input exceeds the maximum length" "$out" || [ "$(wc -c < "$out")" -lt 600 ]; then
    tmpl=~/.claude/plugins/cache/openai-codex/codex/1.0.6/prompts/adversarial-review.md
    prompt=$(python3 - "$tmpl" "$focus" <<'PY'
import sys
t = open(sys.argv[1]).read()
t = t.replace('{{TARGET_LABEL}}', 'the files named in the user focus (read them from disk in this repository)')
t = t.replace('{{USER_FOCUS}}', sys.argv[2])
t = t.replace('{{REVIEW_COLLECTION_GUIDANCE}}', 'Read the named files in full with shell commands before judging.')
t = t.replace('Return only valid JSON matching the provided schema.', 'Return a markdown report: a verdict line (approve or needs-attention), a terse summary, then findings with severity, file and line range, confidence, and a concrete recommendation.')
print(t)
PY
)
    { echo "# Codex Adversarial Review (plugin prompt via codex exec; the working-tree diff exceeded the plugin's input limit)"; echo; } > "$out"
    echo "$prompt" | timeout 570 codex exec -s read-only - > "$out.raw" 2>&1 || true
    awk '/^codex$/{buf=""; keep=1; next} keep{buf=buf $0 "\n"} END{printf "%s", buf}' "$out.raw" >> "$out"
  fi
else
  echo "unknown mode $mode" >&2; exit 2
fi
echo "wrote $out ($(wc -w < "$out") words)"
