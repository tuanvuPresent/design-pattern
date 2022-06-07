"""
Facade không đóng gói các lớp hệ thống con;
Facade chỉ đơn thuần cung cấp một giao diện đơn giản hóa cho chức năng của chúng.
Các lớp hệ thống con vẫn có sẵn để sử dụng trực tiếp bởi các client cần sử dụng các giao diện cụ thể hơn.

Đây là một thuộc tính tuyệt vời của Facade Pattern:
nó cung cấp giao diện đơn giản hóa trong khi vẫn có đầy đủ chức năng của hệ thống cho những người có thể cần nó.
"""


class Cpu:
    def execute(self):
        print('execute')


class HardDrive:
    def read(self):
        print('read')


class Memory:
    def load(self):
        print('load')


class ComputerFacade:
    def __init__(self, cpu: Cpu, hard_drive: HardDrive, memory: Memory):
        self._cpu = cpu
        self._memory = memory
        self._hard_drive = hard_drive

    def start(self):
        self._memory.load()
        self._hard_drive.read()
        self._cpu.execute()


computer = ComputerFacade(Cpu(), HardDrive(), Memory())
computer.start()
