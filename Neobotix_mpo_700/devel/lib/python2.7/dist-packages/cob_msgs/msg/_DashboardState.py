# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from cob_msgs/DashboardState.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import cob_msgs.msg
import genpy
import std_msgs.msg

class DashboardState(genpy.Message):
  _md5sum = "db0cd0d535d75e0f6257b20c403e87f5"
  _type = "cob_msgs/DashboardState"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message communicates state information that might be used by a
# dashboard application.
std_msgs/Bool motors_halted
bool motors_halted_valid

cob_msgs/PowerBoardState power_board_state
bool power_board_state_valid

cob_msgs/PowerState power_state
bool power_state_valid

cob_msgs/AccessPoint access_point
bool access_point_valid

================================================================================
MSG: std_msgs/Bool
bool data
================================================================================
MSG: cob_msgs/PowerBoardState
# This message communicates the state of the PR2's power board.
int8 STATE_NOPOWER=0
int8 STATE_STANDBY=1
int8 STATE_PUMPING=2
int8 STATE_ON=3
int8 STATE_ENABLED=3  # Preferred over STATE_ON, keeping STATE_ON for backcompat
int8 STATE_DISABLED=4

int8 MASTER_NOPOWER=0
int8 MASTER_STANDBY=1
int8 MASTER_ON=2
int8 MASTER_OFF=3
int8 MASTER_SHUTDOWN=4

Header header
string name # Name with serial number
uint32 serial_num # Serial number for this board's message
float64 input_voltage # Input voltage to power board

# Master States:
#  MASTER_NOPOWER, MASTER_STANDBY, MASTER_ON, MASTER_OFF, MASTER_SHUTDOWN 
int8 master_state  # The master state machine's state in the powerboard

# Circuit States:
#  STATE_NOPOWER, STATE_STANDBY, STATE_PUMPING, STATE_ON, STATE_DISABLED
int8[3] circuit_state # One of the above states
float64[3] circuit_voltage  # Output voltage of each circuit

# True if robot should be enabled
bool run_stop           #Note - if the wireless run-stop is hit, this will be unobservable
bool wireless_stop 

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
MSG: cob_msgs/PowerState
# This message communicates the state of the PR2's power system.
Header header
float64 power_consumption ## Watts
duration time_remaining ## estimated time to empty or full
string prediction_method ## how time_remaining is being calculated
int8  relative_capacity ## percent of capacity
int8  AC_present ## number of packs detecting AC power, > 0 means plugged in

================================================================================
MSG: cob_msgs/AccessPoint
# This message communicates the state of the PR2's wifi access point.
Header header
string essid
string macaddr
int32 signal
int32 noise
int32 snr
int32 channel
string rate
string tx_power
int32 quality
"""
  __slots__ = ['motors_halted','motors_halted_valid','power_board_state','power_board_state_valid','power_state','power_state_valid','access_point','access_point_valid']
  _slot_types = ['std_msgs/Bool','bool','cob_msgs/PowerBoardState','bool','cob_msgs/PowerState','bool','cob_msgs/AccessPoint','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       motors_halted,motors_halted_valid,power_board_state,power_board_state_valid,power_state,power_state_valid,access_point,access_point_valid

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DashboardState, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.motors_halted is None:
        self.motors_halted = std_msgs.msg.Bool()
      if self.motors_halted_valid is None:
        self.motors_halted_valid = False
      if self.power_board_state is None:
        self.power_board_state = cob_msgs.msg.PowerBoardState()
      if self.power_board_state_valid is None:
        self.power_board_state_valid = False
      if self.power_state is None:
        self.power_state = cob_msgs.msg.PowerState()
      if self.power_state_valid is None:
        self.power_state_valid = False
      if self.access_point is None:
        self.access_point = cob_msgs.msg.AccessPoint()
      if self.access_point_valid is None:
        self.access_point_valid = False
    else:
      self.motors_halted = std_msgs.msg.Bool()
      self.motors_halted_valid = False
      self.power_board_state = cob_msgs.msg.PowerBoardState()
      self.power_board_state_valid = False
      self.power_state = cob_msgs.msg.PowerState()
      self.power_state_valid = False
      self.access_point = cob_msgs.msg.AccessPoint()
      self.access_point_valid = False

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
      buff.write(_get_struct_2B3I().pack(_x.motors_halted.data, _x.motors_halted_valid, _x.power_board_state.header.seq, _x.power_board_state.header.stamp.secs, _x.power_board_state.header.stamp.nsecs))
      _x = self.power_board_state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.power_board_state.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_Idb().pack(_x.power_board_state.serial_num, _x.power_board_state.input_voltage, _x.power_board_state.master_state))
      buff.write(_get_struct_3b().pack(*self.power_board_state.circuit_state))
      buff.write(_get_struct_3d().pack(*self.power_board_state.circuit_voltage))
      _x = self
      buff.write(_get_struct_3B3I().pack(_x.power_board_state.run_stop, _x.power_board_state.wireless_stop, _x.power_board_state_valid, _x.power_state.header.seq, _x.power_state.header.stamp.secs, _x.power_state.header.stamp.nsecs))
      _x = self.power_state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2i().pack(_x.power_state.power_consumption, _x.power_state.time_remaining.secs, _x.power_state.time_remaining.nsecs))
      _x = self.power_state.prediction_method
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2bB3I().pack(_x.power_state.relative_capacity, _x.power_state.AC_present, _x.power_state_valid, _x.access_point.header.seq, _x.access_point.header.stamp.secs, _x.access_point.header.stamp.nsecs))
      _x = self.access_point.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.access_point.essid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.access_point.macaddr
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4i().pack(_x.access_point.signal, _x.access_point.noise, _x.access_point.snr, _x.access_point.channel))
      _x = self.access_point.rate
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.access_point.tx_power
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_iB().pack(_x.access_point.quality, _x.access_point_valid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.motors_halted is None:
        self.motors_halted = std_msgs.msg.Bool()
      if self.power_board_state is None:
        self.power_board_state = cob_msgs.msg.PowerBoardState()
      if self.power_state is None:
        self.power_state = cob_msgs.msg.PowerState()
      if self.access_point is None:
        self.access_point = cob_msgs.msg.AccessPoint()
      end = 0
      _x = self
      start = end
      end += 14
      (_x.motors_halted.data, _x.motors_halted_valid, _x.power_board_state.header.seq, _x.power_board_state.header.stamp.secs, _x.power_board_state.header.stamp.nsecs,) = _get_struct_2B3I().unpack(str[start:end])
      self.motors_halted.data = bool(self.motors_halted.data)
      self.motors_halted_valid = bool(self.motors_halted_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_board_state.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.power_board_state.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_board_state.name = str[start:end].decode('utf-8')
      else:
        self.power_board_state.name = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.power_board_state.serial_num, _x.power_board_state.input_voltage, _x.power_board_state.master_state,) = _get_struct_Idb().unpack(str[start:end])
      start = end
      end += 3
      self.power_board_state.circuit_state = _get_struct_3b().unpack(str[start:end])
      start = end
      end += 24
      self.power_board_state.circuit_voltage = _get_struct_3d().unpack(str[start:end])
      _x = self
      start = end
      end += 15
      (_x.power_board_state.run_stop, _x.power_board_state.wireless_stop, _x.power_board_state_valid, _x.power_state.header.seq, _x.power_state.header.stamp.secs, _x.power_state.header.stamp.nsecs,) = _get_struct_3B3I().unpack(str[start:end])
      self.power_board_state.run_stop = bool(self.power_board_state.run_stop)
      self.power_board_state.wireless_stop = bool(self.power_board_state.wireless_stop)
      self.power_board_state_valid = bool(self.power_board_state_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_state.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.power_state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.power_state.power_consumption, _x.power_state.time_remaining.secs, _x.power_state.time_remaining.nsecs,) = _get_struct_d2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_state.prediction_method = str[start:end].decode('utf-8')
      else:
        self.power_state.prediction_method = str[start:end]
      _x = self
      start = end
      end += 15
      (_x.power_state.relative_capacity, _x.power_state.AC_present, _x.power_state_valid, _x.access_point.header.seq, _x.access_point.header.stamp.secs, _x.access_point.header.stamp.nsecs,) = _get_struct_2bB3I().unpack(str[start:end])
      self.power_state_valid = bool(self.power_state_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.access_point.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.essid = str[start:end].decode('utf-8')
      else:
        self.access_point.essid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.macaddr = str[start:end].decode('utf-8')
      else:
        self.access_point.macaddr = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.access_point.signal, _x.access_point.noise, _x.access_point.snr, _x.access_point.channel,) = _get_struct_4i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.rate = str[start:end].decode('utf-8')
      else:
        self.access_point.rate = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.tx_power = str[start:end].decode('utf-8')
      else:
        self.access_point.tx_power = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.access_point.quality, _x.access_point_valid,) = _get_struct_iB().unpack(str[start:end])
      self.access_point_valid = bool(self.access_point_valid)
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
      buff.write(_get_struct_2B3I().pack(_x.motors_halted.data, _x.motors_halted_valid, _x.power_board_state.header.seq, _x.power_board_state.header.stamp.secs, _x.power_board_state.header.stamp.nsecs))
      _x = self.power_board_state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.power_board_state.name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_Idb().pack(_x.power_board_state.serial_num, _x.power_board_state.input_voltage, _x.power_board_state.master_state))
      buff.write(self.power_board_state.circuit_state.tostring())
      buff.write(self.power_board_state.circuit_voltage.tostring())
      _x = self
      buff.write(_get_struct_3B3I().pack(_x.power_board_state.run_stop, _x.power_board_state.wireless_stop, _x.power_board_state_valid, _x.power_state.header.seq, _x.power_state.header.stamp.secs, _x.power_state.header.stamp.nsecs))
      _x = self.power_state.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_d2i().pack(_x.power_state.power_consumption, _x.power_state.time_remaining.secs, _x.power_state.time_remaining.nsecs))
      _x = self.power_state.prediction_method
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_2bB3I().pack(_x.power_state.relative_capacity, _x.power_state.AC_present, _x.power_state_valid, _x.access_point.header.seq, _x.access_point.header.stamp.secs, _x.access_point.header.stamp.nsecs))
      _x = self.access_point.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.access_point.essid
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.access_point.macaddr
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_4i().pack(_x.access_point.signal, _x.access_point.noise, _x.access_point.snr, _x.access_point.channel))
      _x = self.access_point.rate
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.access_point.tx_power
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_iB().pack(_x.access_point.quality, _x.access_point_valid))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.motors_halted is None:
        self.motors_halted = std_msgs.msg.Bool()
      if self.power_board_state is None:
        self.power_board_state = cob_msgs.msg.PowerBoardState()
      if self.power_state is None:
        self.power_state = cob_msgs.msg.PowerState()
      if self.access_point is None:
        self.access_point = cob_msgs.msg.AccessPoint()
      end = 0
      _x = self
      start = end
      end += 14
      (_x.motors_halted.data, _x.motors_halted_valid, _x.power_board_state.header.seq, _x.power_board_state.header.stamp.secs, _x.power_board_state.header.stamp.nsecs,) = _get_struct_2B3I().unpack(str[start:end])
      self.motors_halted.data = bool(self.motors_halted.data)
      self.motors_halted_valid = bool(self.motors_halted_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_board_state.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.power_board_state.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_board_state.name = str[start:end].decode('utf-8')
      else:
        self.power_board_state.name = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.power_board_state.serial_num, _x.power_board_state.input_voltage, _x.power_board_state.master_state,) = _get_struct_Idb().unpack(str[start:end])
      start = end
      end += 3
      self.power_board_state.circuit_state = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=3)
      start = end
      end += 24
      self.power_board_state.circuit_voltage = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=3)
      _x = self
      start = end
      end += 15
      (_x.power_board_state.run_stop, _x.power_board_state.wireless_stop, _x.power_board_state_valid, _x.power_state.header.seq, _x.power_state.header.stamp.secs, _x.power_state.header.stamp.nsecs,) = _get_struct_3B3I().unpack(str[start:end])
      self.power_board_state.run_stop = bool(self.power_board_state.run_stop)
      self.power_board_state.wireless_stop = bool(self.power_board_state.wireless_stop)
      self.power_board_state_valid = bool(self.power_board_state_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_state.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.power_state.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.power_state.power_consumption, _x.power_state.time_remaining.secs, _x.power_state.time_remaining.nsecs,) = _get_struct_d2i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.power_state.prediction_method = str[start:end].decode('utf-8')
      else:
        self.power_state.prediction_method = str[start:end]
      _x = self
      start = end
      end += 15
      (_x.power_state.relative_capacity, _x.power_state.AC_present, _x.power_state_valid, _x.access_point.header.seq, _x.access_point.header.stamp.secs, _x.access_point.header.stamp.nsecs,) = _get_struct_2bB3I().unpack(str[start:end])
      self.power_state_valid = bool(self.power_state_valid)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.access_point.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.essid = str[start:end].decode('utf-8')
      else:
        self.access_point.essid = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.macaddr = str[start:end].decode('utf-8')
      else:
        self.access_point.macaddr = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.access_point.signal, _x.access_point.noise, _x.access_point.snr, _x.access_point.channel,) = _get_struct_4i().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.rate = str[start:end].decode('utf-8')
      else:
        self.access_point.rate = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.access_point.tx_power = str[start:end].decode('utf-8')
      else:
        self.access_point.tx_power = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.access_point.quality, _x.access_point_valid,) = _get_struct_iB().unpack(str[start:end])
      self.access_point_valid = bool(self.access_point_valid)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2B3I = None
def _get_struct_2B3I():
    global _struct_2B3I
    if _struct_2B3I is None:
        _struct_2B3I = struct.Struct("<2B3I")
    return _struct_2B3I
_struct_4i = None
def _get_struct_4i():
    global _struct_4i
    if _struct_4i is None:
        _struct_4i = struct.Struct("<4i")
    return _struct_4i
_struct_3B3I = None
def _get_struct_3B3I():
    global _struct_3B3I
    if _struct_3B3I is None:
        _struct_3B3I = struct.Struct("<3B3I")
    return _struct_3B3I
_struct_d2i = None
def _get_struct_d2i():
    global _struct_d2i
    if _struct_d2i is None:
        _struct_d2i = struct.Struct("<d2i")
    return _struct_d2i
_struct_2bB3I = None
def _get_struct_2bB3I():
    global _struct_2bB3I
    if _struct_2bB3I is None:
        _struct_2bB3I = struct.Struct("<2bB3I")
    return _struct_2bB3I
_struct_3b = None
def _get_struct_3b():
    global _struct_3b
    if _struct_3b is None:
        _struct_3b = struct.Struct("<3b")
    return _struct_3b
_struct_iB = None
def _get_struct_iB():
    global _struct_iB
    if _struct_iB is None:
        _struct_iB = struct.Struct("<iB")
    return _struct_iB
_struct_Idb = None
def _get_struct_Idb():
    global _struct_Idb
    if _struct_Idb is None:
        _struct_Idb = struct.Struct("<Idb")
    return _struct_Idb
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d