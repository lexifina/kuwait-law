# How this repository was made (Kuwait)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Ministry of Justice of Kuwait, laws page | <https://www.moj.gov.kw/AR/Pages/MojLaws.aspx> | 2026-10-29 | No licence stated; official legislation, credited to the Ministry of Justice. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `law-63-2015` | قانون رقم 63 لسنة 2015 في شأن مكافحة جرائم تقنية المعلومات | 1 | 2015-07-07 to 2015-07-07 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 0 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Asia/Kuwait) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Kuwaiti laws take effect on publication in Kuwait Al-Youm unless the law says otherwise (Law 63/2015 art. 21 delays it six months). This first build dates its one version from the Amir's date of issue. https://www.moj.gov.kw/AR/Pages/MojLaws.aspx

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `9be1f1ca435a235e8277f0aad1f96f71074bba66550c1296e6409fa616a9694e` (28458 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6229396f41c9d7f1d6f405becfbe4097b35b82da`, `check.py` `5e112e6a33b7e93d00112e55f01fbb4fb3fdd8da`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Punctuation spacing was normalised (one space after the Arabic comma and colon, none before) and two words whose shadda was detached in the PDF text layer were repaired.
- Punctuation spacing was normalised (one space after the Arabic comma and colon, none before) and two words whose shadda was detached in the PDF text layer were repaired (القُصّر, يخصّه).
- Only Law 63 of 2015 as issued is recorded, no amendments; the explanatory memorandum and the preamble recitals are left out.
- The version is dated 7 July 2015, the date of issue (20 Ramadan 1436), because the source gives no publication date; it is the oldest version available, credited to the publisher.
- The PDF text layer has digit runs in visual order; lists of numbers in parentheses were reversed ("( ) 79 ، 46" read as "(46، 79)"), item numbers "- 1" read as "1-", checked against a rendering of the page, and kashida (tatweel) removed.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
