#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

from __future__ import absolute_import
import six
from thrift.util.Recursive import fix_spec
from thrift.Thrift import *
from thrift.protocol.TProtocol import TProtocolException


import includes.ttypes


import pprint
import warnings
from thrift import Thrift
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol
from thrift.protocol import THeaderProtocol
try:
  from thrift.protocol import fastproto
except:
  fastproto = None
all_structs = []
UTF8STRINGS = bool(0) or sys.version_info.major >= 3

__all__ = ['UTF8STRINGS', 'MyStruct']

class MyStruct:
  """
  Attributes:
   - MyIncludedField
  """

  thrift_spec = None
  thrift_field_annotations = None
  thrift_struct_annotations = None
  __init__ = None
  @staticmethod
  def isUnion():
    return False

  def read(self, iprot):
    if (isinstance(iprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0)
      return
    if (isinstance(iprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(iprot, THeaderProtocol.THeaderProtocol) and iprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastproto is not None:
      fastproto.decode(self, iprot.trans, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2)
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.MyIncludedField = includes.ttypes.Included()
          self.MyIncludedField.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if (isinstance(oprot, TBinaryProtocol.TBinaryProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_BINARY_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=0))
      return
    if (isinstance(oprot, TCompactProtocol.TCompactProtocolAccelerated) or (isinstance(oprot, THeaderProtocol.THeaderProtocol) and oprot.get_protocol_id() == THeaderProtocol.THeaderProtocol.T_COMPACT_PROTOCOL)) and self.thrift_spec is not None and fastproto is not None:
      oprot.trans.write(fastproto.encode(self, [self.__class__, self.thrift_spec, False], utf8strings=UTF8STRINGS, protoid=2))
      return
    oprot.writeStructBegin('MyStruct')
    if self.MyIncludedField != None:
      oprot.writeFieldBegin('MyIncludedField', TType.STRUCT, 1)
      self.MyIncludedField.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def __repr__(self):
    L = []
    for key, value in six.iteritems(self.__dict__):
      padding = ' ' * 4
      value = pprint.pformat(value, indent=0)
      value = padding.join(value.splitlines(True))
      L.append('    %s=%s' % (key, value))
    return "%s(\n%s)" % (self.__class__.__name__, ",\n".join(L))

  def __eq__(self, other):
    if not isinstance(other, self.__class__):
      return False

    return self.__dict__ == other.__dict__ 

  def __ne__(self, other):
    return not (self == other)

  # Override the __hash__ function for Python3 - t10434117
  if not six.PY2:
    __hash__ = object.__hash__

all_structs.append(MyStruct)
MyStruct.thrift_spec = (
  None, # 0
  (1, TType.STRUCT, 'MyIncludedField', [includes.ttypes.Included, includes.ttypes.Included.thrift_spec, False], includes.ttypes.Included(**{
    "MyIntField" : 5,
  }), 2, ), # 1
)

MyStruct.thrift_struct_annotations = {
}
MyStruct.thrift_field_annotations = {
}

def MyStruct__init__(self, MyIncludedField=MyStruct.thrift_spec[1][4],):
  if MyIncludedField is self.thrift_spec[1][4]:
    MyIncludedField = includes.ttypes.Included(**{
    "MyIntField" : 5,
  })
  self.MyIncludedField = MyIncludedField

MyStruct.__init__ = MyStruct__init__

fix_spec(all_structs)
del all_structs
