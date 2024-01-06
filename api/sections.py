from typing import Optional, List, Union
from fastapi import FastAPI, HTTPException, Path, Query, APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/sections/{id}")
async def read_sections():
  return {"courses": []}
  
@router.post("/sections/{id}/content-blocks")
async def read_section_content_blocks():
  return {"courses": []}

@router.get("/content-blocks/{id}")
async def read_content_blocks():
  return {"courses": []}
    
