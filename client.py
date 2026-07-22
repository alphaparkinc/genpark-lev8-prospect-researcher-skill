class Lev8ProspectResearcherClient:
    def research_and_rank(self, ideal_customer_profile: dict, candidates: list) -> dict:
        icp_industry = ideal_customer_profile.get("industry", "").lower()
        icp_size = ideal_customer_profile.get("company_size", "mid-market")
        icp_title = ideal_customer_profile.get("title_keywords", [])

        ranked = []
        for c in candidates:
            score = 0
            # Industry match
            if icp_industry and icp_industry in c.get("industry", "").lower():
                score += 35
            # Company size match
            if c.get("company_size", "") == icp_size:
                score += 25
            # Title keyword match
            title = c.get("title", "").lower()
            for kw in icp_title:
                if kw.lower() in title:
                    score += 20
                    break
            # Engagement signals
            if c.get("recently_funded"): score += 10
            if c.get("hiring_ai_roles"):  score += 10

            ranked.append({**c, "fit_score": score, "outreach_priority": "HIGH" if score >= 60 else "MEDIUM" if score >= 40 else "LOW"})

        ranked.sort(key=lambda x: x["fit_score"], reverse=True)
        return {"ranked_prospects": ranked, "top_prospect": ranked[0] if ranked else {}}
