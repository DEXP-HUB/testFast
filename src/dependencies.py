from fastapi import Depends


async def param(key: str):
    return key