import duckdb,sys
D=sys.argv[1]+'/data/'
c=duckdb.connect()
def q(t,s): print('##',t); print(c.sql(s.replace('@',D)).df().to_string()); print()
q('single-commit files: first commit looks like squash-merge "(#N)" or merge',"""
select spec_tool, spec_role, count(*) n,
 round(avg(case when regexp_matches(split_part(file_first_commit_message,chr(10),1),'\\(#[0-9]+\\)\\s*$') then 1 else 0 end),3) squash_like,
 round(avg(case when file_first_commit_parents like '%,%' then 1 else 0 end),3) mergecommit,
 round(avg(case when lower(file_first_commit_message) like '%archive%' then 1 else 0 end),3) archive_msg
from '@spec_files.parquet' where file_total_commits=1 and spec_tool in ('speckit','openspec') group by 1,2 order by 1,3 desc""")
q('multi-commit files same',"""
select spec_tool, count(*) n,
 round(avg(case when regexp_matches(split_part(file_first_commit_message,chr(10),1),'\\(#[0-9]+\\)\\s*$') then 1 else 0 end),3) squash_like
from '@spec_files.parquet' where file_total_commits>1 and spec_tool in ('speckit','openspec') group by 1""")
q('parents sample',"select file_first_commit_parents from '@spec_files.parquet' limit 3")
