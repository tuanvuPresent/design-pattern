class TurnOnCommand:
    def execute(self):
        print('turn on')


class TurnOffCommand:
    def execute(self):
        print('turn off')


class Remote:
    _command = None

    def set_command(self, command):
        self._command = command

    def run(self):
        self._command.execute()


if __name__ == '__main__':
    turn_on_command = TurnOnCommand()
    turn_off_command = TurnOffCommand()
    remote = Remote()

    remote.set_command(turn_on_command)
    remote.run()
    remote.set_command(turn_off_command)
    remote.run()
