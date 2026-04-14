class ApiErrorHandler(Exception):
    def __init__(self,status_code:int,message:str,error_code:str):
        super().__init__(message)
        self.status_code=status_code
        self.error_code=error_code

    @classmethod
    def bad_request(cls,message="Bad request"):
        return cls(400,message,"BAD REQUEST")
    
    @classmethod
    def unauthourized(cls,message="Unauthorized"):
        return cls(401,message,"UNAUTHORIZED")

    @classmethod
    def forbidden(cls,message="Forbidden"):
        return cls(403,message,"FORBIDDEN")

    @classmethod
    def internal_server_error(cls,message="Internal Server Error"):
        return cls(500,message,"INTERNAL SERVER ERROR")
