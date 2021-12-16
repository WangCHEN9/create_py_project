from sample.get_solid import GetSolid

class hi:
    """hiiiiii
    """
    def say_hi(self) -> str:
        """call get_solid function and return response

        :return: [response from get_solid]
        :rtype: str
        """
        rep = GetSolid().get_solid()
        return rep