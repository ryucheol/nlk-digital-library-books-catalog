import json,collections,os,shutil,sys
# usage: python3 build_site.py <work dir with final_rows.json, units.json, wiki_links.json> <output docs dir>
W=sys.argv[1] if len(sys.argv)>1 else "."
rows=json.load(open(os.path.join(W,"final_rows.json")))
wiki={}  # ID -> [ko, en, zh, ja] Wikipedia titles ('' when missing)
LANGS=['ko','en','zh','ja']
if os.path.exists(os.path.join(W,"wiki_all.json")):
    links=json.load(open(os.path.join(W,"wiki_all.json")))
    for u in json.load(open(os.path.join(W,"units.json"))):
        m=links.get(u["key"])
        if m:
            for i in u["ids"]: wiki[i]=[m.get(L,'') for L in LANGS]
ERA=['고려 이전 (~1391)','조선 전기 (1392–1592)','조선 중기 (1593–1723)','조선 후기 (1724–1875)','개항기·대한제국 (1876–1910)','일제강점기 (1910–1945)','해방 이후 (1945~)','연대 미상']
CATS=['경서·유학','역사·전기','지리·지도·기행','정치·행정·법률','경제·산업·통계','사회·풍속·예법','불교','기독교','기타종교·민간신앙','철학·사상','문학(시문·문집)','소설·희곡','어학·문자·사전','교육·교재·아동','자연과학·수학','의학·약학','공학·기술·농업','예술·음악·건축','족보·가승','군사','총서·유서·잡지·목록','고문서·기록물','기타','고문서·기록물(간찰 등)']
out=sys.argv[2] if len(sys.argv)>2 else "docs"; shutil.rmtree(out+"/data",ignore_errors=True); os.makedirs(out+"/data")
g=collections.defaultdict(list)
for r in rows:
    c=CATS.index(r['분류']) if r['분류'] in CATS else CATS.index('기타')
    g[(c,ERA.index(r['시대']))].append(r)
counts={}
for (c,e),L in g.items():
    L.sort(key=lambda r:(r['연도'] if r['연도']!='' else 9999,r['원제목']))
    data=[[r['ID'],r['한국어제목'],r['원제목'],r['저자'],r['발행연도_원문'],r['연도'],1 if r['시대추정'] else 0,r['한줄요약'],r['발행처'],wiki.get(r['ID'],0)] for r in L]
    json.dump(data,open(f"{out}/data/{c}_{e}.json","w"),ensure_ascii=False,separators=(',',':'))
    counts[f"{c}_{e}"]=len(L)
json.dump({"cats":CATS,"eras":ERA,"counts":counts,"total":len(rows),"wiki":len(wiki),"wikiLang":{L:sum(1 for v in wiki.values() if v[j]) for j,L in enumerate(LANGS)}},open(f"{out}/data/meta.json","w"),ensure_ascii=False)
sizes=sorted(os.path.getsize(f"{out}/data/{f}") for f in os.listdir(out+"/data"))
print(len(counts),"files; max KB",sizes[-1]//1024,"total MB",sum(sizes)/1e6)
