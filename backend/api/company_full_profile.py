from fastapi import APIRouter, HTTPException
from ..repository.company_repository import CompanyRepository
from ..schemas.company_full_profile import CompanyFullProfile, CompanyListItem, CompanyFullProfileUpsert
from ..schemas.common import PaginatedResponse, PaginationMeta, BulkUpsertRequest
from ..schemas.company_filters import CompanyPrimaryFilter
from ..schemas.company_primary import CompanyPrimaryRead
from fastapi import Depends, status
from ..services.company_profile_service import CompanyProfileService

router = APIRouter()

# @router.get("/", response_model=list[CompanyListItem])
# def list_companies():
#     """
#     List all companies (id + name).
#     """
#     return CompanyRepository.list_companies()

@router.get("/", response_model=PaginatedResponse[CompanyListItem])
def list_companies(
    filters: CompanyPrimaryFilter = Depends(),
    page: int = 1,
    page_size: int = 20,
):
    data, total = CompanyRepository.list_companies(
        filters, page, page_size
    )

    return PaginatedResponse(
        data=data,
        meta=PaginationMeta(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=(total + page_size - 1) // page_size,
        ),
    )

@router.get("/{company_id}")
def get_company(company_id: int):
    """
    Get basic company info by ID.
    """
    company = CompanyRepository.get_company_by_id(company_id)

    if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    return company



@router.get("/{company_id}/full-profile", response_model=CompanyFullProfile)
def get_full_profile(company_id: int):
    company = CompanyRepository.get_company_full_profile(company_id)
    if not company:
        raise HTTPException(status_code=404)
    return company


@router.post("/bulk-upsert")
def bulk_upsert(payload: BulkUpsertRequest):
    CompanyRepository.bulk_upsert(payload.items)
    return {"status": "success"}


@router.put("",status_code=status.HTTP_204_NO_CONTENT)
def upsert_company_full_profile(
    company_id: int,
    payload: CompanyFullProfileUpsert
):
    CompanyProfileService.upsert_full_profile(company_id, payload)