# # 输入
# name = input()
# age = input('enter ur age: ')
# # 三元表达式
# unit = ' years' if int(age) > 0 else ' year'
# # 输出
# print('ur name is ' + name)

# print('and u r ' + age + unit + ' old')

# sentence = 'i\'m wz, and r u \"OK" ?'
# print(sentence)

# sentence_ = '\\\22e2\\'  # \e2\
# sentence__ = r'\\\222\\'  # \\\222\\
# print(sentence_)
# print(sentence__)
# print('the score is %d' % 96)  # the score is 96
# print('the score is %5d' % 96)  # the score is    96
# print('the score is %05d' % 96)  # the score is 00096

# # %f 没有指定小数点的时候 会 五舍六入到小数点后6位(如下代码)
# print('the score is %f' %
#       96.12345)  # the score is 96.123450   # 末尾会补0 直到小数点后六位(未知原因) TODO;
# print('the score is %f' % 96.123456)  # the score is 96.123456
# print('the score is %f' % 96.1234567)  # the score is 96.123457
# print('the score is %f' % 96.1234546)  # the score is 96.123455
# print('the score is %f' % 96.1234545)  # the score is 96.123454

print('the score is %.3f' % 96.1234)  # the score is 96.123

# 没有小数点的时候 %0Xf 会保留小数点后6位 没有的用0补充, 遵循四舍五入
print('the score is %03f' % 96.12345)  # the score is 96.123450
print('the score is %03f' % 96.123456)  # the score is 96.123456
print('the score is %03f' % 96.1234561)  # the score is 96.123456
print('the score is %03f' % 96.1234564)  # the score is 96.123456
print('the score is %03f' % 96.1234565)  # the score is 96.123457
