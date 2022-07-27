
(cl:in-package :asdf)

(defsystem "cob_srvs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
               :trajectory_msgs-msg
)
  :components ((:file "_package")
    (:file "GetPoseStampedTransformed" :depends-on ("_package_GetPoseStampedTransformed"))
    (:file "_package_GetPoseStampedTransformed" :depends-on ("_package"))
    (:file "SetDefaultVel" :depends-on ("_package_SetDefaultVel"))
    (:file "_package_SetDefaultVel" :depends-on ("_package"))
    (:file "SetFloat" :depends-on ("_package_SetFloat"))
    (:file "_package_SetFloat" :depends-on ("_package"))
    (:file "SetInt" :depends-on ("_package_SetInt"))
    (:file "_package_SetInt" :depends-on ("_package"))
    (:file "SetJointStiffness" :depends-on ("_package_SetJointStiffness"))
    (:file "_package_SetJointStiffness" :depends-on ("_package"))
    (:file "SetJointTrajectory" :depends-on ("_package_SetJointTrajectory"))
    (:file "_package_SetJointTrajectory" :depends-on ("_package"))
    (:file "SetMaxVel" :depends-on ("_package_SetMaxVel"))
    (:file "_package_SetMaxVel" :depends-on ("_package"))
    (:file "SetOperationMode" :depends-on ("_package_SetOperationMode"))
    (:file "_package_SetOperationMode" :depends-on ("_package"))
    (:file "SetString" :depends-on ("_package_SetString"))
    (:file "_package_SetString" :depends-on ("_package"))
    (:file "Trigger" :depends-on ("_package_Trigger"))
    (:file "_package_Trigger" :depends-on ("_package"))
  ))