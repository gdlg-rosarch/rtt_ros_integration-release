# Script generated with Bloom
pkgdesc="ROS - This package provides an RTT plugin to add a ROS node to the RTT process, as well as several wrapper scripts to enable roslaunching of orocos programs."
url='http://ros.org/wiki/rtt_ros_integration'

pkgname='ros-kinetic-rtt-ros'
pkgver='2.9.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libxml2'
'ros-kinetic-catkin'
'ros-kinetic-ocl'
'ros-kinetic-roslib'
'ros-kinetic-rospack'
'ros-kinetic-rostime'
'ros-kinetic-rtt'
)

depends=('libxml2'
'ros-kinetic-ocl'
'ros-kinetic-roslib'
'ros-kinetic-rospack'
'ros-kinetic-rostime'
'ros-kinetic-rtt'
)

conflicts=()
replaces=()

_dir=rtt_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtt_ros $srcdir/rtt_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

