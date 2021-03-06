// Generated by gencpp from file cob_srvs/GetPoseStampedTransformedResponse.msg
// DO NOT EDIT!


#ifndef COB_SRVS_MESSAGE_GETPOSESTAMPEDTRANSFORMEDRESPONSE_H
#define COB_SRVS_MESSAGE_GETPOSESTAMPEDTRANSFORMEDRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/PoseStamped.h>

namespace cob_srvs
{
template <class ContainerAllocator>
struct GetPoseStampedTransformedResponse_
{
  typedef GetPoseStampedTransformedResponse_<ContainerAllocator> Type;

  GetPoseStampedTransformedResponse_()
    : success(false)
    , result()  {
    }
  GetPoseStampedTransformedResponse_(const ContainerAllocator& _alloc)
    : success(false)
    , result(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;

   typedef  ::geometry_msgs::PoseStamped_<ContainerAllocator>  _result_type;
  _result_type result;





  typedef boost::shared_ptr< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetPoseStampedTransformedResponse_

typedef ::cob_srvs::GetPoseStampedTransformedResponse_<std::allocator<void> > GetPoseStampedTransformedResponse;

typedef boost::shared_ptr< ::cob_srvs::GetPoseStampedTransformedResponse > GetPoseStampedTransformedResponsePtr;
typedef boost::shared_ptr< ::cob_srvs::GetPoseStampedTransformedResponse const> GetPoseStampedTransformedResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "aa1ecfaaa2557395e49e336255c7a317";
  }

  static const char* value(const ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xaa1ecfaaa2557395ULL;
  static const uint64_t static_value2 = 0xe49e336255c7a317ULL;
};

template<class ContainerAllocator>
struct DataType< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cob_srvs/GetPoseStampedTransformedResponse";
  }

  static const char* value(const ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"geometry_msgs/PoseStamped result\n"
"\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PoseStamped\n"
"# A Pose with reference coordinate frame and timestamp\n"
"Header header\n"
"Pose pose\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetPoseStampedTransformedResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cob_srvs::GetPoseStampedTransformedResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "result: ";
    s << std::endl;
    Printer< ::geometry_msgs::PoseStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // COB_SRVS_MESSAGE_GETPOSESTAMPEDTRANSFORMEDRESPONSE_H
