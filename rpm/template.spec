Name:           ros-kinetic-rtt-actionlib-msgs
Version:        2.9.0
Release:        0%{?dist}
Summary:        ROS rtt_actionlib_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-actionlib-msgs
Requires:       ros-kinetic-rtt-roscomm
Requires:       ros-kinetic-rtt-std-msgs
BuildRequires:  ros-kinetic-actionlib-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rtt-roscomm
BuildRequires:  ros-kinetic-rtt-std-msgs

%description
Provides an rtt typekit for ROS actionlib_msgs messages. It allows you to use
ROS messages transparently in RTT components and applications. This package was
automatically generated by the create_rtt_msgs generator and should not be
manually modified. See the http://ros.org/wiki/actionlib_msgs documentation for
the documentation of the ROS messages in this typekit.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Tue May 02 2017 Orocos Developers <orocos-dev@lists.mech.kuleuven.be> - 2.9.0-0
- Autogenerated by Bloom

