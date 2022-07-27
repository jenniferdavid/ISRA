// Generated by gencpp from file cob_srvs/SetOperationModeRequest.msg
// DO NOT EDIT!


#ifndef COB_SRVS_MESSAGE_SETOPERATIONMODEREQUEST_H
#define COB_SRVS_MESSAGE_SETOPERATIONMODEREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/String.h>

namespace cob_srvs
{
template <class ContainerAllocator>
struct SetOperationModeRequest_
{
  typedef SetOperationModeRequest_<ContainerAllocator> Type;

  SetOperationModeRequest_()
    : operation_mode()  {
    }
  SetOperationModeRequest_(const ContainerAllocator& _alloc)
    : operation_mode(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::String_<ContainerAllocator>  _operation_mode_type;
  _operation_mode_type operation_mode;





  typedef boost::shared_ptr< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetOperationModeRequest_

typedef ::cob_srvs::SetOperationModeRequest_<std::allocator<void> > SetOperationModeRequest;

typedef boost::shared_ptr< ::cob_srvs::SetOperationModeRequest > SetOperationModeRequestPtr;
typedef boost::shared_ptr< ::cob_srvs::SetOperationModeRequest const> SetOperationModeRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace cob_srvs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/melodic/share/trajectory_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/melodic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "df954cef597fce5b749fee53c7846c40";
  }

  static const char* value(const ::cob_srvs::SetOperationModeRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xdf954cef597fce5bULL;
  static const uint64_t static_value2 = 0x749fee53c7846c40ULL;
};

template<class ContainerAllocator>
struct DataType< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cob_srvs/SetOperationModeRequest";
  }

  static const char* value(const ::cob_srvs::SetOperationModeRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/String operation_mode\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/String\n"
"string data\n"
;
  }

  static const char* value(const ::cob_srvs::SetOperationModeRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.operation_mode);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetOperationModeRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cob_srvs::SetOperationModeRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cob_srvs::SetOperationModeRequest_<ContainerAllocator>& v)
  {
    s << indent << "operation_mode: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.operation_mode);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COB_SRVS_MESSAGE_SETOPERATIONMODEREQUEST_H
