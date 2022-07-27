// Generated by gencpp from file cob_srvs/SetJointStiffnessRequest.msg
// DO NOT EDIT!


#ifndef COB_SRVS_MESSAGE_SETJOINTSTIFFNESSREQUEST_H
#define COB_SRVS_MESSAGE_SETJOINTSTIFFNESSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace cob_srvs
{
template <class ContainerAllocator>
struct SetJointStiffnessRequest_
{
  typedef SetJointStiffnessRequest_<ContainerAllocator> Type;

  SetJointStiffnessRequest_()
    : joint_stiffness()  {
    }
  SetJointStiffnessRequest_(const ContainerAllocator& _alloc)
    : joint_stiffness(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _joint_stiffness_type;
  _joint_stiffness_type joint_stiffness;





  typedef boost::shared_ptr< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetJointStiffnessRequest_

typedef ::cob_srvs::SetJointStiffnessRequest_<std::allocator<void> > SetJointStiffnessRequest;

typedef boost::shared_ptr< ::cob_srvs::SetJointStiffnessRequest > SetJointStiffnessRequestPtr;
typedef boost::shared_ptr< ::cob_srvs::SetJointStiffnessRequest const> SetJointStiffnessRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3f30c4d99702f028fe1bef65668a3d21";
  }

  static const char* value(const ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3f30c4d99702f028ULL;
  static const uint64_t static_value2 = 0xfe1bef65668a3d21ULL;
};

template<class ContainerAllocator>
struct DataType< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "cob_srvs/SetJointStiffnessRequest";
  }

  static const char* value(const ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32[] joint_stiffness\n"
;
  }

  static const char* value(const ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joint_stiffness);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetJointStiffnessRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::cob_srvs::SetJointStiffnessRequest_<ContainerAllocator>& v)
  {
    s << indent << "joint_stiffness[]" << std::endl;
    for (size_t i = 0; i < v.joint_stiffness.size(); ++i)
    {
      s << indent << "  joint_stiffness[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.joint_stiffness[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // COB_SRVS_MESSAGE_SETJOINTSTIFFNESSREQUEST_H
