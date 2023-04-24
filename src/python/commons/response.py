from typing import List, Optional, Union

from fastapi.responses import JSONResponse as FastAPIResponse


class UJSONResponse(FastAPIResponse):

    def __init__(
            self,
            message: str,
            status_code: int,
            data: Optional[Union[dict, List[dict]]] = None
    ):
        response = dict(
            message=message,
            status_code=status_code,
            data=data,
        )
        super().__init__(response, status_code)
