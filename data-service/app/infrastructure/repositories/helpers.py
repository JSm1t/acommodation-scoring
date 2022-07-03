from uuid import UUID

def is_valid_uuid(value):
    try:
        UUID(str(value))
    except ValueError:
        return False
    
    return True