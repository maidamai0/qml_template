import QtQuick 2.15
import QtQuick.Controls 2.15

import ui.quick 1.0

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Scroll")
    Text {
        id: name
        text:clock.second
    }

    Clock {
        id: clock
    }
}
