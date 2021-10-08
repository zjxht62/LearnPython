import os
import turtle

def pen_p_fun(pen, value):
    pen.color('red')

def pen_down_fun(pen, value):
    pen.pendown()


def pen_north_fun(pen, value):
    pen.lt(90)
    pen.fd(int(value))
    pen.rt(90)


def pen_south_fun(pen, value):
    pen.rt(90)
    pen.fd(int(value))
    pen.lt(90)


def pen_east_fun(pen, value):
    pen.fd(int(value))


def pen_west_fun(pen, value):
    pen.lt(180)
    pen.fd(int(value))
    pen.rt(180)


def pen_up_fun(pen, value):
    pen.penup()

command_dict = {
    'P':pen_p_fun,
    'D':pen_down_fun,
    'U':pen_up_fun,
    'W':pen_west_fun,
    'E':pen_east_fun,
    'S':pen_south_fun,
    'N':pen_north_fun
}


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
    command_text_list = translator.translate_to_text_list()
    print(command_text_list)
    s = turtle.getscreen()
    t = turtle.Turtle()
    for command_text in command_text_list:
        command_key = command_text[:1]
        command_value = int(command_text[1:]) if command_text[1:] !='' else None
        command_dict[command_key](t, command_value)
    # actuator = Actuator(t)
    # actuator.process_commands(command_obj_list)
    s.mainloop()
