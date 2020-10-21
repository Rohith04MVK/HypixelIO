"""This module is dedicated to definition of the Booster's Info class."""


class BoosterInfo:
    """
    This is the definition of the Custom Hypixel API Booster's Info Model.
    """
    def __init__(
        self,
        info: dict
    ) -> None:
        self.ID = info["_id"]
        self.PURCHASER_UUID = info["purchaserUuid"]

        self.AMOUNT = info["amount"]
        self.ORIGINAL_LENGTH = info["originalLength"]
        self.LENGTH = info["length"]

        self.GAME_TYPE_CODE = info["gameType"]
        self.DATE_ACTIVATED = info["dateActivated"]

        self.STACKED = True if "stacked" in info else False