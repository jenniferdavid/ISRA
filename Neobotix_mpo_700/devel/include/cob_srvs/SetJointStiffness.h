// Generated by gencpp from file cob_srvs/SetJointStiffness.msg
// DO NOT EDIT!


#ifndef COB_SRVS_MESSAGE_SETJOINTSTIFFNESS_H
#define COB_SRVS_MESSAGE_SETJOINTSTIFFNESS_H

#include <ros/service_traits.h>


#include <cob_srvs/SetJointStiffnessRequest.h>
#include <cob_srvs/SetJointStiffnessResponse.h>


namespace cob_srvs
{

struct SetJointStiffness
{

typedef SetJointStiffnessRequest Request;
typedef SetJointStiffnessResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetJointStiffness
} // namespace cob_srvs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::cob_srvs::SetJointStiffness > {
  static const char* value()
  {
    return "2ae9ddd5d3294ccf3c876d966e4e11a3";
  }

  static const char* value(const ::cob_srvs::SetJointStiffness&) { return value(); }
};

template<>
struct DataType< ::cob_srvs::SetJointStiffness > {
  static const char* value()
  {
    return "cob_srvs/SetJointStiffness";
  }

  static const char* value(const ::cob_srvs::SetJointStiffness&) { return value(); }
};


// service_traits::MD5Sum< ::cob_srvs::SetJointStiffnessRequest> should match 
// service_traits::MD5Sum< ::cob_srvs::SetJointStiffness > 
template<>
struct MD5Sum< ::cob_srvs::SetJointStiffnessRequest>
{
  static const char* value()
  {
    return MD5Sum< ::cob_srvs::SetJointStiffness >::value();
  }
  static const char* value(const ::cob_srvs::SetJointStiffnessRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::cob_srvs::SetJointStiffnessRequest> should match 
// service_traits::DataType< ::cob_srvs::SetJointStiffness > 
template<>
struct DataType< ::cob_srvs::SetJointStiffnessRequest>
{
  static const char* value()
  {
    return DataType< ::cob_srvs::SetJointStiffness >::value();
  }
  static const char* value(const ::cob_srvs::SetJointStiffnessRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::cob_srvs::SetJointStiffnessResponse> should match 
// service_traits::MD5Sum< ::cob_srvs::SetJointStiffness > 
template<>
struct MD5Sum< ::cob_srvs::SetJointStiffnessResponse>
{
  static const char* value()
  {
    return MD5Sum< ::cob_srvs::SetJointStiffness >::value();
  }
  static const char* value(const ::cob_srvs::SetJointStiffnessResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::cob_srvs::SetJointStiffnessResponse> should match 
// service_traits::DataType< ::cob_srvs::SetJointStiffness > 
template<>
struct DataType< ::cob_srvs::SetJointStiffnessResponse>
{
  static const char* value()
  {
    return DataType< ::cob_srvs::SetJointStiffness >::value();
  }
  static const char* value(const ::cob_srvs::SetJointStiffnessResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // COB_SRVS_MESSAGE_SETJOINTSTIFFNESS_H