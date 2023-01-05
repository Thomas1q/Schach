import asyncio
import chess

from chess4b.logic.base import LogicBase
from chess4b.ui import GuiGameLoop


class LogicGame(LogicBase):
    def __init__(self, loop: asyncio.events.AbstractEventLoop, conn, host: bool):
        super().__init__(loop)
        self.host: bool = host

        self.board = chess.Board()
        self.gui = GuiGameLoop()

    async def host_game_loop(self):
        await self.h_display_board()
        while not self.board.is_checkmate():
            # Host Turn
            h_move = await self.gui.wait_move()
            if await self.validate_move(h_move):
                self.execute_move()
                await self.h_display_board()

            # Client Turn
            c_move = await self.conn.wait_move()
            if await self.validate_move(c_move):
                self.execute_move()
                await self.h_display_board()

    async def client_game_loop(self):
        await self.c_display_board()
        while not self.board.is_checkmate():
            # Host Turn
            await self.c_display_board()

            move = await self.gui.wait_move()
            if not await self.conn.validate_move(move):
                continue

    async def c_display_board(self):
        self.board = await self.conn.recv_board(self.board)
        await self.gui.display_board(self.board)

    async def h_display_board(self):
        await self.conn.send_board(self.board)
        await self.gui.display_board(self.board)

    def run(self):
        pygame_task = self.loop.run_in_executor(None, self.pygame_event_loop)
        if self.host:
            game_task = asyncio.ensure_future(self.host_game_loop(), loop=self.loop)
        else:
            game_task = asyncio.ensure_future(self.client_game_loop(), loop=self.loop)
        event_task = asyncio.ensure_future(self.handle_events(), loop=self.loop)

        pygame.init()
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            pygame_task.cancel()
            game_task.cancel()
            event_task.cancel()
            self.loop.stop()


if __name__ == '__main__':
    game = LogicGame(asyncio.new_event_loop(), "xxx", True)
