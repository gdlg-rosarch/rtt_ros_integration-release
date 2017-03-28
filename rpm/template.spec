Name:           ros-jade-rtt-ros
Version:        2.8.5
Release:        0%{?dist}
Summary:        ROS rtt_ros package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rtt_ros_integration
Source0:        %{name}-%{version}.tar.gz

Requires:       libxml2-devel
Requires:       ros-jade-ocl
Requires:       ros-jade-roslib
Requires:       ros-jade-rospack
Requires:       ros-jade-rostime
Requires:       ros-jade-rtt
BuildRequires:  libxml2-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-ocl
BuildRequires:  ros-jade-roslib
BuildRequires:  ros-jade-rospack
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-rtt

%description
This package provides an RTT plugin to add a ROS node to the RTT process, as
well as several wrapper scripts to enable roslaunching of orocos programs.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Mar 28 2017 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.5-0
- Autogenerated by Bloom

* Sat Nov 26 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.4-1
- Autogenerated by Bloom

* Sat Nov 26 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.4-0
- Autogenerated by Bloom

* Wed Jul 20 2016 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.3-0
- Autogenerated by Bloom

* Fri Jul 24 2015 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.8.2-0
- Autogenerated by Bloom

