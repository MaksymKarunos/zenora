import abc
import typing


class Query(abc.ABC):
    __slots__ = ["token", "token_type"]

    def __init__(self, token: str, token_type: str):
        self.token = token
        self.token_type = token_type

    @abc.abstractmethod
    def channel(self, snonwflake: int) -> typing.Dict:
        """Interface for the REST API query to get channels.

        Parameters:
        snowflake: int
                The channel ID of a Discord channel

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def user(self, snowflake: int) -> typing.Dict:
        """Interface for the REST API query to get user.

        Parameters:
        snowflake: int
                The ID of a Discord User

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """

    @abc.abstractmethod
    def current_user(self) -> typing.Dict:
        """Interface for the REST API query to get current user.

        Returns:
        typing.Dict: A dictionary object that will be used to parse the data
            into objects
        """
