from fastapi import Depends, HTTPException, status, Header

# In a real app, use a robust auth mechanism (JWT/OAuth2). Here, a demo header approach.
async def get_current_user(authorization: str = Header(...)) -> int:
    # Here, any fixed token in the format 'Bearer user1' returns user_id 1
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Authorization header.")
    token = authorization[7:]
    # Simulate one user for assessment
    if token == "user1":
        return 1
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token.")
