# Script generated with Bloom
pkgdesc="ROS - This package provides an RTT service and service-requester for associating RTT component properties with ROS parameters"
url='http://ros.org/wiki/rtt_ros_integration'

pkgname='ros-kinetic-rtt-rosparam'
pkgver='2.9.1_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('eigen3'
'ros-kinetic-catkin'
'ros-kinetic-roscpp'
'ros-kinetic-rtt-ros'
)

depends=('eigen3'
'ros-kinetic-roscpp'
'ros-kinetic-rtt-ros'
)

conflicts=()
replaces=()

_dir=rtt_rosparam
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtt_rosparam $srcdir/rtt_rosparam
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

