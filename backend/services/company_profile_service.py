from ..database import get_session

from ..repository.company_repository import CompanyRepository
from ..repository.company_secondary_repository import CompanySecondaryRepository
# from ..repository.competitive_intelligence_repository import CompetitiveIntelligenceRepository
# from ..repositorycontact_information_repository import ContactInformationRepository
# from ..repositorydigital_presence_brand_repository import DigitalPresenceBrandRepository
# from ..repositoryfinancials_funding_repository import FinancialsFundingRepository
# from ..repositoryindygx_assessment_repository import IndygxAssessmentRepository
# from ..repositorypartnerships_ecosystem_repository import PartnershipsEcosystemRepository


class CompanyProfileService:

    @staticmethod
    def upsert_full_profile(company_id: int, payload):
        with get_session() as session:
            try:
                CompanyRepository.upsert(
                    company_id,
                    payload.primary.model_dump(exclude_unset=True),
                    session
                )

                if payload.secondary:
                    CompanySecondaryRepository.upsert(
                        company_id,
                        payload.secondary.model_dump(exclude_unset=True),
                        session
                    )

                # if payload.competitive_intelligence:
                #     CompetitiveIntelligenceRepository.upsert(
                #         company_id,
                #         payload.competitive_intelligence.model_dump(exclude_unset=True),
                #         session
                #     )

                # if payload.contact_information:
                #     ContactInformationRepository.upsert(
                #         company_id,
                #         payload.contact_information.model_dump(exclude_unset=True),
                #         session
                #     )

                # if payload.digital_presence_brand:
                #     DigitalPresenceBrandRepository.upsert(
                #         company_id,
                #         payload.digital_presence_brand.model_dump(exclude_unset=True),
                #         session
                #     )

                # if payload.financials_funding:
                #     FinancialsFundingRepository.upsert(
                #         company_id,
                #         payload.financials_funding.model_dump(exclude_unset=True),
                #         session
                #     )

                # if payload.indygx_assessment:
                #     IndygxAssessmentRepository.upsert(
                #         company_id,
                #         payload.indygx_assessment.model_dump(exclude_unset=True),
                #         session
                #     )

                # if payload.partnerships_ecosystem:
                #     PartnershipsEcosystemRepository.upsert(
                #         company_id,
                #         payload.partnerships_ecosystem.model_dump(exclude_unset=True),
                #         session
                #    )

                session.commit()

            except Exception:
                session.rollback()
                raise
