
#！/usr/bin/python3
# -*- coding:utf-8 -*-
# author centyuan
# @time 19-10-18 下午1:33

import uuid

print(uuid.uuid1())
print(uuid.uuid3(uuid.NAMESPACE_DNS,'yuanlin'))
print(uuid.uuid4())
print(uuid.uuid5(uuid.NAMESPACE_DNS,'yuanlin'))


str = "3cfc8d7a-f169-11e9-af5b-58a023321f81"
str_2= "".join(str.split('-'))
print(str_2)
print(len(''.join(str.split('-'))))

"""
uuid1()：这个是根据当前的时间戳和MAC地址生成的，最后的12个字符408d5c985711对应的就是MAC地址，因为是MAC地址，那么唯一性应该不用说了。但是生成后暴露了MAC地址这就很不好了。

uuid3()：里面的namespace和具体的字符串都是我们指定的，然后呢···应该是通过MD5生成的，这个我们也很少用到，莫名其妙的感觉。

uuid4()：这是基于随机数的uuid，既然是随机就有可能真的遇到相同的，但这就像中奖似的，几率超小，因为是随机而且使用还方便，所以使用这个的还是比较多的。

uuid5()：这个看起来和uuid3()貌似并没有什么不同，写法一样，也是由用户来指定namespace和字符串，不过这里用的散列并不是MD5，而是SHA1.
"""