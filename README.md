# Kuwait: law history in git

The law of Kuwait as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `law-63-2015/` | قانون رقم 63 لسنة 2015 في شأن مكافحة جرائم تقنية المعلومات (Law No. 63 of 2015 on combating information technology crimes) | 1 | As issued by the Amir on 7 July 2015 (21 articles); no amendments recorded |

**Language.** The text is in Arabic, the official language of Kuwait's laws. No English text is published by the ministry.

**Source.** The Ministry of Justice of Kuwait's laws page, https://www.moj.gov.kw/AR/Pages/MojLaws.aspx (PDF of the law, text layer), retrieved 29 October 2026. The ministry's own PDF of the Constitution has an unreadable text layer (scan or legacy font encoding), so it is not included.

## Dates

Each commit is dated at noon, Asia/Kuwait. The one version is dated 7 July 2015 (20 Ramadan 1436), the date the Amir issued the law. By article 21 it applies six months after its publication in the Official Gazette; this record does not have the publication date, so 7 July 2015 is the date of the oldest version available, not the commencement date.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@moj.invalid`). The version is the oldest version available, credited to the publisher (the Ministry of Justice). The committer is always Lexifina.

## Limits

A first build with a single law. The Constitution of Kuwait and the rest of Kuwaiti law are not included. Amendments, if any, are not recorded. In the source PDF numbers inside the text are stored in visual order; they were restored and checked against a rendering of the page.
