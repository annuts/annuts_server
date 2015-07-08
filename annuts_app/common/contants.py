#coding:utf-8
__author__ = 'zhangdewei'

class Enum:
    def inv_dict(self):
        d = self.__dict__.values()
        if len(d) != len(set(d)):
            raise "Cannot reverse key-value because the Enum obj has duplicated values."
        return {v: k for k, v in self.__dict__.iteritems()}

    def sorted_names(self):
        return sorted(self.names(),
                      lambda a, b: cmp(self.__dict__[a], self.__dict__[b]))

    def sorted_values(self):
        return sorted(self.values())

    def names(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def __contains__(self, key):
        return key in self.values()



user_agents = Enum()
user_agents.DEFAULT = 0
user_agents.IPHONE = 1
user_agents.IPAD = 2
user_agents.IPOD = 3
user_agents.ANDROID = 4

MIMETYPE = {
    'image': 'image/png',  # 图片
    'text' : 'text/plain',  #　文件
    'stream' : 'application/octet-stream'
}