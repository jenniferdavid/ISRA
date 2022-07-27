// Generated by gencpp from file cob_srvs/SetJointTrajectoryResponse.msg
// DO NOT EDIT!


#ifndef COB_SRVS_MESSAGE_SETJOINTTRAJECTORYRESPONSE_H
#define COB_SRVS_MESSAGE_SETJOINTTRAJECTORYRESPONSE_H


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
struct SetJointTrajectoryResponse_
{
  typedef SetJointTrajectoryResponse_<ContainerAllocator> Type;

  SetJointTrajectoryResponse_()
    : success(0)
    , errorMessage()  {
    }
  SetJointTrajectoryResponse_(const ContainerAllocator& _alloc)
    : success(0)
    , errorMessage(_alloc)  {
  (void)_alloc;
    }



   typedef int64_t _success_type;
  _success_type success;

   typedef  ::std_msgs::String_<ContainerAllocator>  _errorMessage_type;
  _errorMessage_type errorMessage;





  typedef boost::shared_ptr< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SetJointTrajectoryResponse_

typedef ::cob_srvs::SetJointTrajectoryResponse_<std::allocator<void> > SetJointTrajectoryResponse;

typedef boost::shared_ptr< ::cob_srvs::SetJointTrajectoryResponse > SetJointTrajectoryResponsePtr;
typedef boost::shared_ptr< ::cob_srvs::SetJointTrajectoryResponse const> SetJointTrajectoryResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "fff2fd61c570b3016de5f27e6dc433be";
  }

  static const char* value(const ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xfff2fd61c570b301ULL;
  static const uint64_t static_value2 = 0x6de5f27e6dc433beULL;
};

template<class ContainerAllocator>
struct DataType< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cob_srvs/SetJointTrajectoryResponse";
  }

  static const char* value(const ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 success\n"
"std_msgs/String errorMessage\n"
"\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/String\n"
"string data\n"
;
  }

  static const char* value(const ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.errorMessage);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetJointTrajectoryResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cob_srvs::SetJointTrajectoryResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<int64_t>::stream(s, indent + "  ", v.success);
    s << indent << "errorMessage: ";
    s << std::endl;
    Printer< ::std_msgs::String_<ContainerAllocator> >::stream(s, indent + "  ", v.errorMessage);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COB_SRVS_MESSAGE_SETJOINTTRAJECTORYRESPONSE_H