pinmodes = []
for i in range(0, 8):
    print(f"Enter GPIO pin {i} mode:")
    mode = input()
    if mode == "in":
        pinmodes.append('0')
    elif mode == "out":
        pinmodes.append('1')
st = ''.join(pinmodes)
st = '0b' + st
with open("init.c", 'w') as fd:
    fd.write("void PORTA_DIR(void) {\n\tDDRA = %s;\n}" % st)
