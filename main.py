from encryption_utils import Encoder
from encryption_utils import Decoder
from generator import CoverGenerator


def display_menu():
    print('=' * 50)
    print('-' * 50)
    print('[1] generate a cover')
    print('[2] decode the cover')
    print('[q] QUIT')
    print('-' * 50)


def generate_a_cover():
    raw_input = input('Please enter your feeling today:')
    encoder = Encoder(raw_input)
    raw_digst = encoder.encode()
    color = encoder.color_generator(raw_digst)

    color_generator = CoverGenerator(color)
    img = color_generator.generate()

    file_path = color_generator.save(img)
    color_generator.save_to_mongo(raw_digst, color, raw_input, file_path)


def decode_a_cover():
    input_str = input('please enter the filename or color band:')
    print(input_str)
    if isinstance(eval(repr(input_str)), tuple):
        decoder = Decoder(color=list(input_str))
    else:
        decoder = Decoder(file_path=input_str)

    res = decoder.decode()
    print(res)


while True:
    display_menu()
    choice = input('please enter your choice')

    if choice == '1':
        generate_a_cover()
    elif choice == '2':
        decode_a_cover()
        exit()
    elif choice == 'q':
        exit()
    else:
        print("please enter a correct choice")
        continue
