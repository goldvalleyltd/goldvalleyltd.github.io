---
title: "Center of Gravity & Toppling Moments in Zinc Alloy Wine Stoppers: A Physical Modeling Approach"
slug: wine-stopper-center-of-gravity
description: "Why tall decorative wine stoppers tip over: CG height vs. the 9.25 mm pivot, toppling moments, and the fixes that keep a stag head upright."
date: 2026-11-16
topic: "Wine Stoppers"
tool: https://goldvalleyltd.github.io/winestopper-physics-lab/
tool_name: "Wine Stopper Physics Lab"
---

# Center of Gravity & Toppling Moments in Zinc Alloy Wine Stoppers: A Physical Modeling Approach

- **Height beats weight.** A stopper tips when its composite center of gravity climbs past +25 mm (0.98") above the bottle rim or its anti-tilt safety factor falls below 1.35× — our lab grades either condition HIGH RISK.
- **The pivot is tiny.** The whole assembly balances on the 9.25 mm (0.364") radius of an 18.5 mm (0.73") bore, so every gram above the rim works against stability.
- **The default stag head is already top-heavy.** A 55 × 35 × 65 mm (2.17" × 1.38" × 2.56") Zamak 3 stag at 30% coring weighs 104.1 g (3.67 oz) with a composite CG of +27.6 mm (1.09") — high-risk as drawn; 50% deep coring plus a 38 g (1.34 oz) stainless counterweight stem brings it to +20.1 mm (0.79").
- **Sealing is a separate system.** Stepped silicone rings (17.0–17.5 mm / 0.67"–0.69" at the base, 19.5–20.0 mm / 0.77"–0.79" at the top) grip a bore of 18.5 mm ± 0.5 mm (0.73" ± 0.020"), and the metal head never touches the wine — the stainless core and the silicone do the sealing.

The stag head is magnificent on the shelf — antlers, muscle, a mirror-gold finish. In the bottle, it leans. A week later the lean is a tilt, the silicone rib on one side is permanently compressed, and air is creeping past the seal. The failure has nothing to do with how well the stopper was made and everything to do with statics: a tall metal ornament puts the center of gravity far above a pivot no wider than a bottle neck, and gravity does the rest.

## The Lever You Cannot See: CG Height Against a 9.25 mm Pivot

A wine stopper is two assemblies pretending to be one object: a decorative metal head above the rim and a sealing stem below it. Stability is decided by where their combined center of gravity (CG) sits relative to the rim — and the lever working against it is brutally short. The standard Bordeaux/Burgundy bottleneck has a bore of 18.5 mm (0.73"), which means the whole stopper pivots on a radius of just 9.25 mm (0.364"). Every millimeter of CG height above the rim multiplies the overturning moment; every gram of head mass multiplies it again.

Our lab models this as rigid-body statics on a 15° tilt, the angle a bottle reaches when it is pulled from a crowded shelf or knocked in a door rack. The composite CG is the mass-weighted average of the head (above the rim, plus an 8.0 mm / 0.315" transition collar between the rim and the ornament base) and the stem (below the rim, where its mass counts negative and pulls the CG down). The overturning moment is the assembly's weight × CG height × sin(15°). Against it stands the restoring moment: weight × the 9.25 mm pivot radius × cos(15°), plus the friction torque bonus from the seal gripping the bore wall — 9.5 N·mm (1.35 oz·in) for a standard silicone-ribbed stem, 13.5 N·mm (1.91 oz·in) for the heavy stainless counterweight stem, and 6.5 N·mm (0.92 oz·in) for a traditional cork base. The anti-tilt safety factor is simply restoring moment divided by overturning moment, and the critical tipping angle follows from the ratio of the support arm to the CG height.

That model sorts every design into three grades. Any single condition triggers the grade — a stopper can pass on safety factor and still fail on CG height, as the default stag head below does:

| Grade | Composite CG above rim | Safety factor at 15° tilt | Decorative top mass |
|---|---|---|---|
| STABLE | ≤ +15 mm (0.59") | ≥ 2.1× | ≤ 90 g (3.17 oz) |
| MARGINAL | +15 to +25 mm (0.59"–0.98") | 1.35×–2.1× | 90–135 g (3.17–4.76 oz) |
| HIGH RISK | > +25 mm (0.98") | < 1.35× | > 135 g (4.76 oz) |

The practical sweet spot for the decorative top is 45–75 g (1.59–2.65 oz): heavy enough to feel substantial in the hand, light enough to keep the CG in check. Above 90 g the design is already marginal before the height is even considered, and a solid-cast Zamak 3 ornament of any real size gets there fast — a solid head in the 60–80 g range is already enough to unbalance the assembly, which is why coring is not an optional refinement but the first stability decision.

## Worked Example: The 55 × 35 × 65 mm Stag Head

Numbers make the trade-off concrete. Take the lab's default stag head: a 55 × 35 × 65 mm (2.17" × 1.38" × 2.56") bounding box, a figurine fullness factor of 0.18 (antlers and open space mean the sculpture fills only about 18% of its bounding box), cast in Zamak 3. Four configurations, all evaluated at a 15° tilt on the standard 18.5 mm bore:

| Configuration | Top mass | Composite CG | Safety factor | Verdict |
|---|---|---|---|---|
| Solid Zamak 3 stag, standard stem | 148.6 g (5.24 oz) | +28.7 mm (1.13") | 1.95× | HIGH RISK |
| 30% cored stag, standard stem (lab default) | 104.1 g (3.67 oz) | +27.6 mm (1.09") | 2.29× | HIGH RISK |
| 50% deep-cored stag + heavy SUS304 stem | 74.3 g (2.62 oz) | +20.1 mm (0.79") | 4.08× | MARGINAL |
| 6061 aluminium stag (30% cored), standard stem | 42.6 g (1.50 oz) | +16.9 mm (0.67") | 5.24× | MARGINAL |

Read the table from the top down and the physics tells its own story. The solid casting is the worst of every world: 148.6 g of head mass, a CG nearly 29 mm above the rim, and — beyond the statics — a thick solid section that risks internal shrinkage porosity and surface sink marks under plating. Standard 30% core-pulling (a uniform wall of about 3.0 mm / 0.118") cuts the top to 104.1 g, but the CG barely moves, because coring removes metal from the middle of the form, not from the top of it — the centroid sits at about 45% of the ornament's height either way, and 65 mm of height is simply a long lever. The safety factor clears 2.1×, but the CG at +27.6 mm still triggers HIGH RISK on height alone.

The fixes that actually move the CG work from below and from the material, not from the sculpture. Deep 50% coring (a wall of about 2.0 mm / 0.079") brings the top to 74.3 g — inside the 45–75 g sweet spot — and pairing it with the heavy SUS304 stainless counterweight stem (38.0 g / 1.34 oz, its own centroid 21.0 mm / 0.83" below the rim) drags the composite CG down to +20.1 mm and lifts the safety factor to 4.08×. Switching the head alloy to 6061 aluminium (2.70 g/cm³ against Zamak 3's 6.60 g/cm³) cuts top mass by about 59% at identical geometry and reaches +16.9 mm with the standard stem. Shortening the decorative transition neck by 4–6 mm (0.157"–0.236") is the remaining lever when the sculpture itself cannot change.

Be honest about the floor, though: a 65 mm tall figurative topper stays MARGINAL even after the best fixes, because the height itself sets the CG. The remedies buy margin and a much larger safety factor — they do not repeal the geometry. If a design must grade fully STABLE, the top has to come down in height, or the form has to change toward a compact profile: a solid T-bar or cylindrical cap fills about 65% of its bounding box and keeps its centroid low, where a figurine fills 18% and carries its mass high. Run your own dimensions through the [Wine Stopper Physics Lab](https://goldvalleyltd.github.io/winestopper-physics-lab/) before committing to tooling — the model evaluates any bounding box, alloy, coring level, and stem combination, including uploads of your own 3D mesh.

## Balance Is Only Half the Job: Bore Fit and the Seal

A stopper that stands upright but leaks is still a failure, and sealing obeys a different set of dimensions than balance. The bore it must grip is the same 18.5 mm (0.73") neck, with a ± 0.5 mm (± 0.020") tolerance across bottle makers — a full millimeter of variation that a single fixed-diameter plug cannot cover. The working answer is a stepped silicone ring stack: three to five tapered rings whose outside diameter grows from about 17.0–17.5 mm (0.67"–0.69") at the bottom ring to about 19.5–20.0 mm (0.77"–0.79") at the top. The lower rings guide and center the stem on insertion; the upper rings compress against the bore wall and lock with elastic friction. The seal specification is a Shore A 45–55° food-grade silicone three-rib ring, and a comfortable pull force for the finished stopper is 20–35 N (4.5–7.9 lbf) — firm enough to trust, light enough to open one-handed.

One boundary is absolute and worth stating plainly: the decorative metal head never touches the wine. Wine is acidic (pH 3.0–3.8), and an unprotected zinc or brass surface in contact with it corrodes and leaches metal into the bottle. The head stays above the rim as a handle; everything below the rim is a food-grade stainless steel core (SUS304, or SUS316L for high-acid or long-soak use) carrying the silicone rings, which do all of the sealing. The governing requirements are GB 4806.9-2023 for the metal food-contact parts and FDA 21 CFR 177.2600 for the silicone — the reason the stem is stainless and the seal is silicone is regulatory, not decorative.

Fit has one more edge case worth knowing before you order. The stepped rings are sized for the standard straight Bordeaux bore; on flared champagne or Burgundy necks with a bore wider than 19.2 mm (0.756"), the same stopper can show slight lateral play, because the rings meet the wall higher up the taper with less compression. If your bottles run wide, say so in the RFQ — the ring stack can be specified to match.

> **📋 Copy-Paste Spec for Your Custom Wine Stopper RFQ:** Head: Zamak 3 die-cast (6.60 g/cm³) or 6061 aluminium (2.70 g/cm³); top mass target 45–75 g; core-pulling 30% standard (wall ~3.0 mm) or 50% deep (wall ~2.0 mm). Stem: SUS304 stainless core + Shore A 45–55° food-grade silicone 3-rib stepped rings (17.0–17.5 mm → 19.5–20.0 mm OD); bore 18.5 mm ± 0.5 mm; pull force 20–35 N. Stability: composite CG ≤ +15 mm target, safety factor ≥ 2.1× at 15° tilt. Finish: per plating chart; salt spray 48–96 h. MOQ 300 pcs; sample 3–7 working days; bulk 12–18 working days.

## Frequently Asked Questions

### How heavy can the decorative top be before the stopper tips?

The sweet spot is 45–75 g (1.59–2.65 oz). Above 90 g (3.17 oz) the design grades MARGINAL on mass alone, and above 135 g (4.76 oz) it grades HIGH RISK — before height is even considered. A solid-cast Zamak 3 ornament reaches those numbers quickly, which is why 30–50% core-pulling is standard practice rather than an upgrade. Height matters as much as mass: a 65 mm tall topper can grade MARGINAL even at 74 g, because its CG sits high.

### Will one stopper fit all my bottles?

One stopper fits the standard straight Bordeaux/Burgundy bore of 18.5 mm ± 0.5 mm (0.73" ± 0.020"), thanks to the stepped ring stack that spans 17.0–20.0 mm. Flared champagne or Burgundy necks wider than 19.2 mm (0.756") may show slight lateral play — if your bottles run wide, specify it in the RFQ so the ring stack can be matched to your neck.

### Is the metal safe next to wine?

The metal head never contacts the wine. Everything below the rim is a food-grade stainless steel core (SUS304, or SUS316L for high-acid wines) carrying food-grade silicone sealing rings; the decorative head stays above the rim as a handle. The metal food-contact parts follow GB 4806.9-2023 and the silicone follows FDA 21 CFR 177.2600. Brass and zinc-alloy heads are handle-only by design — never sealing surfaces.

Browse the range at [metal wine stoppers](https://www.goldvalleyltd.com/wine-barware/wine-stoppers/), including the [stag-head wine stopper](https://www.goldvalleyltd.com/wine-barware/wine-stoppers/stag-head-wine-stopper/) that this guide models.

<!--
FACT-CHECK — GH-002 wine-stopper-center-of-gravity
Every quantitative claim in this draft, with its source.

1. Standard bore 18.5 mm ± 0.5 mm; pivot radius 9.25 mm.
   Source: teardown 酒塞的系统性拆解.md §三 (bore 18.5 ± 0.5 mm); presets.js BOTTLE_CONSTANTS (standardBoreDiameterMm 18.5, pivotRadiusMm 9.25).
2. 15° tilt evaluation angle; collar adds 8.0 mm to effective CG height.
   Source: physics.js evaluateStability (tiltAngleDeg default = BOTTLE_CONSTANTS.criticalTiltAngleDeg 15.0; effectiveTopZ = topZ + 8.0; comment: 16.0 mm upper transition neck collar).
3. Overturning moment = weight × CG height × sin(15°); restoring = weight × pivot radius × cos(15°) + friction bonus; safety factor = restoring / overturning; critical angle = atan(support arm / CG height).
   Source: physics.js evaluateStability §§3–4 (formulas, no numbers invented).
4. Friction torque bonus: zinc-silicone stem 9.5 N·mm; heavy SUS304 stem 13.5 N·mm; brass-cork 6.5 N·mm.
   Source: presets.js BASE_CONFIGS (frictionTorqueBonusNmm).
5. Grade thresholds: STABLE CG ≤ +15 mm, Sf ≥ 2.1, top ≤ 90 g; MARGINAL CG > 15 mm or Sf < 2.1 or top > 90 g; HIGH RISK CG > 25 mm or Sf < 1.35 or top > 135 g. Any single condition triggers the grade.
   Source: physics.js evaluateStability §5 (if/else-if thresholds, OR logic).
6. Top-mass sweet spot 45–75 g.
   Source: physics.js MARGINAL recommendation ("bring top mass into the 45–75 g sweet spot").
7. Solid Zamak 3 head of 60–80 g unbalances the assembly.
   Source: teardown §二 route A ("若做实心重达 60~80 g 会导致插瓶后重心严重失衡倾倒").
8. Worked-example table (148.6/104.1/74.3/42.6 g; CG +28.7/+27.6/+20.1/+16.9 mm; Sf 1.95/2.29/4.08/5.24×).
   Source: computed with the lab's own engine — geometry.js estimateByBoundingBox (55 × 35 × 65 mm, k = 0.18) + physics.js evaluateStability — verified by running the engine in Node 2026-11-16. Lab defaults (55/35/65 mm) from app.js state.
9. Coring levels: 30% standard, wall ~3.0 mm, η = 0.70; 50% deep, wall ~2.0 mm, η = 0.50; 15% shallow, wall 4.5 mm, η = 0.85.
   Source: presets.js HOLLOWING_LEVELS.
10. Solid casting > 15 mm cross-section → shrinkage porosity / sink marks.
    Source: presets.js HOLLOWING_LEVELS solid warning.
11. Sculpted-bust centroid at ~45% of height (centroidRatio = 0.45 + (1−η) × 0.12).
    Source: geometry.js estimateByBoundingBox.
12. Shape fullness factors: figurine k = 0.18; column/T-bar k = 0.65; geometric 0.48; crest 0.32.
    Source: presets.js SHAPE_PRESETS.
13. Base configs: zinc-silicone stem 26.5 g, centroid −19.5 mm; heavy SUS304 stem 38.0 g, centroid −21.0 mm; brass-cork 22.0 g, centroid −18.0 mm.
    Source: presets.js BASE_CONFIGS.
14. Densities: Zamak 3 6.60, Zamak 5 6.70, SUS304 7.93, H65 8.50, 6061 Al 2.70 g/cm³.
    Source: presets.js MATERIALS (within engineering-params.md §一·1 ranges).
15. 6061 aluminium cuts top mass ~59% vs Zamak 3 at identical geometry (2.70/6.60 = 0.409).
    Source: arithmetic from (14); lab computation cross-check: 104.1 g → 42.6 g.
16. Shorten transition neck by 4–6 mm.
    Source: physics.js HIGH_RISK recommendation.
17. Stepped rings: 3–5 layers; bottom OD 17.0–17.5 mm → top OD 19.5–20.0 mm.
    Source: teardown §三.
18. Shore A 45–55° food-grade silicone 3-rib rings.
    Source: teardown 酒塞的系统性拆解.md §二 (line 26: 邵氏硬度优选 Shore A 45°~55°). RESOLVED by QC 2026-11-16: the lab presets say Shore A 60±5, but the teardown (product knowledge base, with the engineering rationale) wins for the article. The lab preset discrepancy is logged for later cleanup. RESOLVED 2026-11-16 evening: user chose A; lab presets now say Shore A 45–55 (goldvalley-work c34b84b, org d6a147c).
19. Comfortable pull force 20–35 N (4.5–7.9 lbf).
    Source: task brief + GitHub_Pages内容站实施方案.md guides matrix (silicone O-ring row, "20~35 N 舒适拔出力实测"). NOT in teardown or lab files — flagged to parent.
20. Wine pH 3.0–3.8; metal head never touches wine; SUS304 core (SUS316L for high-acid/long-soak); silicone does the sealing.
    Source: teardown §二 (food-safety red line; SUS304 standard, SUS316L for high-acid) + §五 (physical isolation rule).
21. GB 4806.9-2023 (metal food-contact) and FDA 21 CFR 177.2600 (silicone).
    Source: teardown §五. Cited as governing requirements for the parts, not as factory certifications.
22. Flared necks > 19.2 mm bore → slight lateral play.
    Source: physics.js MARGINAL summary ("flared champagne/burgundy necks (>19.2 mm bore) may exhibit slight lateral play").
23. Salt spray 48–96 h (teardown §五, stopper-specific); MOQ 300; sample 3–7 working days; bulk 12–18 working days; artwork 2–4 h.
    Source: teardown (salt spray); engineering-params.md Tier 1 + §五 (commercial baseline). QC 2026-11-16: draft originally said 48–72 h (params doc premium grade); corrected to the product-specific 48–96 h from the teardown.
24. Draft angle 1°–2° for stopper handles (teardown §二) — NOT used in the draft; omitted to avoid confusion with the general 1.5°–3.0° die-cast draft in engineering-params.md §二·2.
-->
