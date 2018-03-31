from decryptTools import score

ciphertext = '--.-.-.-.- -.....-... ...-..-..... .....-..- -..-. ---- .......-.-. -..-. ..-.---.-. --.----.. ...--- .-..---...-.-.. -..... .-----.-..-..-.. -.....-- ..... --..-...-. ......... ----.. .--.-.. ----..-..-.-- ...----. -.....-- .--....---....-..-. -.....-........-.... ..-. ......-- ........-.-...-.. -.---- .--...-.......... -.....-- .....-...-. .-..-.-..-.-.. .-......-.. ..-.---.-. --.----.. -....-.. -.---- ....-.-.. ......... ...----. ..-.---- -..... .-----.-..-..-.. ---- -.-.----.-...---. -..... .-----.-..-..-.. -.....-- ---- ....-...-. -..... .-----.-..-..-.. -.....-.---..---..... ......--'

conversion = {'..-.': 'F', '-..-': 'X', '.--.': 'P', '-': 'T', '..---': '2',
              '....-': '4', '-----': '0', '--...': '7', '...-': 'V',
              '-.-.': 'C', '.': 'E', '.---': 'J', '---': 'O', '-.-': 'K',
              '----.': '9', '..': 'I', '.-..': 'L', '.....': '5', '...--': '3',
              '-.--': 'Y', '-....': '6', '.--': 'W', '....': 'H', '-.': 'N',
              '.-.': 'R', '-...': 'B', '---..': '8', '--..': 'Z', '-..': 'D',
              '--.-': 'Q', '--.': 'G', '--': 'M', '..-': 'U', '.-': 'A',
              '...': 'S', '.----': '1'}

s = set(conversion)
al = '|'+'|'.join(s)+'|'

def search(i=0, prev=''):
    branch = {}
    for nex in '.-':
        if '|'+prev+nex in al:
            branch[nex] = search(i+1, prev+nex)
    if prev in s:
        branch['char']=conversion[prev]
    else:
        branch['char']=None
    return branch

tree = search()

def generate_endings(rem, branch=tree, incomplete=False):
    if not rem:
        if incomplete:
            return []
        else:
            return ['']
    possibilities = []
    nex = rem[0]
    rest = rem[1:]
    if nex in branch:
        limb = branch[nex]
        char = limb['char']
        if limb['char']:
            endings = generate_endings(rest, tree)
            if endings:
                possibilities += [char + other for other in endings]
        endings = generate_endings(rest, limb, True)
        if endings:
            possibilities += endings
    return possibilities
    

chunks = ciphertext.split(' ')
poss_list = []
for c, chunk in enumerate(chunks):
    print()
    print(chunk)
    print()
    remaining = ' '.join(chunks[c:])
    poss_list.append(generate_endings(chunk))
    sort = sorted(poss_list[-1],
                 key=lambda x:(len([c for c in x if c not in '1234567890'])/
                               float(len(x)),
                               score(x)/(len(x)**1.0)),
                  # increase 1.0 to make shorter words sort closer to the start
                  # and decrease to make longer words come sooner
                 reverse = True
                 )
    i = 0
    cont = True
    while cont:
        try:
            line = sort[i]
        except IndexError:
            print('no more possibilites to show.')
            break
        i += 1
        while True:
            try:
                newline = line+' '+sort[i]
            except IndexError:
                break
            if len(newline) > 80:
                break
            line = newline
            i += 1
        print(line)
        cont = input('Press enter to continue, or type more to show more: ')
