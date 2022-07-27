# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cob_msgs/BatteryServer2.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cob_msgs.msg
import genpy
import std_msgs.msg

class BatteryServer2(genpy.Message):
  _md5sum = "5f2cec7d06c312d756189db96c1f3819"
  _type = "cob_msgs/BatteryServer2"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This message communicates the state of a battery server, which controls
# multiple batteries.
Header header
int32 MAX_BAT_COUNT=4
int32 MAX_BAT_REG=48
int32 id  # unique ID for each battery server
# Battery System Stats
time last_system_update  # last time the system stats where updated
duration time_left       # in seconds (hardware resolution is 1 minute)
int32 average_charge     # in percent
string message           # message from the ocean server
time last_controller_update # last time a battery status flag was updated
# for each battery
cob_msgs/BatteryState2[] battery

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
MSG: cob_msgs/BatteryState2
# This message communicates the state of a single battery.
# Battery Controller Flags, one per battery
bool present       # is this pack present
bool charging      # is this pack charging
bool discharging   # is this pack discharging
bool power_present # is there an input voltage
bool power_no_good # is there a fault (No Good)
bool inhibited     # is this pack disabled for some reason
# These registers are per battery
time      last_battery_update     # last time any battery update occurred
int16[48] battery_register        # value of this register in the battery
bool[48]  battery_update_flag     # Has this register ever been updated
time[48]  battery_register_update # last time this specific register was updated
"""
  # Pseudo-constants
  MAX_BAT_COUNT = 4
  MAX_BAT_REG = 48

  __slots__ = ['header','id','last_system_update','time_left','average_charge','message','last_controller_update','battery']
  _slot_types = ['std_msgs/Header','int32','time','duration','int32','string','time','cob_msgs/BatteryState2[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,id,last_system_update,time_left,average_charge,message,last_controller_update,battery

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(BatteryServer2, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.id is None:
        self.id = 0
      if self.last_system_update is None:
        self.last_system_update = genpy.Time()
      if self.time_left is None:
        self.time_left = genpy.Duration()
      if self.average_charge is None:
        self.average_charge = 0
      if self.message is None:
        self.message = ''
      if self.last_controller_update is None:
        self.last_controller_update = genpy.Time()
      if self.battery is None:
        self.battery = []
    else:
      self.header = std_msgs.msg.Header()
      self.id = 0
      self.last_system_update = genpy.Time()
      self.time_left = genpy.Duration()
      self.average_charge = 0
      self.message = ''
      self.last_controller_update = genpy.Time()
      self.battery = []

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_i2I3i().pack(_x.id, _x.last_system_update.secs, _x.last_system_update.nsecs, _x.time_left.secs, _x.time_left.nsecs, _x.average_charge))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.last_controller_update.secs, _x.last_controller_update.nsecs))
      length = len(self.battery)
      buff.write(_struct_I.pack(length))
      for val1 in self.battery:
        _x = val1
        buff.write(_get_struct_6B().pack(_x.present, _x.charging, _x.discharging, _x.power_present, _x.power_no_good, _x.inhibited))
        _v1 = val1.last_battery_update
        _x = _v1
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        buff.write(_get_struct_48h().pack(*val1.battery_register))
        buff.write(_get_struct_48B().pack(*val1.battery_update_flag))
        if len(val1.battery_register_update) != 48:
          self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (48, len(val1.battery_register_update), 'val1.battery_register_update')))
        for val2 in val1.battery_register_update:
          _x = val2
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.last_system_update is None:
        self.last_system_update = genpy.Time()
      if self.time_left is None:
        self.time_left = genpy.Duration()
      if self.last_controller_update is None:
        self.last_controller_update = genpy.Time()
      if self.battery is None:
        self.battery = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.id, _x.last_system_update.secs, _x.last_system_update.nsecs, _x.time_left.secs, _x.time_left.nsecs, _x.average_charge,) = _get_struct_i2I3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8')
      else:
        self.message = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.last_controller_update.secs, _x.last_controller_update.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.battery = []
      for i in range(0, length):
        val1 = cob_msgs.msg.BatteryState2()
        _x = val1
        start = end
        end += 6
        (_x.present, _x.charging, _x.discharging, _x.power_present, _x.power_no_good, _x.inhibited,) = _get_struct_6B().unpack(str[start:end])
        val1.present = bool(val1.present)
        val1.charging = bool(val1.charging)
        val1.discharging = bool(val1.discharging)
        val1.power_present = bool(val1.power_present)
        val1.power_no_good = bool(val1.power_no_good)
        val1.inhibited = bool(val1.inhibited)
        _v2 = val1.last_battery_update
        _x = _v2
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 96
        val1.battery_register = _get_struct_48h().unpack(str[start:end])
        start = end
        end += 48
        val1.battery_update_flag = _get_struct_48B().unpack(str[start:end])
        val1.battery_update_flag = map(bool, val1.battery_update_flag)
        val1.battery_register_update = []
        for i in range(0, 48):
          val2 = genpy.Time()
          _x = val2
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          val1.battery_register_update.append(val2)
        self.battery.append(val1)
      self.last_system_update.canon()
      self.time_left.canon()
      self.last_controller_update.canon()
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_i2I3i().pack(_x.id, _x.last_system_update.secs, _x.last_system_update.nsecs, _x.time_left.secs, _x.time_left.nsecs, _x.average_charge))
      _x = self.message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.last_controller_update.secs, _x.last_controller_update.nsecs))
      length = len(self.battery)
      buff.write(_struct_I.pack(length))
      for val1 in self.battery:
        _x = val1
        buff.write(_get_struct_6B().pack(_x.present, _x.charging, _x.discharging, _x.power_present, _x.power_no_good, _x.inhibited))
        _v3 = val1.last_battery_update
        _x = _v3
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        buff.write(val1.battery_register.tostring())
        buff.write(val1.battery_update_flag.tostring())
        if len(val1.battery_register_update) != 48:
          self._check_types(ValueError("Expecting %s items but found %s when writing '%s'" % (48, len(val1.battery_register_update), 'val1.battery_register_update')))
        for val2 in val1.battery_register_update:
          _x = val2
          buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.last_system_update is None:
        self.last_system_update = genpy.Time()
      if self.time_left is None:
        self.time_left = genpy.Duration()
      if self.last_controller_update is None:
        self.last_controller_update = genpy.Time()
      if self.battery is None:
        self.battery = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.id, _x.last_system_update.secs, _x.last_system_update.nsecs, _x.time_left.secs, _x.time_left.nsecs, _x.average_charge,) = _get_struct_i2I3i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.message = str[start:end].decode('utf-8')
      else:
        self.message = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.last_controller_update.secs, _x.last_controller_update.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.battery = []
      for i in range(0, length):
        val1 = cob_msgs.msg.BatteryState2()
        _x = val1
        start = end
        end += 6
        (_x.present, _x.charging, _x.discharging, _x.power_present, _x.power_no_good, _x.inhibited,) = _get_struct_6B().unpack(str[start:end])
        val1.present = bool(val1.present)
        val1.charging = bool(val1.charging)
        val1.discharging = bool(val1.discharging)
        val1.power_present = bool(val1.power_present)
        val1.power_no_good = bool(val1.power_no_good)
        val1.inhibited = bool(val1.inhibited)
        _v4 = val1.last_battery_update
        _x = _v4
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 96
        val1.battery_register = numpy.frombuffer(str[start:end], dtype=numpy.int16, count=48)
        start = end
        end += 48
        val1.battery_update_flag = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=48)
        val1.battery_update_flag = map(bool, val1.battery_update_flag)
        val1.battery_register_update = []
        for i in range(0, 48):
          val2 = genpy.Time()
          _x = val2
          start = end
          end += 8
          (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
          val1.battery_register_update.append(val2)
        self.battery.append(val1)
      self.last_system_update.canon()
      self.time_left.canon()
      self.last_controller_update.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6B = None
def _get_struct_6B():
    global _struct_6B
    if _struct_6B is None:
        _struct_6B = struct.Struct("<6B")
    return _struct_6B
_struct_i2I3i = None
def _get_struct_i2I3i():
    global _struct_i2I3i
    if _struct_i2I3i is None:
        _struct_i2I3i = struct.Struct("<i2I3i")
    return _struct_i2I3i
_struct_48h = None
def _get_struct_48h():
    global _struct_48h
    if _struct_48h is None:
        _struct_48h = struct.Struct("<48h")
    return _struct_48h
_struct_48B = None
def _get_struct_48B():
    global _struct_48B
    if _struct_48B is None:
        _struct_48B = struct.Struct("<48B")
    return _struct_48B
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
