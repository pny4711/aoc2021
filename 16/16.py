def extract_number(input,idx):
    start_idx = idx
    val = 0
    numstr = ""
    while input[idx] == '1':
        numstr += input[idx+1:idx+5]
        idx += 5
    numstr += input[idx+1:idx+5]
    idx += 5
    val = int(numstr,2)
    return val,idx

vsum = 0

def eat_packet(input,start_idx = 0, indent = ""):
    idx = start_idx
    version = int(input[idx:idx+3],2)
    type_id = int(input[idx+3:idx+6],2)

    global vsum
    vsum += version

    if type_id == 4:
        val,end_idx = extract_number(input,idx+6)
        print(f"  {indent}{val}")
        idx = end_idx
    else:
        lt_id = int(input[idx+6])
        subpacket_values = []
        if lt_id == 0:
            sub_packet_length = int(input[idx+7:idx+22],2)
            sub_packet_end = idx + 22 + sub_packet_length
            end_idx = idx+22
            while end_idx < sub_packet_end:
                sval, end_idx = eat_packet(input,end_idx, indent + "    ")
                subpacket_values.append(sval)
            idx = sub_packet_end
        else:
            nr_sub_packets = int(input[idx+7:idx+18],2)
            idx += 18
            for p in range(nr_sub_packets):
                sval,idx = eat_packet(input, idx, indent + "    ")
                subpacket_values.append(sval)
        if type_id == 0:    
            val = sum(subpacket_values)
            print(f"  {indent}{val} = {' + '.join([str(sv) for sv in subpacket_values])}")
        elif type_id == 1:
            val = 1
            for sv in subpacket_values:
                val *= sv
            print(f"  {indent}{val} = {' * '.join([str(sv) for sv in subpacket_values])}")
        elif type_id == 2:
            val = min(subpacket_values)
            print(f"  {indent}{val} = min({','.join([str(sv) for sv in subpacket_values])})")
        elif type_id == 3:
            val = max(subpacket_values)
            print(f"  {indent}{val} = max({','.join([str(sv) for sv in subpacket_values])})")
        elif type_id == 5:
            val =  int(subpacket_values[0] > subpacket_values[1])
            print(f"  {indent}{val} = {subpacket_values[0]} > {subpacket_values[1]}")
        elif type_id == 6:
            val =  int(subpacket_values[0] < subpacket_values[1])
            print(f"  {indent}{val} = {subpacket_values[0]} < {subpacket_values[1]}")
        elif type_id == 7:
            val =  int(subpacket_values[0] == subpacket_values[1])
            print(f"  {indent}{val} = {subpacket_values[0]} == {subpacket_values[1]}")

    return val,idx

def make_bits(hexstring):
    bits = ""
    hs = ["0000","0001","0010","0011",
          "0100","0101","0110","0111",
          "1000","1001","1010","1011",
          "1100","1101","1110","1111",]
    for h in hexstring:
        bits +=  hs[int(h,16)]
    return bits

val_b, _ = eat_packet(make_bits(open('16.input').read().strip()))
print(f"a: {vsum}")
print(f"b: {val_b}")
