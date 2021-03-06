// Generated by gencpp from file cob_msgs/BatteryState.msg
// DO NOT EDIT!


#ifndef COB_MSGS_MESSAGE_BATTERYSTATE_H
#define COB_MSGS_MESSAGE_BATTERYSTATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cob_msgs
{
template <class ContainerAllocator>
struct BatteryState_
{
  typedef BatteryState_<ContainerAllocator> Type;

  BatteryState_()
    : lastTimeBattery(0)
    , batReg()
    , batRegFlag()
    , batRegTime()  {
      batReg.assign(0);

      batRegFlag.assign(0);

      batRegTime.assign(0);
  }
  BatteryState_(const ContainerAllocator& _alloc)
    : lastTimeBattery(0)
    , batReg()
    , batRegFlag()
    , batRegTime()  {
  (void)_alloc;
      batReg.assign(0);

      batRegFlag.assign(0);

      batRegTime.assign(0);
  }



   typedef int32_t _lastTimeBattery_type;
  _lastTimeBattery_type lastTimeBattery;

   typedef boost::array<uint16_t, 48>  _batReg_type;
  _batReg_type batReg;

   typedef boost::array<uint16_t, 48>  _batRegFlag_type;
  _batRegFlag_type batRegFlag;

   typedef boost::array<int32_t, 48>  _batRegTime_type;
  _batRegTime_type batRegTime;





  typedef boost::shared_ptr< ::cob_msgs::BatteryState_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cob_msgs::BatteryState_<ContainerAllocator> const> ConstPtr;

}; // struct BatteryState_

typedef ::cob_msgs::BatteryState_<std::allocator<void> > BatteryState;

typedef boost::shared_ptr< ::cob_msgs::BatteryState > BatteryStatePtr;
typedef boost::shared_ptr< ::cob_msgs::BatteryState const> BatteryStateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cob_msgs::BatteryState_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cob_msgs::BatteryState_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cob_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'cob_msgs': ['/home/yusseff/Neobotix/src/cob_common/cob_msgs/msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cob_msgs::BatteryState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cob_msgs::BatteryState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_msgs::BatteryState_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_msgs::BatteryState_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_msgs::BatteryState_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_msgs::BatteryState_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cob_msgs::BatteryState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "00e9f996c2fc26700fd25abcd8422db0";
  }

  static const char* value(const ::cob_msgs::BatteryState_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x00e9f996c2fc2670ULL;
  static const uint64_t static_value2 = 0x0fd25abcd8422db0ULL;
};

template<class ContainerAllocator>
struct DataType< ::cob_msgs::BatteryState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cob_msgs/BatteryState";
  }

  static const char* value(const ::cob_msgs::BatteryState_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cob_msgs::BatteryState_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# DEPRECATED.  Use cob_msgs/BatteryState2 instead.\n"
"# Each batteries registers\n"
"int32 lastTimeBattery #epoch time\n"
"uint16[48] batReg\n"
"uint16[48] batRegFlag\n"
"int32[48] batRegTime\n"
;
  }

  static const char* value(const ::cob_msgs::BatteryState_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cob_msgs::BatteryState_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.lastTimeBattery);
      stream.next(m.batReg);
      stream.next(m.batRegFlag);
      stream.next(m.batRegTime);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct BatteryState_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cob_msgs::BatteryState_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cob_msgs::BatteryState_<ContainerAllocator>& v)
  {
    s << indent << "lastTimeBattery: ";
    Printer<int32_t>::stream(s, indent + "  ", v.lastTimeBattery);
    s << indent << "batReg[]" << std::endl;
    for (size_t i = 0; i < v.batReg.size(); ++i)
    {
      s << indent << "  batReg[" << i << "]: ";
      Printer<uint16_t>::stream(s, indent + "  ", v.batReg[i]);
    }
    s << indent << "batRegFlag[]" << std::endl;
    for (size_t i = 0; i < v.batRegFlag.size(); ++i)
    {
      s << indent << "  batRegFlag[" << i << "]: ";
      Printer<uint16_t>::stream(s, indent + "  ", v.batRegFlag[i]);
    }
    s << indent << "batRegTime[]" << std::endl;
    for (size_t i = 0; i < v.batRegTime.size(); ++i)
    {
      s << indent << "  batRegTime[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.batRegTime[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // COB_MSGS_MESSAGE_BATTERYSTATE_H
