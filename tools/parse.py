"""Kuwait: Law 63/2015 (information technology crimes) from the Ministry of Justice PDF. Reads .cache only."""
import json, re, hashlib, subprocess
from pathlib import Path
here = Path(__file__).parent
pdf = here/'.cache'/'law-63-2015.pdf'
sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
t = subprocess.run(['pdftotext','-enc','UTF-8','-layout',str(pdf),'-'],capture_output=True,text=True,encoding='utf8').stdout
t = re.sub('[‪-‮‎‏]','',t).replace('ـ','').replace(' ',' ')
i = t.index('الفصل الأول'); j = t.index('المذكرة الايضاحية')
body = t[i:j]
def fix(s):
    s = re.sub(r'\(\s*\)\s*([\d][\d\s،]*)', lambda m: '('+'، '.join(reversed([x for x in re.split(r'[\s،]+', m.group(1).strip()) if x]))+') ', s)
    s = s.strip()
    s = re.sub(r'^- (\d+)', r'\1- ', s)
    s = re.sub(r'(\d)([ء-ي])', r'\1 \2', s)
    s = re.sub(r'لسنة\s*،\s*(\d{4})', r'لسنة \1،', s)
    s = re.sub(r'\s+([،.])', r'\1', s)
    s = re.sub(r'\s*،\s*', '، ', s)
    s = re.sub(r'\s*:\s*', ': ', s)
    s = s.replace('بالُق ّصر', 'بالقُصّر').replace('يخ ّصه', 'يخصّه')
    s = re.sub(r'\s+', ' ', s).strip()
    return s
units = {}; key = None
for raw in body.split(chr(10)):
    s = fix(raw)
    if not s: continue
    m = re.fullmatch(r'المادة\s*\((\d+)\)', s)
    if m:
        n = int(m.group(1)); key = f'art-{n:03d}'; units[key] = {'label': f'المادة {n}', 'lines': []}; continue
    if s in ('الفصل الأول','الفصل الثاني','تعريفات','الجرائم والعقوبات'): continue
    if key is None: continue
    if s.startswith('أمير الكويت'): break
    units[key]['lines'].append(s)
final = {}
for k,u in units.items():
    ps = []
    for ln in u['lines']:
        if ps and not re.search(r'[.:]$', ps[-1]) and not re.match(r'\d+- ', ln): ps[-1] += ' ' + ln
        else: ps.append(ln)
    final[k] = {'label': u['label'], 'kind': 'art', 'text': f"# {u['label']}" + chr(10) + chr(10).join(ps) + chr(10)}
assert len(final)==21, len(final)
corpus = {
 'country': {'code':'KW','name':'Kuwait','slug':'kuwait','lang':'ar','tz':'Asia/Kuwait','future_branch':'future',
  'publisher': {'name':'Ministry of Justice of Kuwait (وزارة العدل)','email':'moj@moj.invalid'},
  'default_in_force_rule': {'text':'Kuwaiti laws take effect on publication in Kuwait Al-Youm unless the law says otherwise (Law 63/2015 art. 21 delays it six months). This first build dates its one version from the Amir\'s date of issue.','source':'https://www.moj.gov.kw/AR/Pages/MojLaws.aspx'},
  'licence_note':'Text published by the Ministry of Justice of Kuwait, https://www.moj.gov.kw.'},
 'sources': [{'name':'Ministry of Justice of Kuwait, laws page','url':'https://www.moj.gov.kw/AR/Pages/MojLaws.aspx','retrieved':'2026-10-29','requests':3,'licence':'No licence stated; official legislation, credited to the Ministry of Justice.','notes':'Text layer of the ministry PDF Law 63 of 2015. The PDF stores digit runs in visual order; the builder restores them.'}],
 'laws': {},
 'acts': [{'slug':'law-63-2015','short':'63/2015','title':'قانون رقم 63 لسنة 2015 في شأن مكافحة جرائم تقنية المعلومات','url':'https://www.moj.gov.kw/AR/Documents/MojDocs/%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%B1%D9%82%D9%85%2063%20%D9%84%D8%B3%D9%86%D8%A9%202015%20%D8%A8%D8%A5%D8%B5%D8%AF%D8%A7%D8%B1%20%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D9%85%D9%83%D8%A7%D9%81%D8%AD%D8%A9%20%D8%AC%D8%B1%D8%A7%D8%A6%D9%85%20%D8%AA%D9%82%D9%86%D9%8A%D8%A9%20%D8%A7%D9%84%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA.pdf',
   'first_law': None, 'earlier_laws': [],
   'versions': [{'from':'2015-07-07','source_url':'https://www.moj.gov.kw/AR/Pages/MojLaws.aspx','sha256':sha,'units':final,
     'note':'Text as published by the Ministry of Justice. Dated 7 July 2015, the Amir\'s date of issue; under article 21 the law applies six months after its publication in the Official Gazette, a date this record does not have.'}]}],
 'applies': [],
 'decisions': ['Punctuation spacing was normalised (one space after the Arabic comma and colon, none before) and two words whose shadda was detached in the PDF text layer were repaired.','Punctuation spacing was normalised (one space after the Arabic comma and colon, none before) and two words whose shadda was detached in the PDF text layer were repaired (القُصّر, يخصّه).','Only Law 63 of 2015 as issued is recorded, no amendments; the explanatory memorandum and the preamble recitals are left out.',
   'The version is dated 7 July 2015, the date of issue (20 Ramadan 1436), because the source gives no publication date; it is the oldest version available, credited to the publisher.',
   'The PDF text layer has digit runs in visual order; lists of numbers in parentheses were reversed ("( ) 79 ، 46" read as "(46، 79)"), item numbers "- 1" read as "1-", checked against a rendering of the page, and kashida (tatweel) removed.'],
 'ai_use': ['none']}
json.dump(corpus, open(here/'corpus.json','w',encoding='utf8'), ensure_ascii=False, indent=1)
print(len(final))
