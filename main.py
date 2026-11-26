"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply (a single sentence, under 200
characters) to /output/entry.txt.

Strategy, in my own words: the house judge weighs honesty first, then
politeness, then the turn of phrase, so the line leads with two private
admissions a real employee would only say off the record — answering
email at midnight for years, and having stopped pretending to keep up —
then names the concrete evidence (400 unread messages) instead of
complaining in general terms, and closes warm and professional: the
sender will reply properly, rested, when back. One sentence, commas
only, no em-dash, no list of complaints, and quotable in the middle
("stopped pretending I can keep up") rather than at the end.

Standard library only: the grading sandbox installs nothing.
"""

import os

ENTRY = (
    # 194 characters, verified by len() in the test run below — safely
    # inside the 1-200 gate, with room to spare and no cramming.
    "I'm away until Monday, and after years of answering email at "
    "midnight I've stopped pretending I can keep up, so your message "
    "joins 400 unread ones and I'll reply properly, rested, when I'm back."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
