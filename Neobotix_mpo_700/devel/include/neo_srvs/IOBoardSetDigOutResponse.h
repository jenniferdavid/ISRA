// Generated by gencpp from file neo_srvs/IOBoardSetDigOutResponse.msg
// DO NOT EDIT!


#ifndef NEO_SRVS_MESSAGE_IOBOARDSETDIGOUTRESPONSE_H
#define NEO_SRVS_MESSAGE_IOBOARDSETDIGOUTRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace neo_srvs
{
template <class ContainerAllocator>
struct IOBoardSetDigOutResponse_
{
  typedef IOBoardSetDigOutResponse_<ContainerAllocator> Type;

  IOBoardSetDigOutResponse_()
    : success(false)  {
    }
  IOBoardSetDigOutResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> const> ConstPtr;

}; // struct IOBoardSetDigOutResponse_

typedef ::neo_srvs::IOBoardSetDigOutResponse_<std::allocator<void> > IOBoardSetDigOutResponse;

typedef boost::shared_ptr< ::neo_srvs::IOBoardSetDigOutResponse > IOBoardSetDigOutResponsePtr;
typedef boost::shared_ptr< ::neo_srvs::IOBoardSetDigOutResponse const> IOBoardSetDigOutResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace neo_srvs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "neo_srvs/IOBoardSetDigOutResponse";
  }

  static const char* value(const ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"\n"
;
  }

  static const char* value(const ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct IOBoardSetDigOutResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::neo_srvs::IOBoardSetDigOutResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NEO_SRVS_MESSAGE_IOBOARDSETDIGOUTRESPONSE_H
