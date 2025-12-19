from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from bson import ObjectId
from enum import Enum

from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema, core_schema
from typing import Any, Annotated

class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not value:
            return None

        if isinstance(value, ObjectId):
            return str(value)

        if isinstance(value, str):
            try:
                if ObjectId.is_valid(value):
                    return str(ObjectId(value))
            except Exception:
                raise ValueError("Invalid ObjectId format")

        raise ValueError("Invalid ObjectId format")

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        _source_type: Any,
        _handler: Any
    ) -> CoreSchema:
        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.str_schema()
            ]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda x: str(x) if isinstance(x, ObjectId) else x,
                return_schema=core_schema.str_schema(),
            ),
        )

# User Models
class UserBase(BaseModel):
    email: EmailStr
    name: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    study_interests: List[str] = []
    learning_streaks: int = 0
    student_id: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    bio: Optional[str] = None
    avatar: Optional[str] = None
    study_interests: Optional[List[str]] = None
    learning_streaks: Optional[int] = None

class UserInDB(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    hashed_password: str
    is_verified: bool = False
    friends: List[PyObjectId] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda v: v.isoformat(),
        }
        populate_by_name = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class User(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    is_verified: bool = False
    friends: List[PyObjectId] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Authentication Models
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None

class EmailVerification(BaseModel):
    email: EmailStr
    code: str
    expires_at: datetime

# Friend System Models
class FriendRequestStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    DECLINED = "declined"

class FriendRequest(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    sender_id: PyObjectId
    receiver_id: PyObjectId
    status: FriendRequestStatus = FriendRequestStatus.PENDING
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Classroom Models
class ClassroomBase(BaseModel):
    name: str
    description: Optional[str] = None
    logo: Optional[str] = None

class ClassroomCreate(ClassroomBase):
    pass

class ClassroomUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None

class ClassroomInDB(ClassroomBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    admin_id: PyObjectId
    members: List[PyObjectId] = []
    invite_code: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Classroom(ClassroomBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    admin_id: PyObjectId
    members: List[PyObjectId] = []
    invite_code: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Room Models
class RoomBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoomCreate(RoomBase):
    classroom_id: PyObjectId

class RoomUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class RoomInDB(RoomBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    classroom_id: PyObjectId
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Room(RoomBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    classroom_id: PyObjectId
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# YouTube Summarizer Models
class YouTubeChatMessage(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class YouTubeSessionBase(BaseModel):
    video_url: str
    video_title: Optional[str] = None
    video_duration: Optional[int] = None  # in seconds
    transcript: Optional[str] = None
    short_summary: Optional[str] = None
    detailed_summary: Optional[str] = None
    chat_history: List[YouTubeChatMessage] = []

class YouTubeSessionCreate(YouTubeSessionBase):
    pass

class YouTubeSessionUpdate(BaseModel):
    video_title: Optional[str] = None
    transcript: Optional[str] = None
    short_summary: Optional[str] = None
    detailed_summary: Optional[str] = None
    chat_history: Optional[List[YouTubeChatMessage]] = None

class YouTubeSessionInDB(YouTubeSessionBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class YouTubeSession(YouTubeSessionBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: PyObjectId
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# Message Models
class MessageBase(BaseModel):
    content: str
    room_id: PyObjectId

class MessageCreate(MessageBase):
    pass

class MessageUpdate(BaseModel):
    content: Optional[str] = None

class MessageInDB(MessageBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    sender_id: PyObjectId
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    edited: bool = False
    deleted: bool = False
    edited_at: Optional[datetime] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Message(MessageBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    sender_id: PyObjectId
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    edited: bool = False
    deleted: bool = False
    edited_at: Optional[datetime] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

# WebSocket Models
class WebSocketMessage(BaseModel):
    type: str
    data: Dict[str, Any]

class ChatMessage(BaseModel):
    room_id: str
    content: str
    sender_id: str

# Direct messaging models
class MessageType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    AI_RESPONSE = "ai_response"

class DirectMessage(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    conversation_id: str
    sender_id: str
    receiver_id: str
    content: str
    message_type: MessageType = MessageType.TEXT
    file_url: Optional[str] = None
    file_name: Optional[str] = None
    file_size: Optional[int] = None
    is_ai_response: bool = False
    replied_to: Optional[str] = None  # ID of message being replied to
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    is_read: bool = False
    is_edited: bool = False
    edited_at: Optional[datetime] = None

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

class Conversation(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    participants: List[str]  # User IDs
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    last_message_id: Optional[str] = None
    last_message_content: Optional[str] = None
    last_message_timestamp: Optional[datetime] = None

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
