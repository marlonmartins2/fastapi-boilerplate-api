from http import HTTPStatus

import sentry_sdk
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

from app.routers import admin, user
from app.settings import settings
from app.utils.logger import logger
from app.version import __version__

sentry_sdk.init(
    settings.SENTRY_URL,
    environment=settings.SENTRY_ENVIRONMENT,
    send_default_pii=True,
    release=__version__,
    integrations=[StarletteIntegration(), FastApiIntegration()],
)

logger.info('App "%s" - v%s (%s)', settings.APP_NAME, __version__, settings.APP_ENV)

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=__version__,
    contact={
        "name": "Marlon Martins",
        "url": "https://github.com/marlonmartins2",
        "email": "marlon.azevedo.m@gmail.com",
    },
    license_info={
        "name": "Copyright",
        "url": "https://github.com/marlonmartins2/fastapi-boilerplate-api/blob/master/LICENSE",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(
    "/health_check",
    status_code=HTTPStatus.NO_CONTENT,
    description="Endpoint básico para testar o uptime do serviço.",
    name="Verifica Status do Serviço",
)
async def get_health_check():
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


app.include_router(admin.router)
app.include_router(user.router)


@app.middleware("http")
async def http_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as ex:
        logger.error("%s", str(ex))

        with sentry_sdk.push_scope() as scope:
            scope.set_context("request", request)
            scope.user = {"ip_address": request.client.host}
            sentry_sdk.capture_exception(ex)
        raise
