"""This scripts contains base class to moderate each modal contens (text, audio,...)"""

from pydantic import BaseModel, Field, computed_field

class ModerationResult(BaseModel):
    """Base model for content moderation."""

    rationale: str = Field(description="Explanation of what was harmful and why")

    @computed_field
    @property
    def is_flagged(self) -> bool:
        """Determines if any moderation flags are set to True."""
        return False

class TextModerationResult(ModerationResult):
    """Base model for text content moderation."""

    contains_pii: bool = Field(description="Whether the message contains any personally-identifiable information (PII)")
    is_unfriendly: bool = Field(description="Whether unfriendly tone or content was detected")
    is_unprofessional: bool = Field(description="Whether unprofessional tone or content was detected")

    @computed_field
    @property
    def is_flagged(self) -> bool:
        """Determines if any text moderation flags are set to True."""
        return self.contains_pii or self.is_unfriendly or self.is_unprofessional

class ImageModerationResult(ModerationResult):
    """Base model for image content moderation."""

    contains_pii: bool = Field(
        description="Whether the image contains any person, part of a person, or personally-identifiable information (PII)"
    )
    is_disturbing: bool = Field(description="Whether the image is disturbing")
    is_low_quality: bool = Field(description="Whether the image is low quality")

    @computed_field
    @property
    def is_flagged(self) -> bool:
        """Determines if any image moderation flags are set to True."""
        return self.contains_pii or self.is_disturbing or self.is_low_quality

class VideoModerationResult(ModerationResult):
    """Base model for video content moderation."""

    contains_pii: bool = Field(
        description="Whether the video contains any person or personally-identifiable information (PII)"
    )
    is_disturbing: bool = Field(description="Whether the video is disturbing")
    is_low_quality: bool = Field(description="Whether the video is low quality")

    @computed_field
    @property
    def is_flagged(self) -> bool:
        """Determines if any video moderation flags are set to True."""
        return self.contains_pii or self.is_disturbing or self.is_low_quality


class AudioModerationResult(ModerationResult):
    """Base model for audio content moderation."""

    transcription: str = Field(description="Transcription of the audio")
    contains_pii: bool = Field(
        description="Whether the audio contains any personally-identifiable information (PII) such as names, addresses, phone numbers"
    )
    is_unfriendly: bool = Field(
        description="Whether unfriendly tone or content was detected"
    )
    is_unprofessional: bool = Field(
        description="Whether unprofessional tone or content was detected"
    )

    @computed_field
    @property
    def is_flagged(self) -> bool:
        """Determines if any audio moderation flags are set to True."""
        return self.contains_pii or self.is_unfriendly or self.is_unprofessional
