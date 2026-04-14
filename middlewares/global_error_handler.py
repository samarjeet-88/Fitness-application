from fastapi import Request
from fastapi.responses import JSONResponse
from core.ApiErrorHandler import ApiErrorHandler
from fastapi.exceptions import RequestValidationError

async def api_exception_handler(request: Request, exc: ApiErrorHandler):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "code": exc.error_code
        }
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "code": "VALIDATION_ERROR",
            "errors": exc.errors()
        }
    )