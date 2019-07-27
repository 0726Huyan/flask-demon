from wtforms.validators import ValidationError
import re
class My_Length(object):
    def __init__(self,min=-1,max=-1,message=None):
        self.min=min
        self.max=max
        if not message:
            message='min~max input please'
        self.message=message
    def __call__(self, form,field):
        l = field.data and len(field.data) or 0
        if l<self.min or self.max !=-1 and l>self.max:
            raise ValidationError('len must be less than 5')
class cheak_Mail(object):
    def __init__(self,message=None):
        if not message:
            message='格式错误'
        self.message = message
    def __call__(self, form,field):
        l =field.data and len(field.data) or 0
        if not re.findall(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',l):
            raise ValidationError('邮箱格式错误')

