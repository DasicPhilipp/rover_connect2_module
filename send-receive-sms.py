# import pdb
from rover_connect2.rover_connect import RoverConnect

if __name__ == "__main__":

    rover = RoverConnect('/dev/ttyS0', 'internet.mts.ru')

    phone_number = input('Номер телефона для отправки (7XXXXXXXXXX):\n')
    message = input('Текст сообщения:\n')
    rover.send_sms(phone_number, message)

    result = rover.get_sms()
    for r in result:
        print(r[0], ' ', r[1], ' ', r[2], '\n', r[3])
    rover.delete_all_sms()
