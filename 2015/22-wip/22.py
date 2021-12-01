from dataclasses import dataclass


@dataclass
class Character:
    hp: int = 100
    dmg: int = 0
    armor: int = 0
    mana: int = 0


@dataclass
class Effect:
    duration: int = 0
    dmg: int = 0
    shield: int = 0
    mana: int = 0


@dataclass
class Spell:
    cost: int = 0
    dmg: int = 0
    healing: int = 0
    effect: Effect = None


effects = {
    'shield': Effect(duration=6, shield=7),
    'poison': Effect(duration=6, dmg=3),
    'recharge': Effect(duration=5, mana=101)
}
spells = {
    'magic_missile': Spell(cost=53, dmg=4),
    'drain': Spell(cost=73, dmg=2, healing=2),
    'shield': Spell(cost=113, effect=effects['shield']),
    'poison': Spell(cost=173, effect=effects['poison']),
    'recharge': Spell(cost=229, effect=effects['recharge'])
}
player = Character(hp=50, mana=500)
boss = Character(hp=58, dmg=9)
