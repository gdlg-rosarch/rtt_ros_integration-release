# Script generated with Bloom
pkgdesc="ROS - Provides an rtt typekit for ROS sensor_msgs messages. It allows you to use ROS messages transparently in RTT components and applications. This package was automatically generated by the create_rtt_msgs generator and should not be manually modified. See the http://ros.org/wiki/sensor_msgs documentation for the documentation of the ROS messages in this typekit."


pkgname='ros-kinetic-rtt-sensor-msgs'
pkgver='2.9.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
'ros-kinetic-rtt-geometry-msgs'
'ros-kinetic-rtt-roscomm'
'ros-kinetic-rtt-std-msgs'
'ros-kinetic-sensor-msgs'
)

depends=('ros-kinetic-rtt-geometry-msgs'
'ros-kinetic-rtt-roscomm'
'ros-kinetic-rtt-std-msgs'
'ros-kinetic-sensor-msgs'
)

conflicts=()
replaces=()

_dir=rtt_sensor_msgs
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtt_sensor_msgs $srcdir/rtt_sensor_msgs
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

