def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            lines.append(line.strip())
    return lines
def convert(lines):
    new=[]
    date = None
    for line in lines:
        if line == '2020.04.05 星期日':
            date = '2020.04.05 星期日'
            continue
        elif line == '2020.07.21 星期二':
            date = '2020.07.21 星期二'
            continue
        elif line == '2020.07.26 星期日':
            date = '2020.07.26 星期日'
            continue
        if date:
            new.append(date + ' ' + line)
    return new
def count(lines):
    cheng_sticker_count=0
    zhi_sticker_count=0
    cheng_word_count = 0
    zhi_word_count = 0
    for line in lines:
        s = line.split(' ')
        date = s[0]
        week = s[1]
        time = s[2]
        name = s[3]
        if name == 'cheng':
            if s[4] == '貼圖':
                cheng_sticker_count += 1
            else:
                for msg in s[4:]:
                    cheng_word_count += len(msg)
        if name == '陳韋至':
            if s[4] == '貼圖':
                zhi_sticker_count += 1
            else:
                for msg in s[4:]:
                    zhi_word_count += len(msg)
    print('cheng說了', cheng_word_count, '個字' , '輸入貼圖有', cheng_sticker_count, '張')            
    print('陳韋至說了', zhi_word_count, '個字', '輸入貼圖有', zhi_sticker_count, '張')
    
        


def write_file(filename,lines):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('[LINE]陳韋至.txt')
    lines = convert(lines)
    write_file('output_LINE.txt', lines)
    count(lines)

main()
