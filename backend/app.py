from sqlmodel import select, Session
from .database import engine
# from .models import CompanyPrimary
from backend.repository.company_repository import CompanyRepository

# def fetch_all_companies():
#     with Session(engine) as session:
#         try:
#             statement = select(CompanyPrimary.company_id, CompanyPrimary.company_name)
#             results = session.exec(statement).all()
#             return results
#         except Exception as e:
#             print(f"An error occurred while fetching companies: {e}")
#             return []
#         finally:
#             print("Database session closed.")

# if __name__ == "__main__":
#     companies = fetch_all_companies()

#     for company_id, company_name in companies:
#         print(f"{company_id} | {company_name}")




if __name__ == "__main__":
    companies = CompanyRepository.list_companies()
    print("Companies:")
    for c in companies:
        print(c)

    print("\nFull company profile:")
    company = CompanyRepository.get_company_full_profile(company_id=1)
    print(company)
