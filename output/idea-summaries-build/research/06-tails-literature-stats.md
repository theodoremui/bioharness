# Proposal 06 (tail drift): literature sweep, statistics, selection theory and clinical measurement

Status: IN PROGRESS (skeleton created 2026-11-24). Sections are filled step by step.

## 0. Searches run

Progress log (interim, kept for interruption safety):
- Searches 1 to 18 run (selection on noisy estimates; Hashimoto repeated loss minimization; RSI subgroup degradation; bio-creep; e-values; Fisher geometric model; capability erosion; prompt-optimization subgroup harm; SWE-bench Multilingual; Global-MMLU and MGSM; optimizer's curse; Lande-Arnold; Seldonian; Ladder; bias bounties; Cooper-Lenski; rich-get-richer SSL; spectrum bias; markerless pose in older adults; Lusardi falls review; self-evolving agent acceptance gates).
- Leads to verify: SAGE 2609.36043, Self-Evolving Agent Harness 2610.18813, held-out selection 2606.28374, winner's curse 2610.09239 (fetched: mean only), capability erosion 2605.09315 (fetched: task-distribution forgetting, CPE fix), fragility 2608.18066 (fetched: variance and order, no subgroups), Bertran-Roth-Wu 2606.11045 (fetched: compression, no subgroups).

## 1. Closest prior works

(interim notes; final table below replaces these)
- SAGE 2609.36043 (Wang et al., 28 Sep 2026): per-item paired one-sided test per edit; no groups, no cumulative guarantee. VERIFIED.
- Self-Evolving Agent Harness 2610.18813 (Wei et al., 13 Oct 2026): continual-PAC retention bound with regression budget; no subgroups in abstract. VERIFIED.
- RSEA 2606.28374 (Nguyen et al., 17 Jun 2026): held-out non-regression gate at benchmark level. VERIFIED.
- Capability erosion 2605.09315 (Yu et al., 10 May 2026): erosion of earlier task distributions; CPE fix. VERIFIED.
- Winner's curse 2610.09239 (Hu and Tang, 7 Oct 2026): mean-only selection noise. VERIFIED.
- Feng, Emerson, Simon bio-creep arXiv 1912.12413 / Biometrics 2021: online non-inferiority with alpha-investing; constant population, no subgroups in abstract. VERIFIED.
- Hashimoto et al. ICML 2018 arXiv 1806.08010: ERM amplifies disparity through retention dynamics; DRO fix. VERIFIED.
- Zhu, Luo, Liu ICLR 2022 arXiv 2110.06282: SSL rich-get-richer. VERIFIED.
- Globus-Harris, Kearns, Roth arXiv 2201.10408 (FAccT 2022 per ACM DL search result): bias bounties, group-wise updates with no tension. VERIFIED (arXiv); venue from ACM DL search hit.
- Yan et al. CVPR 2021 arXiv 2011.09161: negative flips. VERIFIED.
- La Cava and Moore GECCO 2020 arXiv 2004.13282: lexicase over protected-group intersections. VERIFIED.
- Cooper and Lenski Nature 2000 (Europe PMC): unused functions lost mostly EARLY, via antagonistic pleiotropy. VERIFIED. (Counter-evidence to the late-specialization prediction.)
- Martin and Lenormand Evolution 2015: Fisher geometric model across environments. VERIFIED (abstract does not state dependence on distance to optimum).

## 2. Is the core idea already done?

(pending)

## 3. Scores

(pending)

## 4. Sharpenings

(pending)

## 5. Second domain recommendation

(pending)

## 6. Key citations

(pending)

## 7. Unverified items

(pending)
