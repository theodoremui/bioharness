# Research proposal snapshots

The seven current proposals are in `notes/claude-brainstorm/ideas-claude-simplified/`. They are concise, standalone research ideas, each organized around a highlighted question, scientific rationale, focused study and interpretation. Together they contain 3,903 words, 79.4% fewer than the versions present at the start of this revision.

The latest [adversarial review and resolution record](proposal_snapshot_review.md) documents the scientific changes, remaining limitations and verification. Earlier `codex_review*.md` files describe previous drafts and remain historical records; their descriptions of length, figures, feasibility and appendices do not describe the current proposals.

## Active sources and rebuilding

`build/src/v1_*.md` through `build/src/v7_*.md` are synchronized with the current proposals. The `{-}` suffix on source headings preserves the unnumbered section titles during generation. The sources contain ordinary inline citations and no shared-background includes. The older files in `build/src/parts/` and the figure assets are retained but are not included in the current snapshots.

From the repository root, rebuild with:

```sh
python3 -B output/research-claude-explained/build/build.py docs/ideas-claude-explained \
  v1_stable-tool-agent-reframe \
  v2_measure-or-guess-evaluation \
  v3_measurement-grounded-rewards \
  v4_privileged-teacher-and-budgeted-levers \
  v5_world-model-transfer-and-known-answer-verification \
  v6_simplified-reward-what-can-be-checked \
  v7_final_rewarding-what-can-be-checked
```

Edit the active source files and rebuild to keep the generated documents aligned. The latest verification rebuilt all seven into a temporary directory and confirmed exact agreement with the delivered files.
