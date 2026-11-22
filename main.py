"""Entry for make.fun bounty the-plan-make-fun-will-carry-20261122-2138.

Writes the plan (one text, exactly 280 characters) to /output/entry.txt.
The output path defaults to /output/entry.txt but can be overridden with
the ENTRY_OUTPUT environment variable.
Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "Day 1: list 300 Shopify stores running Meta ads with slow mobile "
    "pages (Ad Library + PageSpeed). Email each a free teardown naming "
    "the leak. Sell a $49 audit, PDF in 24h. If 3% buy, 9 sales = $441; "
    "offer a $199 fix, 2 take it = +$398. Spend $40 on tools; repeat "
    "with fresh stores."
)


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
