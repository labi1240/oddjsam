#region Imports
from Base import ModelBase;
from Enum import SportsEnum;
from dataclasses import dataclass
#endregion Imports

@dataclass
class Game(ModelBase):
    id: int = None;
    sport: SportsEnum = None;
    league: str = None;
    start_date: str = None;
    away_team: str = None;
    home_team: str = None;
    is_live: bool = None;