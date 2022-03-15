import csv
import re

def tokenize(original_text):

    rx = r"\S+"
    sent_text = original_text
    #print(sent_text)
    spans = []
    ai = 0                    
    for r in re.finditer(rx, sent_text):
        spans.append([r.span()[0], r.span()[1], ai])
        ai+=1

    new_spans = []
    for span in spans:
        spilt_token(span, new_spans, sent_text, span[0])

    r_str = []
    for span in new_spans:
        begin = span[0] # word_start + sen_begin
        end = span[1]
        aid = span[2]
        r_str.append(sent_text[begin:end])
    
    return ' '.join(r_str)


def spilt_token(span, new_spans, str, offset):

    tok_str = str[span[0]:span[1]]

    if not tok_str.strip():
        return

    p_ch = tok_str[0]
    start = 0
    for i in range(len(tok_str)):
        ch = tok_str[i]
        if_c = False

        if i > 0:
            if ch.isdigit():
                if not p_ch.isdigit():
                    if_c = True
            elif ch.islower():
                if not (p_ch.islower() or p_ch.isupper()):
                    if_c = True
            elif ch.isupper():
                if not p_ch.isupper():
                    if_c= True
                elif i < len(tok_str) - 1 and tok_str[i + 1].islower():
                    if_c = True
            else:
                if_c = True
        # end if

        if if_c and not ch.isspace():
            begin = start
            end = i
            if p_ch.isspace():
                end = end - 1

            new_spans.append([begin + offset, end + offset, span[2]])
            start = i

        p_ch = ch
    # end for
    new_spans.append([start + offset, len(tok_str) + offset, span[2]])

def main():
    inputFile = open('cleaned-Training-2.csv')
    csvreader = csv.reader(inputFile)

    header = []
    header = next(csvreader)

    rows = []

    with open('cleanedTrainingVowpal-2.txt', 'w') as f:
        for row in csvreader:
            #text = row[0].replace(":", "")
            text = tokenize(row[0].replace(":", ""))
            outputLine = row[1] + " |w " + text + "\n"
            f.write(outputLine)
            rows.append(row)

    f.close()

if __name__ == '__main__':
    main()
