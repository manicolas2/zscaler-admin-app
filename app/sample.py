from textual import events
from textual.app import App
from textual.widgets import Placeholder
import yaml

with open('./config.yml', 'r') as yml:
    config = yaml.load(yml)

LOGFILE = config['log-settings']['logfile']

class ColorChanger(App):
    async def on_key(self, event):
        if event.key.isdigit():
            self.background = f"on color({event.key})"


# ColorChanger.run(log=LOGFILE)

class SimpleApp(App):

    async def on_mount(self, event: events.Mount) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(Placeholder(), Placeholder(), edge="top")


SimpleApp.run(log="textual.log")