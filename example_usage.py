from client import Lev8ProspectResearcherClient
client = Lev8ProspectResearcherClient()
result = client.research_and_rank(
    ideal_customer_profile={"industry": "saas", "company_size": "mid-market", "title_keywords": ["CTO", "VP Engineering"]},
    candidates=[
        {"name": "Alice Zhao", "title": "VP Engineering", "company": "CloudFlow", "industry": "SaaS", "company_size": "mid-market", "recently_funded": True, "hiring_ai_roles": True},
        {"name": "Bob Kim", "title": "Marketing Manager", "company": "RetailHub", "industry": "Retail", "company_size": "enterprise", "recently_funded": False, "hiring_ai_roles": False},
        {"name": "Carol Diaz", "title": "CTO", "company": "DataOps Inc", "industry": "SaaS", "company_size": "smb", "recently_funded": False, "hiring_ai_roles": True},
    ]
)
print(f"Top prospect: {result['top_prospect']['name']} (score: {result['top_prospect']['fit_score']})")
for p in result["ranked_prospects"]:
    print(f"  {p['name']} | Score: {p['fit_score']} | Priority: {p['outreach_priority']}")
