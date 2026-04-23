from typing import TypedDict, Any


class UniversalState(TypedDict):
    main_prompt: str
    intent: str  # "coding", "video_gen", "research"
    data: dict[str, Any]
    status: str
    error_log: list[str]
