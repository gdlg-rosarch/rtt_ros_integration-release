# Script generated with Bloom
pkgdesc="ROS - This stack contains all software necessary to build systems using both Orocos and ROS infrastructures"
url='http://ros.org/wiki/rtt_ros_integration'

pkgname='ros-kinetic-rtt-ros-integration'
pkgver='2.9.1_1'
pkgrel=1
arch=('any')
license=('GPL'
'BSD'
'LGPL'
'GPL + runtime exception'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-rtt-actionlib'
'ros-kinetic-rtt-dynamic-reconfigure'
'ros-kinetic-rtt-ros'
'ros-kinetic-rtt-ros-msgs'
'ros-kinetic-rtt-rosclock'
'ros-kinetic-rtt-roscomm'
'ros-kinetic-rtt-rosdeployment'
'ros-kinetic-rtt-rosnode'
'ros-kinetic-rtt-rospack'
'ros-kinetic-rtt-rosparam'
'ros-kinetic-rtt-tf'
)

conflicts=()
replaces=()

_dir=rtt_ros_integration
source=()
md5sums=()

prepare() {
    cp -R $startdir/rtt_ros_integration $srcdir/rtt_ros_integration
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

