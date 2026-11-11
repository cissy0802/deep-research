import duckdb,sys
D=sys.argv[1]+'/data/'
c=duckdb.connect()
def q(s): print(s.strip()[:90].replace('\n',' ')); print(c.sql(s.replace('@',D)).df().to_string()); print()
q("SELECT spec_tool, COUNT(*) n_specs, COUNT(DISTINCT repo_name) n_repos, ROUND(AVG(file_total_commits),2) mean_commits, ROUND(AVG(CASE WHEN file_total_commits=1 THEN 1 ELSE 0 END),3) share_single_commit FROM '@spec_files.parquet' GROUP BY 1 ORDER BY 2 DESC")
q("SELECT spec_role, COUNT(*) n, ROUND(AVG(CASE WHEN file_total_commits=1 THEN 1 ELSE 0 END),3) single FROM '@spec_files.parquet' GROUP BY 1 ORDER BY 2 DESC")
q("SELECT tool, COUNT(DISTINCT repo_name||'#'||pr_number) prs, SUM(touches_code) cochange, ROUND(AVG(touches_code),3) share_cochange FROM '@pull_requests.parquet' GROUP BY 1 ORDER BY 2 DESC")
q("SELECT COUNT(DISTINCT repo_name||'#'||pr_number) prs, ROUND(AVG(touches_code),3) share FROM '@pull_requests.parquet'")
q("SELECT artifact_type, COUNT(*) n, ROUND(AVG(CASE WHEN total_commits=1 THEN 1 ELSE 0 END),3) single FROM '@kiro_files.parquet' GROUP BY 1") 
