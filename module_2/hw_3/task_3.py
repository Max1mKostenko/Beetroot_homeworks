class TVController:
    current_channel_index = 0

    def __init__(self, channels: list):
        self.channels = channels

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, channel: int):
        if 0 < channel < 4:
            TVController.current_channel_index = channel - 1
            return self.channels[TVController.current_channel_index]
        else:
            return f"Channel with number {channel} doesn't exist! You've only {len(self.channels)} channels"

    def next_channel(self):
        if TVController.current_channel_index + 1 == len(self.channels):
            return self.channels[0]
        else:
            return self.channels[TVController.current_channel_index + 1]

    def previous_channel(self):
        if TVController.current_channel_index == 0:
            return self.channels[-1]
        else:
            return self.channels[TVController.current_channel_index - 1]

    def current_channel(self):
        return self.channels[TVController.current_channel_index]

    def is_exist(self, channel):
        if channel in range(1, len(self.channels) + 1) or channel in self.channels:
            return "Yes"
        else:
            return "No"


controller = TVController(["BBC", "Discovery", "TV1000"])
print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist(4) == "No")
print(controller.is_exist("BBC") == "Yes")
