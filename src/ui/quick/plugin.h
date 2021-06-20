#pragma once

#include <QQmlEngine>
#include <QQmlExtensionPlugin>

class plugin : public QQmlExtensionPlugin {
  Q_OBJECT
  Q_PLUGIN_METADATA(IID "ui.quick/1.0")
public:
  plugin() = default;
  ~plugin() override = default;

  void registerTypes(const char *uri) override;
};
