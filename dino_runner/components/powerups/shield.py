from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.powerups.power_up import PowerUp

SHIELD_IMG = {SHIELD_TYPE: SHIELD}


class Shield(PowerUp):
    def __init__(self):
        self.type = SHIELD_TYPE
        self.image = SHIELD_IMG[self.type][0]
        self.index_type = 0
        super().__init__(self.image, self.type)