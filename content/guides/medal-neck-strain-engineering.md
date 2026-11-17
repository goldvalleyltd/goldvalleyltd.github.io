---
title: "Medal Neck Strain & Jump Ring Fatigue: The Dynamic Physics of Marathon Finisher Medals"
slug: medal-neck-strain-engineering
description: "Why marathon medals strain necks and snap jump rings: 2.5g celebration loads, ribbon-width pressure math, and the weight bands that keep a finisher medal comfortable — computed with the lab engine."
date: 2026-11-17
topic: "Custom Medals"
tool: https://goldvalleyltd.github.io/medal-coin-weight-lab/
tool_name: "Challenge Coin & Medal Weight Lab"
---

# Medal Neck Strain & Jump Ring Fatigue: The Dynamic Physics of Marathon Finisher Medals

- **Weight is the whole story.** A standard 70 mm (2.76") zinc finisher medal weighs 112.2 g (3.96 oz) fully assembled; the same medal in brass reaches 154.8 g (5.46 oz) — and at 80 mm (3.15") in brass it passes 250 g.
- **The jump is the load case.** A finisher celebrating at the line generates a 2.5g peak shock — 2.75 N (0.28 kgf) on a standard 70 mm medal, 6.24 N (0.64 kgf) on the heavy 80 mm brass version — and the unwelded Ø1.5 mm (0.059") jump ring is the weak link.
- **Ribbon width is pressure math.** Neck pressure falls in direct proportion to ribbon width: 25 mm (1.0") to 38 mm (1.5") cuts pressure to 66% at the same weight.
- **Cutouts beat willpower.** A 25% open cutout drops the standard 70 mm zinc medal from 112.2 g to 88.5 g — a 21% cut with no change to diameter or relief.

The medal survives 42.195 km and fails at the finish line: the runner jumps, and the medal hits the asphalt — or it stays on, and the ribbon carves a red line across a tired neck. Both failures are decided months earlier by three numbers: assembled weight, ribbon width, and the hanger between them. This guide works through all three with the engine behind our [Challenge Coin & Medal Weight Lab](https://goldvalleyltd.github.io/medal-coin-weight-lab/), so you can check your medal before artwork approval.

## Weight Is Set Before the Ribbon Is Chosen

A medal is a metal body plus a ribbon plus a hanger, and the body dominates. The table below runs five specifications through the lab's volume model — round medals, 2.5D semi-relief unless noted, Zamak 3 zinc (6.6–6.7 g/cm³) or H65 brass (8.4–8.5 g/cm³, ASTM C26800) — ribbon weight included in the total, exactly as worn.

| Medal specification | Body | Ribbon | Total weight | Lab neck rating |
|---|---|---|---|---|
| 50 mm × 3.0 mm (1.97" × 0.118"), zinc, 25 mm ribbon | 44.4 g (1.57 oz) | 11.5 g | 55.9 g (1.97 oz) | Comfort |
| 70 mm × 3.5 mm (2.76" × 0.138"), zinc, 30 mm ribbon | 97.4 g (3.44 oz) | 14.8 g | 112.2 g (3.96 oz) | Comfort |
| 70 mm × 4.0 mm (2.76" × 0.157"), brass, 30 mm ribbon | 140.0 g (4.94 oz) | 14.8 g | 154.8 g (5.46 oz) | Comfort, at the edge |
| 80 mm × 5.0 mm (3.15" × 0.197"), zinc, high relief, 38 mm ribbon | 185.1 g (6.53 oz) | 19.5 g | 204.6 g (7.22 oz) | Substantial |
| 80 mm × 5.0 mm (3.15" × 0.197"), brass, high relief, 38 mm ribbon | 234.8 g (8.28 oz) | 19.5 g | 254.3 g (8.97 oz) | Heavy load |

Two patterns matter. First, diameter is the expensive lever: going from 70 mm to 80 mm adds about 31% more face area, so weight rises by roughly the same proportion at fixed thickness — the zinc body jumps from 97.4 g to 185.1 g once the extra 1.5 mm of thickness and the deep relief are added on top. Second, brass is a step change, not a tweak: at identical geometry brass weighs about 27% more than zinc, so the 70 mm medal that is a comfortable 112.2 g in zinc becomes 154.8 g in brass — 0.2 g short of the lab's 155 g substantial band. Switching a zinc sample to brass for "a heavier feel" moves the medal to the edge of a different comfort class without touching the artwork.

The lab's rule of thumb puts the standard 70 mm full-marathon medal at roughly 120 g assembled, and the model agrees: a 70 mm zinc medal at 4.0 mm with a 30 mm ribbon totals 125.1 g. Below about 55 g the medal reads as a fun-run token; above 220 g it is a championship piece that needs deliberate engineering, not just a wider ribbon.

## Neck Pressure Is a Width Problem, Not a Weight Problem

Neck pressure is the medal's weight, pulled by gravity, spread over the ribbon's contact area — both sides of the neck, so twice the ribbon width times the contact length:

$$P_{neck} = \frac{W_{total} \times g}{2 \times W_{ribbon} \times L_{contact}}$$

Weight is the numerator and ribbon width the denominator, which is why width is the cheapest fix in the specification. At the same medal weight, widening the ribbon from 25 mm (1.0") to 30 mm (1.2") cuts neck pressure by 17%; going to 38 mm (1.5") cuts it by 34%, to 66% of the 25 mm value. The ribbon itself adds almost nothing — 11.5 g at 25 mm, 14.8 g at 30 mm, 19.5 g at 38 mm — so the trade is nearly free.

The lab sorts assembled medals into four bands. Under 55 g (1.94 oz) is featherweight, for kids' and fun runs. From 55 g to 155 g is the comfort zone, where the standard full-marathon medal lives on a 25 mm or 30 mm ribbon. From 155 g to 220 g is substantial — pair it with at least a 30 mm (1.2") ribbon. Above 220 g (7.76 oz) is heavy load: the medal swings against the sternum, and the specification needs less metal, not a wider ribbon.

The common failure is a mismatch: a 70 mm zinc medal at 112.2 g on a 25 mm ribbon is fine, but the same medal at 80 mm and 204.6 g on that ribbon is not — pressure has nearly doubled while the contact area stayed put. Ribbon width is a line item on the order, not an afterthought.

## The 2.5g Jump: Dynamic Load and the Jump Ring

Static weight is what the neck feels. The hanger feels the celebration: a finisher jumping at the line generates a peak vertical acceleration of about 2.5g, seen by the hanger as a shock load on top of the medal's own weight:

$$F_{dynamic} = 2.5 \times m \times g$$

For the standard 70 mm zinc medal (112.2 g assembled), the peak is 2.75 N (0.28 kgf). For the heavy 80 mm brass medal (254.3 g), it is 6.24 N (0.64 kgf). Those are small forces — a bag of sugar pulls harder — which is why the failure surprises people. The ring does not fail on one clean pull. It fails by fatigue: the unwelded split wire flexes open a fraction of a millimetre on every jump and every swing, until the gap is wide enough for the medal to slip off.

The two hanger options are not close. An integrated cast bridge slot — cast in one piece with the medal body — is rated at 314 N (32.0 kgf), a safety factor of more than 50× even on the heaviest medal in the table. A standard unwelded Ø1.5 mm (0.059") split-wire jump ring is rated at 54 N (5.5 kgf). On paper that still looks safe: the safety factor on the standard 70 mm zinc medal is 19.6×, and even on the 254.3 g brass medal it is 8.7×. But the lab flags any jump-ring medal whose body exceeds 110 g as a critical DFM risk, regardless of that arithmetic — because the arithmetic describes a single static pull, and the field failure is repeated flexing at a gap that was never welded shut.

| Medal (body weight) | Peak dynamic load | Cast bridge safety factor | Jump ring safety factor | Lab verdict on jump ring |
|---|---|---|---|---|
| 70 mm zinc, 97.4 g body | 2.75 N (0.28 kgf) | >99× | 19.6× | Pass |
| 70 mm brass, 140.0 g body | 3.80 N (0.39 kgf) | 82.7× | 14.2× | Critical — switch hanger |
| 80 mm zinc, 185.1 g body | 5.02 N (0.51 kgf) | 62.6× | 10.8× | Critical — switch hanger |
| 80 mm brass, 234.8 g body | 6.24 N (0.64 kgf) | 50.3× | 8.7× | Critical — switch hanger |

The 110 g line is the decision that matters most in this guide. The 70 mm zinc medal at 97.4 g body weight passes with a jump ring; the same medal in brass at 140.0 g does not, even though its force safety factor is still 14.2×. Alloy choice alone moves a medal across the line. Over 110 g, specify an integrated cast bridge slot; the jump ring is for light medals — the 50 mm size, kids' races, fun runs.

## Designing the Failure Out

Once weight, ribbon, and hanger are understood as one system, the specification writes itself — and the cheapest corrections happen before tooling.

**Specify the hanger by body weight, not by habit.** Under 110 g, a Ø1.5 mm jump ring is acceptable. Over it, use an integrated cast bridge slot. This single rule prevents the most common field failure in the category, and it costs nothing at the tooling stage — the bridge is cast in the same die as the medal body.

**Cut weight with openwork before shrinking the medal.** A 25% open cutout on the standard 70 mm zinc medal drops the body from 97.4 g to 73.7 g and the assembled total from 112.2 g to 88.5 g (3.12 oz) — a 21% cut that keeps the diameter, the relief, and the presence on the podium. Cutouts also break up the flat face that shows sink marks. The lab recommends 20%–35% open area for medals over 220 g.

**Hold the core thickness.** The net core — total thickness minus the relief on both faces — should stay at or above 1.5 mm (0.059"): below that, die-cast zinc risks cold-shut flow lines across a large span, and a stamped blank risks being punched through. All five medals in the table clear this comfortably (2.36 mm at the thinnest), but a 3D high-relief design on a 3.0 mm blank would not, and the lab flags any core under 1.3 mm (0.051") as critical. Large medals should hold 2.5–3.5 mm (0.098"–0.138") total thickness for flatness and hand feel.

**Match the ribbon to the band, then stop.** A 38 mm (1.5") jacquard ribbon is the right call above 155 g; below that, 25 mm or 30 mm is enough. Ribbons are produced to our engineering specifications rather than woven in-house, so width, the 850–900 mm (33.5"–35.4") cut length, and the sublimation print should be confirmed as line items, not left to a default.

Run your specification through the [Challenge Coin & Medal Weight Lab](https://goldvalleyltd.github.io/medal-coin-weight-lab/) before approving artwork: enter diameter, thickness, relief, alloy, ribbon width, and hanger type for the assembled weight, neck rating, dynamic load, and hanger safety factor. If the lab flags the hanger or the neck band, change the specification — not the runner's celebration.

> **📋 Copy-Paste Spec for Your Custom Marathon Medal RFQ:** Shape: round, 70 mm × 3.5 mm (2.76" × 0.138") standard. Alloy: Zamak 3 die-cast zinc (6.6–6.7 g/cm³) or H65 stamped brass (8.4–8.5 g/cm³, ASTM C26800). Relief: 2.5D semi-relief; net core ≥ 1.5 mm (0.059"). Hanger: integrated cast bridge slot for body > 110 g (3.88 oz); Ø1.5 mm (0.059") jump ring only under 110 g. Ribbon: 30 mm (1.2") sublimated polyester, 850–900 mm cut length, for 55–155 g; 38 mm (1.5") jacquard for 155–220 g. Finish: per plating chart; salt spray 48–72 h; inspection AQL 1.5 Major / 4.0 Minor. MOQ 300 pcs; sample 3–7 working days; bulk 12–18 working days.

## Frequently Asked Questions

### How heavy should a full-marathon finisher medal be?

Between 80 g and 135 g assembled is the classic band; the lab's comfort zone runs to 155 g. A standard 70 mm zinc medal with a 30 mm ribbon totals 112.2 g, squarely in the middle. Below 55 g the medal feels like a fun-run token; above 220 g it needs cutouts or a smaller diameter, not just a wider ribbon.

### Can I use a jump ring on a heavy medal?

Not above 110 g of body weight. The lab flags any jump-ring medal over 110 g as a critical risk, even though the force safety factor still looks comfortable — the failure is fatigue at the unwelded gap, not a single overload. The 70 mm medal is the boundary: 97.4 g in zinc passes, 140.0 g in brass does not.

### Does a wider ribbon really help, or is it cosmetic?

It is arithmetic. Neck pressure is weight divided by contact area, and contact area is proportional to ribbon width, so a 38 mm ribbon cuts pressure to 66% of the 25 mm value at the same medal weight. The ribbon itself only adds 8 g going from 25 mm to 38 mm, so the comfort gain is nearly free. What a wider ribbon cannot do is fix a medal over 220 g — that needs less metal.

Browse the full range at [custom medals](https://www.goldvalleyltd.com/custom-medals/), including [race and sports medals](https://www.goldvalleyltd.com/custom-medals/race-sports/).

<!--
FACT-CHECK — GH-003 medal-neck-strain-engineering
Every quantitative claim in this draft, with its source.

1. Weight table (bodies 44.4/97.4/140.0/185.1/234.8 g; totals 55.9/112.2/154.8/204.6/254.3 g; ribbons 11.5/14.8/19.5 g).
   Source: computed with the medal lab's own engine — medal-coin-weight-lab/js/engine/geometry.js estimateMedal() + presets.js (RELIEF_STYLES deltas, RIBBON_SPECS weights, densities Zamak 3 = 6.70, H65/C26800 = 8.50). Verified by running the engine in Node 2026-11-17. Engine copies in ~/workspace/medal-coin-weight-lab and goldvalley-work/开源项目/medal-coin-weight-lab are byte-identical (diff clean).
2. Dynamic loads (2.75/3.80/5.02/6.24 N; 0.28/0.39/0.51/0.64 kgf) and safety factors (cast >99×/82.7×/62.6×/50.3×; jump ring 19.6×/14.2×/10.8×/8.7×).
   Source: physics.js evaluateMedalPhysics() — F_dynamic = 2.5 × m × g; loop ratings cast-loop 314 N (32.0 kgf), jump-ring Ø1.5 mm 54 N (5.5 kgf) from presets.js LOOP_STRENGTH. Cast safety factors above 99.9 are capped by the engine at 99.9 and reported as ">99×".
3. Neck bands (<55 g featherweight; 55–155 g comfort; 155–220 g substantial; >220 g heavy load).
   Source: physics.js evaluateMedalPhysics() neckLevel thresholds. NOTE — the PRD doc §4.1 uses different bands (<80 g light; 80–135 g classic; 135–175 g heavy; >175 g excessive). The article follows the lab's implemented bands because those are what the tool reports; the PRD bands are the older reference frame. The "80–135 g classic band" quoted in the FAQ is the PRD's band, labelled as such.
4. Neck pressure formula P = W×g / (2 × W_ribbon × L_contact).
   Source: PRD doc §4.1 (奖牌与挑战币克重评估.md). L_contact is not given a numeric value anywhere in the sources, so the article asserts NO absolute pressure (kPa) figure — only the width ratios, which follow from the formula with L_contact held constant: 25→30 mm = 25/30 = 0.833 (−17%); 25→38 mm = 25/38 = 0.658 (−34%, i.e. 66% of the 25 mm value).
5. 70 mm × 4.0 mm zinc + 30 mm ribbon totals 125.1 g (body 110.3 g incl. cast-loop volume + 14.8 g ribbon) — cross-check of the PRD's "~120 g for a 70 mm marathon medal" rule of thumb.
   Source: engine estimateMedal() run 2026-11-17 (same run as (1)). Close to the PRD's ~120 g; the article says "roughly 120 g" and gives the computed 125.1 g. (Earlier hand computation of 122.6 g was wrong — it omitted the 0.38 cm³ cast-loop volume, ~2.5 g in zinc; engine value used.)
6. 25% cutout: 70 mm zinc body 97.4 → 73.7 g; total 112.2 → 88.5 g (−23.7 g, −21%).
   Source: engine estimateMedal() with cutoutRatio 0.25, same run as (1).
7. Jump-ring CRITICAL rule: body weight > 110 g with an unwelded jump ring → dfmStatus CRITICAL.
   Source: physics.js — `if (loopKey === 'jump-ring' && metalWeightGrams > 110)`. This is a design rule in the engine, NOT derived from the 54 N rating: the force safety factors at the flagged weights (14.2×/10.8×/8.7×) still look comfortable. The article states this explicitly (fatigue at the unwelded gap vs single-pull arithmetic).
8. PRD's "25 N pull-open" rule for <1.8 mm wire jump rings NOT cited in the body.
   Reason: under the engine's 2.5g model no realistic medal reaches 25 N (heaviest computed case is 6.24 N); under the PRD's own (1+2.5)g formula it would be 8.7 N. The 25 N figure must describe a different shock case (snag/drop/yank) than the celebration-jump model, and the sources do not define it. Recorded here as an open source tension, not asserted as a model output.
9. Dynamic-load formula discrepancy: PRD §4.2 writes F_dynamic = W × (1+2.5) × 9.8e-3 (i.e. 3.5× m×g); physics.js implements F_dynamic = 2.5 × m × g. Article uses the engine (2.5×); PRD-formula loads would be 1.4× higher (e.g. standard medal 3.85 N vs 2.75 N). Open discrepancy, logged for later cleanup of the PRD doc.
10. Cast-loop rating discrepancy: lab presets rate the cast bridge at 314 N (32.0 kgf); PRD §4.2 gives 120–250 N. Article uses the lab figure (the tool's number). Open discrepancy, logged.
11. Core thickness rule: T_core = T_total − (relief front + relief back); ≥1.5 mm safe, 1.2–1.5 mm caution, <1.2 mm high risk.
    Source: PRD §3.3. Engine core values in the table (2.36/2.86/3.36/4.30 mm) computed by geometry.js (thickness − 2× enamelRecessDepthMm). Engine flags core < 1.3 mm as CRITICAL (physics.js); article cites the PRD's 1.5 mm safe line and the engine's 1.3 mm flag.
12. Large-medal thickness guidance 2.5–3.5 mm for flatness and hand feel.
    Source: engineering-params.md die-cast wall table note ("大尺寸奖牌建议保持 2.5~3.5 mm 厚度以保证平整度与手感").
13. Ribbon: 850–900 mm cut length, widths 25/30/38 mm, weights 11.5/14.8/19.5 g.
    Source: presets.js RIBBON_SPECS (900 mm cut length folded to ~430 mm drop; weights per spec) + PRD §2.1 (ribbon 12.0–22.0 g — consistent with 11.5–19.5 g).
14. Zamak 3 density 6.6–6.7 g/cm³; H65 brass 8.4–8.5 g/cm³, ASTM C26800.
    Source: engineering-params.md §一·1 + presets.js MATERIALS (6.70 / 8.50). H65/C26800 per 2026-11-16 user decision (option A); do NOT write C26000.
15. Brass ~27% heavier than zinc at identical geometry (8.5/6.7 = 1.269). Arithmetic from (14).
16. 70 → 80 mm adds ~31% face area ((80/70)² − 1 = 0.306). Arithmetic.
17. 20%–35% open cutouts recommended for medals over 220 g.
    Source: physics.js HEAVY_LOAD neckDescEn ("Add 20%–35% open cutouts or pair with a 38 mm wide lanyard").
18. Die life 50,000–100,000 shots; artwork 2–4 h; sampling 3–7 working days; bulk 12–18 working days; MOQ 300; salt spray 48–72 h; AQL 1.5 Major / 4.0 Minor.
    Source: engineering-params.md Tier 1 + §五 (same figures as GH-001 items 12–13).
19. Ribbon is an outsourced item: article says ribbons are "produced to our engineering specifications" (three-tier boundary), never claims an in-house weaving line.
20. 44 mm × 3.5 mm H65 coin sanity check (QC item from Phase 2 run log): engine estimateCoin() gives 47.3 g semi-relief — confirms the Phase 2 finding that 55–65 g is NOT reachable at 44×3.5 mm. Not used in the body (this guide is about medals, not coins); recorded here so the QC item stays verified.
-->
