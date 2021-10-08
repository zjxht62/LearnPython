import os
import turtle

class Command:
    def __init__(self, option, value=None, func=None):
        self.option = option
        self.value = value
        self.func = func

    def __str__(self):
        return f'操作：{self.option}，值：{self.value}, 方法：{self.func}'

    def __repr__(self):
        return self.__str__()




class Translator:
    def __init__(self, code_file):
        self.code_file = code_file

    def translate_to_text_list(self):
        command_text_list = []
        with open(self.code_file) as file:
            for line in file:
                line = line.replace(" ", '')
                line = line.replace('\n', '')
                command_text_list.append(line)
        return command_text_list

    def translate_to_command_obj_list(self):
        command_obj_list = []
        for command_text in self.translate_to_text_list():
            command_obj_list.append(
                Command(command_text[:1], command_text[1:]))
        return command_obj_list


class Actuator:
    def __init__(self, pen):
        self.pen = pen

    def process_commands(self, command_obj_list):
        for command in command_obj_list:
            if command.option == 'D':
                self.pen.pendown()
            if command.option == 'W':
                self.pen.lt(180)
                self.pen.fd(int(command.value))
                self.pen.rt(180)
            if command.option == 'E':
                self.pen.fd(int(command.value))
            if command.option == 'N':
                self.pen.lt(90)
                self.pen.fd(int(command.value))
                self.pen.rt(90)
            if command.option == 'S':
                self.pen.rt(90)
                self.pen.fd(int(command.value))
                self.pen.lt(90)
            if command.option == 'U':
                self.pen.penup()


if __name__ == '__main__':
    translator = Translator(code_file='commands.txt')
    command_obj_list = translator.translate_to_command_obj_list()
    s = turtle.getscreen()
    t = turtle.Turtle()
    actuator = Actuator(t)
    actuator.process_commands(command_obj_list)
    s.mainloop()
