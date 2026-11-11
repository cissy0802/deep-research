import duckdb,sys,random
D=sys.argv[1]+'/data/'
c=duckdb.connect()
def q(t,s): print('##',t); print(c.sql(s.replace('@',D)).df().to_string()); print()
q('age strata single-commit (cutoff 2026-07-11)',"""
select spec_tool, case when d<30 then 'a<30d' when d<90 then 'b30-90d' when d<180 then 'c90-180d' else 'd>=180d' end age, count(*) n, round(avg(case when file_total_commits=1 then 1 else 0 end),3) single
from (select spec_tool,file_total_commits, date_diff('day', try_cast(substr(file_first_commit_at,1,10) as date), date '2026-07-11') d from '@spec_files.parquet') where spec_tool in ('speckit','openspec','specs_generic') group by 1,2 order by 1,2""")
q('first commit range',"select spec_tool, min(file_first_commit_at), median(try_cast(substr(file_first_commit_at,1,10) as date)), max(file_first_commit_at) from '@spec_files.parquet' where spec_tool in ('speckit','openspec') group by 1")
q('repo concentration speckit/openspec specs',"with r as (select spec_tool,repo_name,count(*) n, avg(case when file_total_commits=1 then 1 else 0 end) s from '@spec_files.parquet' where spec_tool in ('speckit','openspec') group by 1,2) select spec_tool, count(*) repos, median(s) med_repo_single, max(n) maxn, sum(n) tot from r group by 1")
q('openspec roles',"select spec_tool, spec_role, count(*) n, round(avg(case when file_total_commits=1 then 1 else 0 end),3) s from '@spec_files.parquet' where spec_tool in ('speckit','openspec') group by 1,2 order by 1,3 desc")
q('consistency file_total_commits vs spec_file_commits rows',"""with k as (select file_url_sha16, count(*) n from '@spec_file_commits.parquet' group by 1) select count(*) files, avg(case when s.file_total_commits=k.n then 1 else 0 end) eq, avg(case when k.n is null then 1 else 0 end) missing from '@spec_files.parquet' s left join k using(file_url_sha16)""")
# cluster bootstrap for PR cochange
import pandas as pd
p=c.sql(f"select repo_name,pr_number,max(touches_code) tc from '{D}pull_requests.parquet' group by 1,2").df()
g=p.groupby('repo_name').tc.agg(['sum','count']).reset_index()
random.seed(2); arr=list(zip(g['sum'],g['count'])); bs=[]
for _ in range(4000):
    s=random.choices(arr,k=len(arr)); bs.append(sum(a for a,b in s)/sum(b for a,b in s))
bs.sort(); print('cluster bootstrap PR cochange 95%',round(bs[100],3),round(bs[3900],3))
