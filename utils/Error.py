from fastapi import status, HTTPException

class Error:
    def __init__(self, exception: Exception) -> None:
        self.__exception = exception

    def raise_error(self):
        error_dict = self.__exception.__dict__

        if error_dict.get('status_code'):
            raise HTTPException(error_dict['status_code'], error_dict['detail'])
        else:
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, \
                detail=f""" Something wrong in the server, {self.__exception}""")
