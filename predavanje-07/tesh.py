def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00'+s[2:]
        else:
            return s[:-2]
    elif s[:2] == '12':
        return s[:-2]
    else:
        if (int(s[:2])+12)%24 > 10:
            return str((int(s[:2])+12)%24)+s[2:-2]
        else:
            return '0'+str((int(s[:2])+12)%24)+s[2:-2]

print(timeConversion('12:01:00PM'))
print(timeConversion('12:01:00AM'))
print(timeConversion('07:01:00PM'))