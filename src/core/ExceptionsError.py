class AppError(Exception):
    pass

class NotFoundError(AppError):
    pass

class DatabaseError(AppError):
    pass

class DuplicateScheduleError(AppError):
    pass

class InvalidInputError(AppError):
    pass

class UnauthorizedError(AppError):
    pass

class InvalidTimeError(AppError):
    pass