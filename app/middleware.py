from __future__ import annotations

import time
import uuid
import hashlib

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.contextvars import bind_contextvars, clear_contextvars


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        clear_contextvars()

        # Use format: req-<8-char-hex>
        correlation_id = request.headers.get(
            "x-request-id",
            f"req-{uuid.uuid4().hex[:8]}"
        )

        user_id = request.headers.get("x-user-id", "anonymous")
        if user_id != "anonymous":
            user_id_hash = hashlib.sha256(user_id.encode()).hexdigest()
        else:
            user_id_hash = "anonymous"
        
        bind_contextvars(
            correlation_id=correlation_id,
            user_id_hash=user_id_hash
        )

        request.state.correlation_id = correlation_id

        start = time.perf_counter()
        response = await call_next(request)

        processing_time_ms = round(
            (time.perf_counter() - start) * 1000,
            2,
        )

        response.headers["x-request-id"] = correlation_id
        response.headers["x-response-time-ms"] = str(processing_time_ms)
        
        return response
