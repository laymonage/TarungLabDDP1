'''
Program pengekstrak informasi rahasia Agen Benny.

Program menerima input berupa nama file teks input dan output.
File input berisi teks yang mengandung tag <start> dan <end> untuk
menandakan informasi rahasia.
'''

user_input = input("Masukkan nama file input dan output: ")
input_name = user_input.split(" ", 1)[0]
output_name = user_input.split(" ", 1)[1]

try:
    input_file = open(input_name, "r")
    output_file = open(output_name, "w+")

except FileNotFoundError:
    print("File {} bermasalah! Benny lolos kali ini.".format(input_name))

else:
    message = []
    for input_line in input_file:
        input_line = input_line.strip()
        pos = -1
        while True:
            pos = input_line.find("<start>", pos + 1)
            if pos == -1:
                break
            part = input_line[input_line.find("<start>", pos) +
                              len("<start>"):input_line.find("<end>", pos)]
            part = part.strip()
            message.append(part)

    output = " ".join(message)
    print(output, end="", file=output_file)
    input_file.close()
    print("Rahasia telah terbongkar, silakan cek file {}".format(output_name))

finally:
    output_file.close()
