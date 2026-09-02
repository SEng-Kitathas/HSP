# Current Status

- Mode: BUILD-COMMIT experiment complete; live promotion not entered.
- Mainline: Pass 345 remains last clean mainline; HSP v0 remains research-only.
- Pass 346 v0.2 bounded-read dogfood is complete with final verdict **NO WINNER**.
- Both initial arms were independently sealed before hidden-evaluator reveal and passed visible 6/6 + initial hidden hostile 5/5.
- Hidden maintenance M3 (`tail_lines`) was independently implemented across core, HTTP wire/route, lab-native project read, and imported action schema.
- First M3 seals were superseded after CSC byte review found 4,568 CRLFs in the ACTIVE schema had been normalized despite semantic tests being green.
- Byte-clean replacement A tree: `b702382494803c2157dd87a4dacf45926099cf58bd5e2ca6031bb868d8fad4da`; replacement seal `015c2340ddc2948edaa1cbd5b4f21018a248e8a654d2cb979dccb3d0c5a5c4ad`.
- Byte-clean replacement B tree: `2fa75e3f085f415e32ad131ae606d302192436d5ee4fd47896acfd060071a830`; replacement seal `d9927501597ac88ac1bfd5a527b247c1d45b79c1428524ba5ae8d1c4e0f17657`.
- Final qualification: A arm tests 8/8, B 13/13; both visible 6/6, M3 9/9, original hidden hostile replay 5/5, compile PASS.
- CSC rejected A clean promotion because bounded `read_many` success reports false default metadata (`size_bytes:0,truncated:false`).
- CSC rejected B clean promotion because its metadata repair compares decoded returned bytes to raw source bytes; unbounded CRLF normalization yields false `truncated:true`, and the metadata referent was not normatively established.
- HSP signal is mixed: B's parent/evidence contract found a seam A missed, but B's lowering made an under-earned semantic choice at that seam. HSP superiority is not earned.
- Final adjudication: `experiments/pass346/results_2026-09-02/PASS346_FINAL_ADJUDICATION_2026-09-02.md`, SHA-256 `4ab3cce22a37c46fe72d61b3cb70d33244b1b1b4744f9c564ae509d34abb08e6`.
- Compact evidence mirror: `experiments/pass346/results_2026-09-02/RESULTS_INDEX.json`, SHA-256 `8a9dc91a287117b6edbb186f7baad2ce11cf48b53631f86536822703b3894060`.
- Full isolated arm trees remain in the local Pass 346 project and are intentionally not duplicated into Git.
- Live receiver source was not mutated by Pass 346.
- Next engineering seam: define authoritative source/selected/returned-byte and truncation evidence at core, then build a separate convergence candidate before any PROMOTION decision.
