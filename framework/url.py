from dataclasses import dataclass


@dataclass
class Url:
    path: str
    controller: PageObject