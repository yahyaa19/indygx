from typing import Any
from sqlmodel import Session, select
from ..database import get_session
from ..models import CompanySecondary

class CompanySecondaryRepository:

    @staticmethod
    def get(company_id: int):
        with get_session() as session:
            return session.get(CompanySecondary, company_id)

    # @staticmethod
    # def upsert(company_id: int, data: dict):
    #     with get_session() as session:
    #         obj = session.get(CompanySecondary, company_id)

    #         if not obj:
    #             obj = CompanySecondary(company_id=company_id, **data)
    #             session.add(obj)
    #         else:
    #             for key, value in data.items():
    #                 setattr(obj, key, value)

    #         session.commit()
    #         session.refresh(obj)
    #         return obj

    @staticmethod
    def upsert(
        company_id: int,
        data: dict[str, Any],
        session: Session
    ) -> CompanySecondary:
        """
        Insert or update company_primary row.

        - company_id comes from path / service layer
        - data contains ONLY fields to be updated (exclude_unset already applied)
        - session lifecycle handled by service layer
        """

        # Always enforce company_id from path
        data["company_id"] = company_id

        stmt = select(CompanySecondary).where(
            CompanySecondary.company_id == company_id
        )
        existing = session.exec(stmt).one_or_none()

        if existing:
            # UPDATE path
            for field, value in data.items():
                setattr(existing, field, value)

            session.add(existing)
            return existing

        # INSERT path
        new_company = CompanySecondary(**data)
        session.add(new_company)
        return new_company

    @staticmethod
    def delete(company_id: int):
        with get_session() as session:
            obj = session.get(CompanySecondary, company_id)
            if not obj:
                return False
            session.delete(obj)
            session.commit()
            return True

