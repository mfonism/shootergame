from ppb import Vector
from ppb.events import Update
from ppb.events import StopScene
from ppb.systemslib import System

from shooter import values
from shooter.events import EnemiesClear
from shooter.events import GameOver
from shooter.events import SetLives
from shooter.events import SpawnPlayer
from shooter.sprites import gameplay as game_sprites
from shooter.sprites import ui

__all__ = [
    "LifeCounter"
]


class LifeCounter(System):
    lives = values.player_starting_lives
    player_spawn_request = False
    enemies_clear = False

    @staticmethod
    def spawn_player(scene):
        player = game_sprites.Player()
        scene.add(player, tags=["ship", "player"])

    def on_player_died(self, died, signal):
        next(died.scene.get(tag=f"life_{self.lives}")).kill(died.scene)

    def on_set_lives(self, command: SetLives, signal):
        """Signalled by a game load, resets lives and spawns a player."""
        self.lives = values.player_starting_lives
        for life in command.scene.get(tag="life_ui"):
            command.scene.remove(life)
        for i in range(1, self.lives + 1):
            command.scene.add(
                ui.LifeSymbol(position=Vector(-4.5 + ((i - 1) * ui.LifeSymbol.size * 2), 9.5)),
                tags=["life_ui", f"life_{i}"]
            )
        self.spawn_player(command.scene)

    def on_spawn_player(self, spawn: SpawnPlayer, signal):
        """Commanded to spawn a new player"""
        self.player_spawn_request = True

    def on_enemies_clear(self, enemies_clear: EnemiesClear, signal):
        self.enemies_clear = True

    def on_update(self, update: Update, signal):
        if self.player_spawn_request and self.enemies_clear:
            self.player_spawn_request = False
            self.enemies_clear = False
            self.lives -= 1
            if self.lives:
                self.spawn_player(update.scene)
            else:
                signal(GameOver())
                signal(StopScene())
