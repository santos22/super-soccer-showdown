import abc


class BaseAPIClient(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_heaviest(self):
        """Get heaviest specimen in universe"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_shortest(self):
        """Get shortest specimen in universe"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_tallest(self):
        """Get tallest specimen in universe"""
        raise NotImplementedError
