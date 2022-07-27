// Generated by gencpp from file neo_srvs/RelayBoardSetLCDMsgResponse.msg
// DO NOT EDIT!


#ifndef NEO_SRVS_MESSAGE_RELAYBOARDSETLCDMSGRESPONSE_H
#define NEO_SRVS_MESSAGE_RELAYBOARDSETLCDMSGRESPONSE_H


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
struct RelayBoardSetLCDMsgResponse_
{
  typedef RelayBoardSetLCDMsgResponse_<ContainerAllocator> Type;

  RelayBoardSetLCDMsgResponse_()
    : success(false)  {
    }
  RelayBoardSetLCDMsgResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RelayBoardSetLCDMsgResponse_

typedef ::neo_srvs::RelayBoardSetLCDMsgResponse_<std::allocator<void> > RelayBoardSetLCDMsgResponse;

typedef boost::shared_ptr< ::neo_srvs::RelayBoardSetLCDMsgResponse > RelayBoardSetLCDMsgResponsePtr;
typedef boost::shared_ptr< ::neo_srvs::RelayBoardSetLCDMsgResponse const> RelayBoardSetLCDMsgResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "neo_srvs/RelayBoardSetLCDMsgResponse";
  }

  static const char* value(const ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"\n"
;
  }

  static const char* value(const ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RelayBoardSetLCDMsgResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::neo_srvs::RelayBoardSetLCDMsgResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // NEO_SRVS_MESSAGE_RELAYBOARDSETLCDMSGRESPONSE_H
