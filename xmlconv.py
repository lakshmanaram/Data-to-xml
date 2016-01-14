import os
def convert(a):
    f = open("resume.xml","a")
    flag = False
    tag = ""
    tag += '<' + a.name
    if a.have_attributes():
        tag += ' '
        for i in a.atts:
            tag += i[0] + "=" + '"' + i[1] + '" '
    tag += "> "
    if a.isdata():
        tag += a.data + " "
        flag = True
    else:
        tag += '\n'
    f.write(tag)
    f.close()
    if a.have_elements():
        for i in a.elements:
            temp_flag = convert(i)
            flag |= temp_flag
    if(flag == False):
        nf = open("resume.xml","rb+")
        nf.seek(0,2)
        size = nf.tell()
        nf.truncate(size - len(tag))
        nf.close()
        return False
    f = open("resume.xml","a")
    f.write('</' + a.name + '>\n')
    f.close()
    return True

def xmlconvert(a):
    try:
        os.remove("resume.xml")
        convert(a)
    except:
        convert(a)
