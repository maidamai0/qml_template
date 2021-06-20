#include "plugin.h"
#include "clock.h"

void plugin::registerTypes(const char *uri) {
  Q_ASSERT(uri == QLatin1String("ui.quick"));
  qmlRegisterType<Clock>(uri, 1, 0, "Clock");
}
