def get_literal_value(input,idx):
    val = 0
    numstr = ""
    while input[idx] == '1':
        numstr += input[idx+1:idx+5]
        idx += 5
    numstr += input[idx+1:idx+5]
    idx += 5
    val = int(numstr,2)
    return val,idx

def get_number(input, idx, length):
    return int(input[idx:idx+length],2),idx+length

def eval_packet(input,idx = 0):
    version, idx = get_number(input, idx, 3)
    type_id, idx = get_number(input, idx, 3)

    if type_id == 4:
        val, idx = get_literal_value(input, idx)
    else:
        lt_id, idx = get_number(input,idx, 1)
        subpacket_values = []
        if lt_id == 0:
            sub_packet_length, idx = get_number(input, idx, 15)
            sub_packet_end = idx + sub_packet_length
            while idx < sub_packet_end:
                sval, idx, sv = eval_packet(input, idx)
                subpacket_values.append(sval)
                version += sv
        else:
            nr_sub_packets, idx = get_number(input, idx, 11)
            for p in range(nr_sub_packets):
                sval, idx, sv = eval_packet(input, idx)
                subpacket_values.append(sval)
                version += sv
        if type_id == 0:    
            val = sum(subpacket_values)
        elif type_id == 1:
            val = 1
            for sv in subpacket_values:
                val *= sv
        elif type_id == 2:
            val = min(subpacket_values)
        elif type_id == 3:
            val = max(subpacket_values)
        elif type_id == 5:
            val =  int(subpacket_values[0] > subpacket_values[1])
        elif type_id == 6:
            val =  int(subpacket_values[0] < subpacket_values[1])
        elif type_id == 7:
            val =  int(subpacket_values[0] == subpacket_values[1])

    return val, idx, version

def make_bits(hexstring):
    return "".join(["{0:04b}".format(int(h,16)) for h in hexstring])

val_b, _, vsum = eval_packet(make_bits(open('16.input').read().strip()))
print(f"a: {vsum}")
print(f"b: {val_b}")
