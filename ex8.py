formatter = "{} {} {} {}"

#ading another arg don't change anythink
print(formatter.format(1, 2, 3, 4))
print(formatter.format(True, False, False, True))
print(formatter.format("random", formatter, formatter, formatter))
print(formatter.format(
"this is random",
"will this stick text to 2 line??",
"\n ooo ",
"typed without sense (it do)"
))
