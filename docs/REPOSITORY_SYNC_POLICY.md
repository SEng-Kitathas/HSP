# Repository Sync Policy

Status: active working policy

1. `origin` is `https://github.com/SEng-Kitathas/HSP.git`.
2. Fetch/reconcile before every HSP Git mutation. Never overwrite remote divergence silently.
3. Commit current working authority, experiment registrations/results, visible supersessions, and continuity-relevant scars.
4. Do not silently promote experimental material into mainline/canon.
5. Do not publish private SOP packages or unrelated donor projects merely because they influenced process.
6. Preserve stale/failed experiment artifacts when they are evidence; supersede rather than rewrite.
7. After push, read back the remote branch SHA and compare it to local `HEAD`.
8. A successful local commit is not a successful GitHub sync until remote readback matches.
