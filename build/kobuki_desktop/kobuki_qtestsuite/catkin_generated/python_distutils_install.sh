#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/eduardo/ws/kobuki/src/kobuki_desktop/kobuki_qtestsuite"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/eduardo/ws/kobuki/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/eduardo/ws/kobuki/install/lib/python2.7/dist-packages:/home/eduardo/ws/kobuki/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/eduardo/ws/kobuki/build" \
    "/usr/bin/python" \
    "/home/eduardo/ws/kobuki/src/kobuki_desktop/kobuki_qtestsuite/setup.py" \
    build --build-base "/home/eduardo/ws/kobuki/build/kobuki_desktop/kobuki_qtestsuite" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/eduardo/ws/kobuki/install" --install-scripts="/home/eduardo/ws/kobuki/install/bin"
