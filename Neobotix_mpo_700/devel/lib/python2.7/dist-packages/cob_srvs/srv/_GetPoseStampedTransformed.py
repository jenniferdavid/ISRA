# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cob_srvs/GetPoseStampedTransformedRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class GetPoseStampedTransformedRequest(genpy.Message):
  _md5sum = "7f6050054c7441aa5c8e1b131c78c448"
  _type = "cob_srvs/GetPoseStampedTransformedRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """geometry_msgs/PoseStamped target
geometry_msgs/PoseStamped origin
geometry_msgs/Quaternion  orientation_override
string root_name
string tip_name

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['target','origin','orientation_override','root_name','tip_name']
  _slot_types = ['geometry_msgs/PoseStamped','geometry_msgs/PoseStamped','geometry_msgs/Quaternion','string','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       target,origin,orientation_override,root_name,tip_name

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetPoseStampedTransformedRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.target is None:
        self.target = geometry_msgs.msg.PoseStamped()
      if self.origin is None:
        self.origin = geometry_msgs.msg.PoseStamped()
      if self.orientation_override is None:
        self.orientation_override = geometry_msgs.msg.Quaternion()
      if self.root_name is None:
        self.root_name = ''
      if self.tip_name is None:
        self.tip_name = ''
    else:
      self.target = geometry_msgs.msg.PoseStamped()
      self.origin = geometry_msgs.msg.PoseStamped()
      self.orientation_override = geometry_msgs.msg.Quaternion()
      self.root_name = ''
      self.tip_name = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs))
      _x = self.target.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.target.pose.position.x, _x.target.pose.position.y, _x.target.pose.position.z, _x.target.pose.orientation.x, _x.target.pose.orientation.y, _x.target.pose.orientation.z, _x.target.pose.orientation.w, _x.origin.header.seq, _x.origin.header.stamp.secs, _x.origin.header.stamp.nsecs))
      _x = self.origin.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_11d().pack(_x.origin.pose.position.x, _x.origin.pose.position.y, _x.origin.pose.position.z, _x.origin.pose.orientation.x, _x.origin.pose.orientation.y, _x.origin.pose.orientation.z, _x.origin.pose.orientation.w, _x.orientation_override.x, _x.orientation_override.y, _x.orientation_override.z, _x.orientation_override.w))
      _x = self.root_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.tip_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.target is None:
        self.target = geometry_msgs.msg.PoseStamped()
      if self.origin is None:
        self.origin = geometry_msgs.msg.PoseStamped()
      if self.orientation_override is None:
        self.orientation_override = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.target.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.target.pose.position.x, _x.target.pose.position.y, _x.target.pose.position.z, _x.target.pose.orientation.x, _x.target.pose.orientation.y, _x.target.pose.orientation.z, _x.target.pose.orientation.w, _x.origin.header.seq, _x.origin.header.stamp.secs, _x.origin.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.origin.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.origin.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.origin.pose.position.x, _x.origin.pose.position.y, _x.origin.pose.position.z, _x.origin.pose.orientation.x, _x.origin.pose.orientation.y, _x.origin.pose.orientation.z, _x.origin.pose.orientation.w, _x.orientation_override.x, _x.orientation_override.y, _x.orientation_override.z, _x.orientation_override.w,) = _get_struct_11d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.root_name = str[start:end].decode('utf-8')
      else:
        self.root_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tip_name = str[start:end].decode('utf-8')
      else:
        self.tip_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs))
      _x = self.target.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d3I().pack(_x.target.pose.position.x, _x.target.pose.position.y, _x.target.pose.position.z, _x.target.pose.orientation.x, _x.target.pose.orientation.y, _x.target.pose.orientation.z, _x.target.pose.orientation.w, _x.origin.header.seq, _x.origin.header.stamp.secs, _x.origin.header.stamp.nsecs))
      _x = self.origin.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_11d().pack(_x.origin.pose.position.x, _x.origin.pose.position.y, _x.origin.pose.position.z, _x.origin.pose.orientation.x, _x.origin.pose.orientation.y, _x.origin.pose.orientation.z, _x.origin.pose.orientation.w, _x.orientation_override.x, _x.orientation_override.y, _x.orientation_override.z, _x.orientation_override.w))
      _x = self.root_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.tip_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.target is None:
        self.target = geometry_msgs.msg.PoseStamped()
      if self.origin is None:
        self.origin = geometry_msgs.msg.PoseStamped()
      if self.orientation_override is None:
        self.orientation_override = geometry_msgs.msg.Quaternion()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.target.header.seq, _x.target.header.stamp.secs, _x.target.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.target.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.target.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 68
      (_x.target.pose.position.x, _x.target.pose.position.y, _x.target.pose.position.z, _x.target.pose.orientation.x, _x.target.pose.orientation.y, _x.target.pose.orientation.z, _x.target.pose.orientation.w, _x.origin.header.seq, _x.origin.header.stamp.secs, _x.origin.header.stamp.nsecs,) = _get_struct_7d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.origin.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.origin.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 88
      (_x.origin.pose.position.x, _x.origin.pose.position.y, _x.origin.pose.position.z, _x.origin.pose.orientation.x, _x.origin.pose.orientation.y, _x.origin.pose.orientation.z, _x.origin.pose.orientation.w, _x.orientation_override.x, _x.orientation_override.y, _x.orientation_override.z, _x.orientation_override.w,) = _get_struct_11d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.root_name = str[start:end].decode('utf-8')
      else:
        self.root_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tip_name = str[start:end].decode('utf-8')
      else:
        self.tip_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_11d = None
def _get_struct_11d():
    global _struct_11d
    if _struct_11d is None:
        _struct_11d = struct.Struct("<11d")
    return _struct_11d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_7d3I = None
def _get_struct_7d3I():
    global _struct_7d3I
    if _struct_7d3I is None:
        _struct_7d3I = struct.Struct("<7d3I")
    return _struct_7d3I
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cob_srvs/GetPoseStampedTransformedResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class GetPoseStampedTransformedResponse(genpy.Message):
  _md5sum = "aa1ecfaaa2557395e49e336255c7a317"
  _type = "cob_srvs/GetPoseStampedTransformedResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success
geometry_msgs/PoseStamped result


================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
"""
  __slots__ = ['success','result']
  _slot_types = ['bool','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,result

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GetPoseStampedTransformedResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.result is None:
        self.result = geometry_msgs.msg.PoseStamped()
    else:
      self.success = False
      self.result = geometry_msgs.msg.PoseStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B3I().pack(_x.success, _x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs))
      _x = self.result.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.result.pose.position.x, _x.result.pose.position.y, _x.result.pose.position.z, _x.result.pose.orientation.x, _x.result.pose.orientation.y, _x.result.pose.orientation.z, _x.result.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.result is None:
        self.result = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.success, _x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.result.pose.position.x, _x.result.pose.position.y, _x.result.pose.position.z, _x.result.pose.orientation.x, _x.result.pose.orientation.y, _x.result.pose.orientation.z, _x.result.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B3I().pack(_x.success, _x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs))
      _x = self.result.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_7d().pack(_x.result.pose.position.x, _x.result.pose.position.y, _x.result.pose.position.z, _x.result.pose.orientation.x, _x.result.pose.orientation.y, _x.result.pose.orientation.z, _x.result.pose.orientation.w))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.result is None:
        self.result = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 13
      (_x.success, _x.result.header.seq, _x.result.header.stamp.secs, _x.result.header.stamp.nsecs,) = _get_struct_B3I().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.result.pose.position.x, _x.result.pose.position.y, _x.result.pose.position.z, _x.result.pose.orientation.x, _x.result.pose.orientation.y, _x.result.pose.orientation.z, _x.result.pose.orientation.w,) = _get_struct_7d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d = None
def _get_struct_7d():
    global _struct_7d
    if _struct_7d is None:
        _struct_7d = struct.Struct("<7d")
    return _struct_7d
_struct_B3I = None
def _get_struct_B3I():
    global _struct_B3I
    if _struct_B3I is None:
        _struct_B3I = struct.Struct("<B3I")
    return _struct_B3I
class GetPoseStampedTransformed(object):
  _type          = 'cob_srvs/GetPoseStampedTransformed'
  _md5sum = 'ed0069a0a6ce5102fc39c3328eef052f'
  _request_class  = GetPoseStampedTransformedRequest
  _response_class = GetPoseStampedTransformedResponse
