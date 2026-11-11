import duckdb,sys
D=sys.argv[1]+'/data/'
c=duckdb.connect()
def q(t,s): print('##',t); print(c.sql(s.replace('@',D)).df().to_string()); print()
q('rows/distinct',"select count(*), count(distinct repo_name||'#'||pr_number) from '@pull_requests.parquet'")
q('dedup cochange',"with p as (select repo_name,pr_number,max(touches_code) tc, max(is_merged) m, any_value(author_login) a, any_value(n_prs_in_repo) npr from '@pull_requests.parquet' group by 1,2) select count(*) n, avg(tc) share, avg(m) merged, avg(case when m=1 then tc end) share_merged from p")
q('cluster: per-repo',"with p as (select repo_name,pr_number,max(touches_code) tc from '@pull_requests.parquet' group by 1,2), r as (select repo_name,count(*) n,avg(tc) s from p group by 1) select count(*) repos, median(s) med_repo_share, avg(s) mean_repo_share, quantile_cont(s,0.25) q25, quantile_cont(s,0.75) q75, max(n) maxn, median(n) medn from r")
q('top repos concentration',"with p as (select repo_name,pr_number,max(touches_code) tc from '@pull_requests.parquet' group by 1,2), r as (select repo_name,count(*) n,avg(tc) s from p group by 1 order by n desc) select repo_name,n,round(s,3) s, round(sum(n) over (order by n desc rows unbounded preceding)/5322.0,3) cum from r limit 12")
q('bot/agent authors',"with p as (select distinct repo_name,pr_number,author_login,touches_code from '@pull_requests.parquet') select (author_login ilike '%bot%' or author_login ilike '%copilot%' or author_login ilike '%claude%' or author_login ilike '%codex%' or author_login ilike '%devin%' or author_login ilike '%cursor%') botlike, count(*), avg(touches_code) from p group by 1")
q('code ext outside specdir',"select ext, count(*) n from '@pr_files.parquet' where is_code=1 and is_specdir=0 group by 1 order by 2 desc limit 25")
q('is_code for md?',"select ext,is_code,count(*) from '@pr_files.parquet' where ext in ('md','json','yaml','yml','toml','txt','lock') group by 1,2 order by 1")
# spec file change status in PRs
q('spec files change_status',"select tool, change_status, count(*) n from '@pr_files.parquet' where is_spec=1 group by 1,2 order by 1,3 desc")
q('PR-level: adds new spec only vs modifies existing spec',"""
with f as (select tool,repo_name,pr_number, max(case when is_spec=1 and change_status='added' then 1 else 0 end) addspec, max(case when is_spec=1 and change_status='modified' then 1 else 0 end) modspec, max(case when is_spec=1 and change_status='removed' then 1 else 0 end) rmspec from '@pr_files.parquet' group by 1,2,3),
p as (select tool,repo_name,pr_number,max(touches_code) tc from '@pull_requests.parquet' group by 1,2,3)
select case when addspec=1 and modspec=0 then 'add-only' when modspec=1 and addspec=0 then 'modify-only' when addspec=1 and modspec=1 then 'both' when rmspec=1 then 'remove-only' else 'none' end k, count(*) n, avg(tc) cochange from p join f using(tool,repo_name,pr_number) group by 1 order by 2 desc""")
q('modify-only & touches code, by tool',"""
with f as (select tool,repo_name,pr_number, max(case when is_spec=1 and change_status='added' then 1 else 0 end) addspec, max(case when is_spec=1 and change_status='modified' then 1 else 0 end) modspec from '@pr_files.parquet' group by 1,2,3),
p as (select tool,repo_name,pr_number,max(touches_code) tc from '@pull_requests.parquet' group by 1,2,3)
select tool, count(*) n, sum(case when modspec=1 and addspec=0 then 1 else 0 end) modonly, sum(case when modspec=1 and addspec=0 and tc=1 then 1 else 0 end) modonly_code from p join f using(tool,repo_name,pr_number) group by 1 order by 2 desc""")
q('which spec files modified (path pattern)',"select regexp_extract(file_path,'([^/]+)$',1) base, count(*) n from '@pr_files.parquet' where is_spec=1 and change_status='modified' group by 1 order by 2 desc limit 12")
q('which spec files added',"select regexp_extract(file_path,'([^/]+)$',1) base, count(*) n from '@pr_files.parquet' where is_spec=1 and change_status='added' group by 1 order by 2 desc limit 12")
