from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.models.chat_message import ChatMessage
from app.schemas.chat import ChatRequest, ChatResponse, ChatHistoryOut
from app.auth.dependencies import get_current_user
from app.chatbot.engine import get_answer

router = APIRouter(prefix="/api", tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    answer = get_answer(payload.message)

    record = ChatMessage(
        user_id=current_user.id,
        question=payload.message,
        answer=answer,
    )
    db.add(record)
    db.commit()

    return ChatResponse(answer=answer)


@router.get("/chat-history", response_model=List[ChatHistoryOut])
def get_chat_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(ChatMessage)
        .filter(ChatMessage.user_id == current_user.id)
        .order_by(ChatMessage.created_at.desc())
        .all()
    )


@router.delete("/chat-history/{item_id}")
def delete_chat_history_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    record = (
        db.query(ChatMessage)
        .filter(ChatMessage.id == item_id, ChatMessage.user_id == current_user.id)
        .first()
    )
    if not record:
        raise HTTPException(status_code=404, detail="Chat history item not found")

    db.delete(record)
    db.commit()
    return {"message": "Deleted successfully"}
