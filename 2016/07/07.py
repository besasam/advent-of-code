import re


def prepare_data(ip):
    sequences = []
    hypernet = []
    pos = 0
    lb = [c.start() for c in re.finditer('\[', ip)]
    rb = [c.start() for c in re.finditer('\]', ip)]
    for i in range(len(lb)):
        sequences.append(ip[pos:lb[i]])
        hypernet.append(ip[lb[i]+1:rb[i]])
        pos = rb[i]+1
    if pos < len(ip):
        sequences.append(ip[pos:])
    return {
        'seq': sequences,
        'hyp': hypernet
    }


def is_abba(sequence):
    i = 0
    while i < len(sequence) - 3:
        if sequence[i] == sequence[i+3] and sequence[i+1] == sequence[i+2] and sequence[i] != sequence[i+1]:
            return True
        i += 1
    return False


def supports_tls(ip):
    p_ip = prepare_data(ip)
    for hyp in p_ip['hyp']:
        if is_abba(hyp):
            return False
    for seq in p_ip['seq']:
        if is_abba(seq):
            return True
    return False


def find_xyx(sequence):
    xyx = []
    i = 0

    return xyx


def find_aba(sequence):
    matches = []
    i = 0
    while i < len(sequence) - 2:
        if sequence[i] == sequence[i+2] and sequence[i] != sequence[i+1]:
            if i < len(sequence) - 3:
                matches.append(sequence[i:i+3])
                #yield sequence[i:i+3]
            else:
                matches.append(sequence[i:])
                #yield sequence[i:]
        i += 1
    return matches


def corresponds(aba, bab):
    return aba[0] == bab[1] and aba[1] == bab[0]


def supports_ssl(ip):
    p_ip = prepare_data(ip)
    seq_aba = []
    for sequence in p_ip['seq']:
        for aba in find_aba(sequence):
            seq_aba.append(aba)
    if not seq_aba:
        return False
    hyp_aba = []
    for sequence in p_ip['hyp']:
        for aba in find_aba(sequence):
            hyp_aba.append(aba)
    if not hyp_aba:
        return False
    for aba in seq_aba:
        for bab in hyp_aba:
            if corresponds(aba, bab):
                return True
    return False


def part_1(ips):
    tls_ips = [ip for ip in ips if supports_tls(ip)]
    return len(tls_ips)


def part_2(ips):
    ssl_ips = [ip for ip in ips if supports_ssl(ip)]
    return len(ssl_ips)


with open('input.txt') as f:
    data = f.read().splitlines()

print(part_2(data))