import socket
import pygame
import asyncio


class LogicBase:
    def __init__(self, loop: asyncio.events.AbstractEventLoop = None, auto_setup: bool = True, auto_run: bool = True):
        self.connection: socket.socket | None = None
        self.loop: asyncio.events.AbstractEventLoop = loop

        self.user_data: dict = {}
        self.enemy_data: dict = {}

        if auto_setup or auto_run:
            self._setup()

        self.screen: pygame.Surface | None = None
        self.event_queue: asyncio.Queue = asyncio.Queue()

        if auto_run:
            self.run()

    def _setup(self):
        if not self.loop:
            self.loop = asyncio.new_event_loop()

    def run(self):
        pygame_task = self.loop.run_in_executor(None, self.pygame_event_loop)
        event_task = asyncio.ensure_future(self.handle_events(), loop=self.loop)

        pygame.init()

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            pass
        finally:
            pygame_task.cancel()
            animation_task.cancel()
            event_task.cancel()
            self.loop.stop()

    def pygame_event_loop(self):
        while True:
            pygame.event.post(pygame.event.Event(pygame.NUMEVENTS))
            event = pygame.event.wait()
            asyncio.run_coroutine_threadsafe(self.event_queue.put(event), loop=self.loop)

    async def handle_events(self):
        while True:
            event = await self.event_queue.get()
            if event.type == pygame.QUIT:
                break


if __name__ == '__main__':
    lb = LogicBase()
