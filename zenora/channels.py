import typing
import datetime


class GuildTextChannel:

    """A server text channel object

    :return: Zenora Guild Text Channel object
    :rtype: zenora.channels.GuildTextChannel
    """

    __slots__ = ["data"]

    def __init__(self, data) -> None:
        self.data = data

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return self.data["id"]

    @property
    def name(self) -> typing.Optional[str]:
        """Returns the name of the channel."""
        return self.data["name"]

    @property
    def position(self) -> typing.Optional[int]:
        """Returns the position of the channel."""
        return self.data["position"]

    @property
    def guild_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the channel's guild."""
        return self.data["guild_id"]

    @property
    def topic(self) -> typing.Optional[str]:
        """Returns the topic of the channel."""
        return self.data["topic"]

    @property
    def is_nsfw(self) -> typing.Optional[bool]:
        """Returns if the channel is NSFW or not."""
        return self.data["nsfw"]

    @property
    def last_message_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the last message of the channel."""
        return self.data["last_message_id"]

    @property
    def rate_limit_per_user(self) -> datetime.timedelta:
        """Returns the rate limit per user of the channel."""
        return self.data["rate_limit_per_user"]

    @property
    def permission_overwrites(self) -> datetime.timedelta:
        """Returns the permission overwrites of the channel."""
        return self.data["permission_overwrites"]

    @property
    def category_id(self) -> datetime.timedelta:
        """Returns the snowflake ID of the parant category of the channel."""
        return self.data["parent_id"]

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("position", self.position),
            ("is_nsfw", self.is_nsfw),
            ("permission_overwrites", self.permission_overwrites),
            ("category_id", self.category_id),
            ("guild_id", self.guild_id),
            ("topic", self.topic),
            ("last_message_id", self.last_message_id),
            ("rate_limit_per_user", self.rate_limit_per_user),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r" % i for i in attrs),
        )


class DMTextChannel:
    """A DM/Private message text channel object


    :return: Zenora DM text channel object
    :rtype: zenora.channel.DMTextChannel
    """

    __slots__ = ["data"]

    def __init__(self, data) -> None:
        self.data = data

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return self.data["id"]

    @property
    def last_message_id(self) -> typing.Optional[int]:
        """Returns The last message ID of the channel."""
        return self.data["last_message_id"]

    @property
    def recipients(self) -> typing.Optional[dict]:
        """Returns The recipients of the channel."""
        return self.data["recipients"]

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("last_message_id", self.last_message_id),
            ("recipients", self.recipients),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r" % i for i in attrs),
        )


class GuildVoiceChannel:
    """A guild voice channel object


    :return: Zenora guild voice channel object
    :rtype: zenora.channel.GuildVoiceChannel
    """

    __slots__ = ["data"]

    def __init__(self, data) -> None:
        self.data = data

    @property
    def id(self) -> typing.Optional[int]:
        """Returns The snowflake ID of the channel."""
        return self.data["id"]

    @property
    def name(self) -> typing.Optional[str]:
        """Returns the name of the channel."""
        return self.data["name"]

    @property
    def position(self) -> typing.Optional[int]:
        """Returns the position of the channel."""
        return self.data["position"]

    @property
    def is_nsfw(self) -> typing.Optional[bool]:
        """Returns if the channel is NSFW or not."""
        return self.data["nsfw"]

    @property
    def bitrate(self) -> typing.Optional[int]:
        """Returns the bitrate of the channel."""
        return self.data["bitrate"]

    @property
    def user_limit(self) -> typing.Optional[int]:
        """Returns the user limit of the channel."""
        return self.data["nsfw"]

    @property
    def permission_overwrites(self) -> datetime.timedelta:
        """Returns the permission overwrites of the channel."""
        return self.data["permission_overwrites"]

    @property
    def guild_id(self) -> typing.Optional[int]:
        """Returns the snowflake ID of the channel's guild."""
        return self.data["guild_id"]

    @property
    def category_id(self) -> datetime.timedelta:
        """Returns the snowflake ID of the parant category of the channel."""
        return self.data["parent_id"]

    def __str__(self):
        """String representation of the model."""
        attrs = [
            ("id", self.id),
            ("name", self.name),
            ("position", self.position),
            ("is_nsfw", self.is_nsfw),
            ("permission_overwrites", self.permission_overwrites),
            ("category_id", self.category_id),
            ("guild_id", self.guild_id),
            ("bitrate", self.bitrate),
            ("user_limit", self.user_limit),
        ]
        return "%s(%s)" % (
            self.__class__.__name__,
            " ".join("%s=%r" % i for i in attrs),
        )